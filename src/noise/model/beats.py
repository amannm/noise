from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Mapping

import numpy as np


def _require_torch():
    try:
        import torch
    except ModuleNotFoundError as exc:  # pragma: no cover - only hit without torch installed
        raise ModuleNotFoundError(
            "torch is required for BEATs. Install it before using noise.model.beats."
        ) from exc
    return torch


@dataclass(frozen=True)
class BeatsConfig:
    checkpoint_path: Path
    target_sr: int = 16000
    device: str | None = None


@dataclass
class BeatsEncoder:
    config: BeatsConfig
    model: Any

    def to_device(self) -> None:
        if self.config.device:
            self.model.to(self.config.device)

    def eval(self) -> None:
        self.model.eval()


def beats_model_factory(checkpoint: Mapping[str, Any]) -> Any:
    try:
        from beats import BEATs, BEATsConfig
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError(
            "BEATs module not found. Install the official BEATs repo on PYTHONPATH "
            "or provide a custom model_factory."
        ) from exc

    cfg = checkpoint.get("cfg")
    if cfg is None:
        raise ValueError("BEATs checkpoint missing 'cfg' entry.")
    if not isinstance(cfg, dict) and hasattr(cfg, "__dict__"):
        cfg = dict(cfg.__dict__)
    if not isinstance(cfg, dict):
        raise ValueError("BEATs checkpoint cfg must be a dict-like object.")

    return BEATs(BEATsConfig(cfg))


def load_beats_encoder(
    config: BeatsConfig,
    *,
    model_factory: Callable[[Mapping[str, Any]], Any] = beats_model_factory,
    strict: bool = False,
) -> BeatsEncoder:
    torch = _require_torch()
    checkpoint = torch.load(config.checkpoint_path, map_location="cpu")
    if not isinstance(checkpoint, dict):
        raise ValueError("Expected BEATs checkpoint to be a mapping with 'cfg'/'model' entries.")

    model = model_factory(checkpoint)
    state = checkpoint.get("model", checkpoint)
    model.load_state_dict(state, strict=strict)

    encoder = BeatsEncoder(config=config, model=model)
    encoder.eval()
    encoder.to_device()
    return encoder


def encode_audio(
    encoder: BeatsEncoder,
    audio: np.ndarray,
    *,
    sample_rate: int,
    normalize: bool = False,
) -> Any:
    if sample_rate != encoder.config.target_sr:
        raise ValueError(
            f"Expected sample_rate={encoder.config.target_sr}, got {sample_rate}. "
            "Resample before calling encode_audio."
        )

    torch = _require_torch()
    device = encoder.config.device or "cpu"

    if audio.ndim == 1:
        tensor = torch.from_numpy(audio.astype(np.float32, copy=False)).unsqueeze(0).to(device)
    elif audio.ndim == 2:
        tensor = torch.from_numpy(audio.astype(np.float32, copy=False)).to(device)
    else:
        raise ValueError(f"Expected mono audio shape (T,) or (B, T), got {audio.shape}")

    if normalize:
        tensor = tensor - tensor.mean(dim=1, keepdim=True)

    if hasattr(encoder.model, "extract_features"):
        output = encoder.model.extract_features(tensor, padding_mask=None)
    else:
        output = encoder.model(tensor)

    if isinstance(output, dict):
        for key in ("x", "features", "encoder_out", "logits"):
            if key in output:
                return output[key]
        raise RuntimeError("Unexpected BEATs output dict; adjust key selection in encode_audio.")
    if isinstance(output, (list, tuple)) and output:
        return output[0]
    return output
