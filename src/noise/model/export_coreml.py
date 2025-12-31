from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from noise.config.loader import get_float, get_nested, get_path, load_config, load_default_config
from noise.model.head import TemporalHeadConfig, build_temporal_head


def _require_torch():
    try:
        import torch
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError("torch is required for Core ML export.") from exc
    return torch


def _require_coremltools():
    try:
        import coremltools as ct
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError("coremltools is required for Core ML export.") from exc
    return ct


def _load_head_checkpoint(
    path: Path,
    *,
    head_config: TemporalHeadConfig | None,
) -> tuple[Any, TemporalHeadConfig]:
    torch = _require_torch()
    checkpoint = torch.load(path, map_location="cpu")
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
    return head, head_config


def _convert_torch_head(
    head: Any,
    head_config: TemporalHeadConfig,
    *,
    batch: int,
    frames: int,
    output: Path,
) -> None:
    torch = _require_torch()
    ct = _require_coremltools()

    head.eval()
    example = torch.randn(batch, frames, head_config.input_dim)
    traced = torch.jit.trace(head, example)

    inputs = [ct.TensorType(name="tokens", shape=example.shape)]
    mlmodel = ct.convert(traced, inputs=inputs)
    mlmodel.save(output.as_posix())


def _convert_onnx(
    onnx_path: Path,
    *,
    output: Path,
) -> None:
    ct = _require_coremltools()

    try:
        from coremltools.converters.onnx import convert as onnx_convert
    except Exception:
        onnx_convert = None

    if onnx_convert is not None:
        mlmodel = onnx_convert(onnx_path.as_posix())
    else:
        try:
            mlmodel = ct.convert(onnx_path.as_posix(), source="onnx")
        except TypeError as exc:  # pragma: no cover - depends on coremltools version
            raise ModuleNotFoundError(
                "coremltools ONNX converter not available. Install coremltools with ONNX support."
            ) from exc

    mlmodel.save(output.as_posix())


def main() -> None:
    parser = argparse.ArgumentParser(description="Export a temporal head or ONNX file to Core ML.")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--mode", choices=("head", "onnx"), default="head")
    parser.add_argument("--head-path", type=Path, default=None)
    parser.add_argument("--onnx-path", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--frames-per-s", type=float, default=100.0)
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--input-dim", type=int, default=None)
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_default_config()
    model_cfg = get_nested(config, "model")
    beats_cfg = get_nested(model_cfg, "beats")
    infer_cfg = get_nested(config, "inference")

    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)

    if args.mode == "onnx":
        onnx_path = args.onnx_path
        if onnx_path is None:
            raise ValueError("--onnx-path is required when mode=onnx")
        output = args.output or Path("models/model.mlpackage")
        _convert_onnx(onnx_path, output=output)
        print(f"Saved Core ML model to {output}")
        return

    head_path = args.head_path or get_path(beats_cfg, "head_path", Path("models/beats_head.pt"))
    head_cfg = None
    head_cfg_raw = beats_cfg.get("head")
    if isinstance(head_cfg_raw, dict):
        cfg_kwargs = dict(head_cfg_raw)
        input_dim = args.input_dim if args.input_dim is not None else cfg_kwargs.pop("input_dim", 0)
        head_cfg = TemporalHeadConfig(input_dim=input_dim, **cfg_kwargs)
    elif args.input_dim is not None:
        head_cfg = TemporalHeadConfig(input_dim=args.input_dim)

    head, head_cfg = _load_head_checkpoint(head_path, head_config=head_cfg)

    frames = args.frames
    if frames is None:
        frames = max(1, int(window_s * args.frames_per_s))

    output = args.output or Path("models/beats_head.mlpackage")
    _convert_torch_head(head, head_cfg, batch=args.batch, frames=frames, output=output)
    print(f"Saved Core ML model to {output}")


if __name__ == "__main__":
    main()
