from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import yaml

from noise.config.loader import (
    get_float,
    get_int,
    get_nested,
    get_path,
    load_config,
    load_default_config,
    merge_config,
)
from noise.model.baseline import LABELS, BaselineFeatureConfig, extract_features, load_bundle
from noise.training.dataset import WindowConfig, WindowedWavDataset, list_wav_files


def _build_matrix(dataset: WindowedWavDataset, feature_config: BaselineFeatureConfig) -> tuple[np.ndarray, np.ndarray]:
    features = []
    labels = []
    for audio, label, _ in dataset:
        features.append(extract_features(audio, feature_config))
        labels.append(label)
    if not features:
        return np.zeros((0, feature_config.feature_dim()), dtype=np.float32), np.zeros((0, len(LABELS)))
    return np.stack(features, axis=0), np.stack(labels, axis=0)


def _calibrate_thresholds(
    probs: np.ndarray,
    labels: np.ndarray,
    p_off: float,
    p_on: float,
    min_gap: float,
) -> dict[str, dict[str, float]]:
    thresholds: dict[str, dict[str, float]] = {}
    for idx, name in enumerate(LABELS):
        present = probs[labels[:, idx] == 1, idx]
        absent = probs[labels[:, idx] == 0, idx]
        if present.size == 0 or absent.size == 0:
            raise ValueError(f"Need both present and absent samples for {name}")
        t_off = float(np.percentile(absent, p_off))
        t_on = float(np.percentile(present, p_on))
        if t_on < t_off + min_gap:
            t_on = min(1.0, t_off + min_gap)
        thresholds[name] = {"t_on": t_on, "t_off": t_off}
    return thresholds


def main() -> None:
    parser = argparse.ArgumentParser(description="Calibrate hysteresis thresholds from steady-state clips.")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--model-path", type=Path, default=None)
    parser.add_argument("--sample-rate", type=int, default=None)
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--hop-s", type=float, default=None)
    parser.add_argument("--p-off", type=float, default=96.0)
    parser.add_argument("--p-on", type=float, default=12.0)
    parser.add_argument("--min-gap", type=float, default=0.10)
    parser.add_argument("--base-config", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=Path("calibrated.yaml"))
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_default_config()
    audio_cfg = get_nested(config, "audio")
    infer_cfg = get_nested(config, "inference")
    model_cfg = get_nested(config, "model")

    model_path = args.model_path or get_path(model_cfg, "path", Path("models/baseline.joblib"))
    bundle = load_bundle(model_path)

    sample_rate = args.sample_rate if args.sample_rate is not None else get_int(audio_cfg, "sample_rate", 16000)
    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)
    hop_s = args.hop_s if args.hop_s is not None else get_float(infer_cfg, "hop_s", 0.5)

    if sample_rate != bundle.config.sample_rate:
        print(
            f"Warning: overriding sample_rate {sample_rate} -> {bundle.config.sample_rate} to match model config."
        )
    window_config = WindowConfig(
        sample_rate=bundle.config.sample_rate,
        window_s=window_s,
        hop_s=hop_s,
        strict_labels=not args.allow_heuristics,
    )
    feature_config = bundle.config

    files = list_wav_files(args.samples_dir)
    dataset = WindowedWavDataset(args.samples_dir, window_config, files=files)
    x, y = _build_matrix(dataset, feature_config)
    probs = bundle.predict_proba(x)

    thresholds = _calibrate_thresholds(probs, y, args.p_off, args.p_on, args.min_gap)

    base_cfg_path = args.base_config or args.config
    base_config = load_config(base_cfg_path) if base_cfg_path else {}
    overrides = {"hysteresis": {name: values for name, values in thresholds.items()}}
    merged = merge_config(base_config, overrides)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as f:
        yaml.safe_dump(merged, f, sort_keys=False)

    print("Calibrated thresholds:")
    for name, values in thresholds.items():
        print(f"  {name}: t_on={values['t_on']:.3f} t_off={values['t_off']:.3f}")
    print(f"Saved calibrated config to {args.output}")


if __name__ == "__main__":
    main()
