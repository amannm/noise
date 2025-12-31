from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score

from noise.config.loader import (
    get_float,
    get_int,
    get_nested,
    load_config,
    load_default_config,
)
from noise.model.baseline import LABELS, BaselineBundle, BaselineFeatureConfig, extract_features
from noise.model.loader import load_inference_model
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


def _predict_probs(dataset: WindowedWavDataset, bundle) -> tuple[np.ndarray, np.ndarray]:
    probs = []
    labels = []
    for audio, label, _ in dataset:
        probs.append(bundle.predict_proba_from_audio(audio))
        labels.append(label)
    if not probs:
        return np.zeros((0, len(LABELS)), dtype=np.float32), np.zeros((0, len(LABELS)))
    return np.stack(probs, axis=0), np.stack(labels, axis=0)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a baseline model on steady-state clips.")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--model-path", type=Path, default=None, help="Overrides baseline model or BEATs head path.")
    parser.add_argument("--sample-rate", type=int, default=None)
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--hop-s", type=float, default=None)
    parser.add_argument("--hist-out", type=Path, default=None, help="Optional CSV path for probability histograms.")
    parser.add_argument("--hist-bins", type=int, default=50)
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_default_config()
    audio_cfg = get_nested(config, "audio")
    infer_cfg = get_nested(config, "inference")

    bundle = load_inference_model(config, model_path=args.model_path)

    sample_rate = args.sample_rate if args.sample_rate is not None else get_int(audio_cfg, "sample_rate", 16000)
    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)
    hop_s = args.hop_s if args.hop_s is not None else get_float(infer_cfg, "hop_s", 0.5)

    if sample_rate != bundle.sample_rate:
        print(f"Warning: overriding sample_rate {sample_rate} -> {bundle.sample_rate} to match model config.")
    window_config = WindowConfig(
        sample_rate=bundle.sample_rate,
        window_s=window_s,
        hop_s=hop_s,
        strict_labels=not args.allow_heuristics,
    )
    feature_config = bundle.config if isinstance(bundle, BaselineBundle) else None

    files = list_wav_files(args.samples_dir)
    dataset = WindowedWavDataset(args.samples_dir, window_config, files=files)
    if isinstance(bundle, BaselineBundle):
        x, y = _build_matrix(dataset, feature_config)
        probs = bundle.predict_proba(x)
    else:
        probs, y = _predict_probs(dataset, bundle)

    print(f"Evaluated {len(files)} files / {len(dataset)} windows")
    for idx, label in enumerate(LABELS):
        try:
            auroc = roc_auc_score(y[:, idx], probs[:, idx])
        except ValueError:
            auroc = float("nan")
        try:
            auprc = average_precision_score(y[:, idx], probs[:, idx])
        except ValueError:
            auprc = float("nan")
        print(f"  {label}: AUROC={auroc:.4f} AUPRC={auprc:.4f}")

    if args.hist_out:
        if args.hist_bins <= 1:
            raise ValueError("hist-bins must be > 1")
        edges = np.linspace(0.0, 1.0, args.hist_bins + 1)
        rows: list[dict[str, object]] = []
        for idx, label in enumerate(LABELS):
            present = probs[y[:, idx] == 1, idx]
            absent = probs[y[:, idx] == 0, idx]
            present_hist, _ = np.histogram(present, bins=edges)
            absent_hist, _ = np.histogram(absent, bins=edges)
            for bin_idx in range(args.hist_bins):
                rows.append(
                    {
                        "label": label,
                        "bin_start": float(edges[bin_idx]),
                        "bin_end": float(edges[bin_idx + 1]),
                        "present_count": int(present_hist[bin_idx]),
                        "absent_count": int(absent_hist[bin_idx]),
                    }
                )
        args.hist_out.parent.mkdir(parents=True, exist_ok=True)
        with args.hist_out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["label", "bin_start", "bin_end", "present_count", "absent_count"],
            )
            writer.writeheader()
            writer.writerows(rows)
        print(f"Wrote histogram CSV to {args.hist_out}")


if __name__ == "__main__":
    main()
