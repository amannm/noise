from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

import numpy as np

from noise.model.baseline import LABELS
from noise.model.beats import BeatsConfig, beats_model_factory, encode_audio, load_beats_encoder
from noise.model.head import TemporalHeadConfig, build_temporal_head


def _require_torch():
    try:
        import torch
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError(
            "torch is required for BEATs pipelines. Install it before using BeatsHeadBundle."
        ) from exc
    return torch


@dataclass
class BeatsHeadBundle:
    encoder: Any
    head: Any
    head_config: TemporalHeadConfig
    labels: tuple[str, ...] = LABELS

    @property
    def sample_rate(self) -> int:
        return self.encoder.config.target_sr

    def predict_proba_from_audio(self, audio: np.ndarray) -> np.ndarray:
        torch = _require_torch()
        self.encoder.eval()
        self.head.eval()
        with torch.no_grad():
            tokens = encode_audio(self.encoder, audio, sample_rate=self.sample_rate)
            tokens = _ensure_btd(tokens, input_dim=self.head_config.input_dim)
            logits = self.head(tokens)
            probs = torch.sigmoid(logits).cpu().numpy()
        return probs[0]


def load_beats_head_bundle(
    *,
    beats_config: BeatsConfig,
    head_path: Path,
    head_config: TemporalHeadConfig | None = None,
    model_factory=beats_model_factory,
) -> BeatsHeadBundle:
    torch = _require_torch()
    checkpoint = torch.load(head_path, map_location="cpu")
    state_dict = checkpoint
    checkpoint_cfg = None
    if isinstance(checkpoint, dict):
        if "state_dict" in checkpoint:
            state_dict = checkpoint["state_dict"]
        if "head_config" in checkpoint:
            checkpoint_cfg = TemporalHeadConfig(**checkpoint["head_config"])

    if checkpoint_cfg is not None:
        head_config = checkpoint_cfg

    if head_config is None:
        raise ValueError("head_config must be provided or stored in the head checkpoint.")

    head = build_temporal_head(head_config)
    head.load_state_dict(state_dict)

    if beats_config.device:
        head.to(beats_config.device)

    encoder = load_beats_encoder(beats_config, model_factory=model_factory)
    return BeatsHeadBundle(encoder=encoder, head=head, head_config=head_config)


def save_head_checkpoint(path: Path, head: Any, head_config: TemporalHeadConfig) -> None:
    torch = _require_torch()
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {"state_dict": head.state_dict(), "head_config": asdict(head_config)},
        path,
    )


def _ensure_btd(tokens: Any, *, input_dim: int | None = None) -> Any:
    torch = _require_torch()
    if not isinstance(tokens, torch.Tensor):
        tokens = torch.as_tensor(tokens)
    if tokens.ndim == 2:
        tokens = tokens.unsqueeze(0)
    if tokens.ndim != 3:
        raise ValueError(f"Expected token tensor with 3 dims (B,T,D), got {tokens.shape}")

    b, t, d = tokens.shape
    if input_dim is not None:
        if d == input_dim:
            return tokens
        if t == input_dim:
            return tokens.transpose(1, 2)
    if t > d:
        tokens = tokens.transpose(1, 2)
    return tokens
