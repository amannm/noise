from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path
from typing import Any

from noise.config.loader import get_float, get_int, get_nested, get_path, load_config, load_default_config
from noise.model.beats import BeatsConfig, load_beats_encoder
from noise.model.head import TemporalHeadConfig, build_temporal_head


def _require_torch():
    try:
        import torch
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError("torch is required for ONNX export.") from exc
    return torch


def _require_onnx() -> None:
    try:
        import onnx  # noqa: F401
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError(
            "onnx is required for export. Install it before running export_onnx."
        ) from exc


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


def _extract_tokens(output: Any) -> Any:
    if isinstance(output, dict):
        for key in ("x", "features", "encoder_out", "logits"):
            if key in output:
                return output[key]
        raise RuntimeError("Unexpected BEATs output dict; adjust key selection in export_onnx.")
    if isinstance(output, (list, tuple)) and output:
        return output[0]
    return output


def _ensure_btd(tokens: Any, *, input_dim: int | None = None) -> Any:
    torch = _require_torch()
    if not isinstance(tokens, torch.Tensor):
        tokens = torch.as_tensor(tokens)
    if tokens.ndim == 2:
        tokens = tokens.unsqueeze(0)
    if tokens.ndim != 3:
        raise ValueError(f"Expected token tensor with 3 dims (B,T,D), got {tokens.shape}")

    _, t, d = tokens.shape
    if input_dim is not None:
        if d == input_dim:
            return tokens
        if t == input_dim:
            return tokens.transpose(1, 2)
    if t > d:
        tokens = tokens.transpose(1, 2)
    return tokens


def _export_head(
    head: Any,
    head_config: TemporalHeadConfig,
    output_path: Path,
    *,
    batch: int,
    frames: int,
    opset: int,
    dynamic_axes: bool,
) -> None:
    torch = _require_torch()
    head.eval()
    dummy = torch.randn(batch, frames, head_config.input_dim)
    dyn = None
    if dynamic_axes:
        dyn = {"tokens": {0: "batch", 1: "frames"}, "logits": {0: "batch"}}
    torch.onnx.export(
        head,
        dummy,
        output_path.as_posix(),
        input_names=["tokens"],
        output_names=["logits"],
        dynamic_axes=dyn,
        opset_version=opset,
        do_constant_folding=True,
    )


def _export_beats_head(
    encoder: Any,
    head: Any,
    head_config: TemporalHeadConfig,
    output_path: Path,
    *,
    batch: int,
    samples: int,
    opset: int,
    dynamic_axes: bool,
    normalize: bool,
) -> None:
    torch = _require_torch()

    class BeatsHeadModule(torch.nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.encoder = encoder.model
            self.head = head

        def forward(self, audio: torch.Tensor) -> torch.Tensor:
            x = audio
            if normalize:
                x = x - x.mean(dim=1, keepdim=True)
            if hasattr(self.encoder, "extract_features"):
                output = self.encoder.extract_features(x, padding_mask=None)
            else:
                output = self.encoder(x)
            tokens = _extract_tokens(output)
            tokens = _ensure_btd(tokens, input_dim=head_config.input_dim)
            return self.head(tokens)

    module = BeatsHeadModule()
    module.eval()
    dummy = torch.randn(batch, samples)
    dyn = None
    if dynamic_axes:
        dyn = {"audio": {0: "batch", 1: "samples"}, "logits": {0: "batch"}}
    torch.onnx.export(
        module,
        dummy,
        output_path.as_posix(),
        input_names=["audio"],
        output_names=["logits"],
        dynamic_axes=dyn,
        opset_version=opset,
        do_constant_folding=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Export temporal head or BEATs+head to ONNX.")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--mode", choices=("head", "full"), default="head")
    parser.add_argument("--head-path", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--device", type=str, default=None)
    parser.add_argument("--opset", type=int, default=17)
    parser.add_argument("--batch", type=int, default=1)
    parser.add_argument("--frames", type=int, default=None)
    parser.add_argument("--frames-per-s", type=float, default=100.0)
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--no-dynamic-axes", action="store_true")
    parser.add_argument("--no-normalize", action="store_true")
    parser.add_argument("--input-dim", type=int, default=None)
    args = parser.parse_args()

    _require_onnx()
    torch = _require_torch()

    config = load_config(args.config) if args.config else load_default_config()
    model_cfg = get_nested(config, "model")
    beats_cfg = get_nested(model_cfg, "beats")
    infer_cfg = get_nested(config, "inference")

    head_path = args.head_path or get_path(beats_cfg, "head_path", Path("models/beats_head.pt"))
    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)
    target_sr = get_int(beats_cfg, "target_sr", 16000)

    head_cfg = None
    head_cfg_raw = beats_cfg.get("head")
    if isinstance(head_cfg_raw, dict):
        cfg_kwargs = dict(head_cfg_raw)
        input_dim = args.input_dim if args.input_dim is not None else cfg_kwargs.pop("input_dim", 0)
        head_cfg = TemporalHeadConfig(input_dim=input_dim, **cfg_kwargs)
    elif args.input_dim is not None:
        head_cfg = TemporalHeadConfig(input_dim=args.input_dim)

    head, head_cfg = _load_head_checkpoint(head_path, head_config=head_cfg)
    if args.device:
        head.to(args.device)

    dynamic_axes = not args.no_dynamic_axes
    if args.mode == "head":
        if args.output is None:
            output = Path("models/beats_head.onnx")
        else:
            output = args.output
        frames = args.frames
        if frames is None:
            frames = max(1, int(window_s * args.frames_per_s))
        _export_head(
            head,
            head_cfg,
            output,
            batch=args.batch,
            frames=frames,
            opset=args.opset,
            dynamic_axes=dynamic_axes,
        )
        print(f"Exported head ONNX to {output}")
        return

    if args.output is None:
        output = Path("models/beats_full.onnx")
    else:
        output = args.output

    device = args.device or beats_cfg.get("device") or "cpu"
    beats_config = BeatsConfig(
        checkpoint_path=get_path(beats_cfg, "checkpoint_path", Path("models/BEATs_iter3_plus_AS2M.pt")),
        target_sr=target_sr,
        device=device,
    )
    encoder = load_beats_encoder(beats_config)
    if args.device:
        encoder.model.to(args.device)

    samples = max(1, int(window_s * target_sr))
    _export_beats_head(
        encoder,
        head,
        head_cfg,
        output,
        batch=args.batch,
        samples=samples,
        opset=args.opset,
        dynamic_axes=dynamic_axes,
        normalize=not args.no_normalize,
    )
    print(f"Exported BEATs+head ONNX to {output}")


if __name__ == "__main__":
    main()
