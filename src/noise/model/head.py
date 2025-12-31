from __future__ import annotations

from dataclasses import dataclass
from typing import Any


def _require_torch():
    try:
        import torch
        from torch import nn
    except ModuleNotFoundError as exc:  # pragma: no cover - only hit without torch installed
        raise ModuleNotFoundError(
            "torch is required for the temporal head. Install it before using noise.model.head."
        ) from exc
    return torch, nn


@dataclass(frozen=True)
class TemporalHeadConfig:
    input_dim: int
    hidden_dim: int = 256
    conv_channels: int = 128
    kernel_size: int = 3
    num_layers: int = 1
    dropout: float = 0.1
    bidirectional: bool = True
    num_outputs: int = 2


def build_temporal_head(config: TemporalHeadConfig) -> Any:
    torch, nn = _require_torch()

    class TemporalHead(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            padding = max(0, config.kernel_size // 2)
            self.conv = nn.Conv1d(
                in_channels=config.input_dim,
                out_channels=config.conv_channels,
                kernel_size=config.kernel_size,
                padding=padding,
            )
            self.act = nn.ReLU()
            self.dropout = nn.Dropout(config.dropout)
            self.gru = nn.GRU(
                input_size=config.conv_channels,
                hidden_size=config.hidden_dim,
                num_layers=config.num_layers,
                batch_first=True,
                bidirectional=config.bidirectional,
            )
            out_dim = config.hidden_dim * (2 if config.bidirectional else 1)
            self.proj = nn.Linear(out_dim, config.num_outputs)

        def forward(self, tokens: torch.Tensor, lengths: torch.Tensor | None = None) -> torch.Tensor:
            if tokens.ndim != 3:
                raise ValueError(f"Expected tokens shape (B, T, D), got {tokens.shape}")
            x = tokens.transpose(1, 2)
            x = self.conv(x)
            x = self.act(x)
            x = self.dropout(x)
            x = x.transpose(1, 2)
            x, _ = self.gru(x)

            if lengths is None:
                pooled = x.mean(dim=1)
            else:
                pooled = _masked_mean(x, lengths)
            return self.proj(pooled)

    return TemporalHead()


def _masked_mean(values: Any, lengths: Any) -> Any:
    torch, _ = _require_torch()
    if lengths.ndim != 1:
        raise ValueError("lengths must be 1D (batch,)")
    max_len = values.size(1)
    mask = torch.arange(max_len, device=values.device)[None, :] < lengths[:, None]
    mask = mask.unsqueeze(-1).to(values.dtype)
    summed = (values * mask).sum(dim=1)
    denom = mask.sum(dim=1).clamp_min(1.0)
    return summed / denom
