from __future__ import annotations

from pathlib import Path
from typing import Any

from noise.config.loader import get_int, get_nested, get_path
from noise.model.baseline import BaselineBundle, load_bundle
from noise.model.beats import BeatsConfig
from noise.model.head import TemporalHeadConfig
from noise.model.pipeline import BeatsHeadBundle, load_beats_head_bundle


def load_inference_model(
    config: dict[str, Any],
    *,
    model_path: Path | None = None,
    device: str | None = None,
) -> BaselineBundle | BeatsHeadBundle:
    model_cfg = get_nested(config, "model")
    model_type = str(model_cfg.get("type", "baseline")).lower()

    if model_type == "beats":
        beats_cfg = get_nested(model_cfg, "beats")
        checkpoint_path = get_path(beats_cfg, "checkpoint_path", Path("models/BEATs_iter3_plus_AS2M.pt"))
        head_path = model_path or get_path(beats_cfg, "head_path", Path("models/beats_head.pt"))
        target_sr = get_int(beats_cfg, "target_sr", 16000)
        device_name = device or beats_cfg.get("device")

        head_cfg = None
        head_cfg_raw = beats_cfg.get("head")
        if isinstance(head_cfg_raw, dict) and "input_dim" in head_cfg_raw:
            head_cfg = TemporalHeadConfig(**head_cfg_raw)

        beats_config = BeatsConfig(
            checkpoint_path=checkpoint_path,
            target_sr=target_sr,
            device=device_name,
        )
        return load_beats_head_bundle(
            beats_config=beats_config,
            head_path=head_path,
            head_config=head_cfg,
        )

    model_path = model_path or get_path(model_cfg, "path", Path("models/baseline.joblib"))
    return load_bundle(model_path)
