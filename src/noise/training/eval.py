from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score

from noise.model.baseline import LABELS, extract_features, load_bundle
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a baseline model on steady-state clips.")
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--model-path", type=Path, default=Path("models/baseline.joblib"))
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--window-s", type=float, default=4.0)
    parser.add_argument("--hop-s", type=float, default=0.5)
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    bundle = load_bundle(args.model_path)

    if args.sample_rate != bundle.config.sample_rate:
        print(
            f"Warning: overriding sample_rate {args.sample_rate} -> {bundle.config.sample_rate} to match model config."
        )
    window_config = WindowConfig(
        sample_rate=bundle.config.sample_rate,
        window_s=args.window_s,
        hop_s=args.hop_s,
        strict_labels=not args.allow_heuristics,
    )
    feature_config = bundle.config

    files = list_wav_files(args.samples_dir)
    dataset = WindowedWavDataset(args.samples_dir, window_config, files=files)
    x, y = _build_matrix(dataset, feature_config)
    probs = bundle.predict_proba(x)

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


if __name__ == "__main__":
    main()
