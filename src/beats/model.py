from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional

import torch
import torch.nn as nn

PROJECT_ROOT = Path(__file__).resolve().parents[2]
BEATS_DIR = PROJECT_ROOT / "reference" / "unilm" / "beats"
if str(BEATS_DIR) not in sys.path:
    sys.path.insert(0, str(BEATS_DIR))

from BEATs import BEATs, BEATsConfig  # type: ignore

def load_beats_checkpoint(
    checkpoint_path: str | Path,
    device: Optional[torch.device | str] = None,
) -> BEATs:
    checkpoint = torch.load(checkpoint_path, map_location="cpu")
    cfg = BEATsConfig(checkpoint["cfg"])
    model = BEATs(cfg)
    model.load_state_dict(checkpoint["model"])
    if device is not None:
        model = model.to(device)
    return model


class AttentionPooling(nn.Module):
    def __init__(self, dim: int) -> None:
        super().__init__()
        self.attn = nn.Linear(dim, 1)

    def forward(
        self, features: torch.Tensor, padding_mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        # features: (batch, frames, dim)
        scores = self.attn(features).squeeze(-1)
        if padding_mask is not None:
            scores = scores.masked_fill(padding_mask, float("-inf"))
        weights = torch.softmax(scores, dim=1)
        pooled = torch.sum(features * weights.unsqueeze(-1), dim=1)
        return pooled


class NoiseClassifier(nn.Module):
    def __init__(
        self,
        beats: BEATs,
        head_dim: int = 256,
        dropout: float = 0.2,
    ) -> None:
        super().__init__()
        self.beats = beats
        embed_dim = beats.cfg.encoder_embed_dim

        self.pool = AttentionPooling(embed_dim)
        self.head = nn.Sequential(
            nn.Dropout(dropout),
            nn.Linear(embed_dim, head_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(head_dim, 2),
        )

    def encode_fbank(
        self, fbank: torch.Tensor, padding_mask: Optional[torch.Tensor] = None
    ) -> tuple[torch.Tensor, Optional[torch.Tensor]]:
        # fbank: (batch, frames, mel)
        if padding_mask is not None:
            padding_mask = self.beats.forward_padding_mask(fbank, padding_mask)

        fbank = fbank.unsqueeze(1)
        features = self.beats.patch_embedding(fbank)
        features = features.reshape(features.shape[0], features.shape[1], -1)
        features = features.transpose(1, 2)
        features = self.beats.layer_norm(features)

        if padding_mask is not None:
            padding_mask = self.beats.forward_padding_mask(features, padding_mask)

        if self.beats.post_extract_proj is not None:
            features = self.beats.post_extract_proj(features)

        x = self.beats.dropout_input(features)
        x, _ = self.beats.encoder(x, padding_mask=padding_mask)
        return x, padding_mask

    def forward(self, fbank: torch.Tensor) -> torch.Tensor:
        # fbank: (batch, frames, mel)
        features, padding_mask = self.encode_fbank(fbank, padding_mask=None)
        pooled = self.pool(features, padding_mask)
        logits = self.head(pooled)
        return logits

    def forward_waveform(self, waveform: torch.Tensor) -> torch.Tensor:
        # waveform: (batch, samples) at 16 kHz
        features, padding_mask = self.beats.extract_features(waveform)
        pooled = self.pool(features, padding_mask)
        logits = self.head(pooled)
        return logits

    def freeze_beats(self) -> None:
        for param in self.beats.parameters():
            param.requires_grad = False

    def unfreeze_last_blocks(self, num_blocks: int) -> None:
        for param in self.beats.parameters():
            param.requires_grad = False
        if num_blocks <= 0:
            return
        layers = self.beats.encoder.layers
        for layer in layers[-num_blocks:]:
            for param in layer.parameters():
                param.requires_grad = True
