from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split

from noise.model.baseline import (
    LABELS,
    BaselineBundle,
    BaselineFeatureConfig,
    build_estimator,
    extract_features,
    save_bundle,
)
from noise.training.dataset import WindowConfig, WindowedWavDataset, label_from_path, list_wav_files


def _build_matrix(dataset: WindowedWavDataset, feature_config: BaselineFeatureConfig) -> tuple[np.ndarray, np.ndarray]:
    features = []
    labels = []
    for audio, label, _ in dataset:
        features.append(extract_features(audio, feature_config))
        labels.append(label)
    if not features:
        return np.zeros((0, feature_config.feature_dim()), dtype=np.float32), np.zeros((0, len(LABELS)))
    return np.stack(features, axis=0), np.stack(labels, axis=0)


def _print_metrics(split: str, y_true: np.ndarray, y_prob: np.ndarray) -> None:
    print(f"\n{split} metrics:")
    for idx, label in enumerate(LABELS):
        try:
            auroc = roc_auc_score(y_true[:, idx], y_prob[:, idx])
        except ValueError:
            auroc = float("nan")
        try:
            auprc = average_precision_score(y_true[:, idx], y_prob[:, idx])
        except ValueError:
            auprc = float("nan")
        print(f"  {label}: AUROC={auroc:.4f} AUPRC={auprc:.4f}")


def _has_label_coverage(labels: np.ndarray) -> bool:
    if labels.size == 0:
        return False
    for idx in range(labels.shape[1]):
        if not ((labels[:, idx] == 1).any() and (labels[:, idx] == 0).any()):
            return False
    return True


def _split_files_with_coverage(
    files: list[Path],
    train_split: float,
    seed: int,
    strict_labels: bool,
) -> tuple[list[Path], list[Path]]:
    if len(files) < 2:
        return files, []

    train_files, val_files = train_test_split(
        files, train_size=train_split, random_state=seed, shuffle=True
    )
    train_labels = np.array([label_from_path(path, strict=strict_labels) for path in train_files])
    if _has_label_coverage(train_labels):
        return train_files, val_files

    # Move files from val to train until coverage is satisfied or val is empty.
    for path in list(val_files):
        train_files.append(path)
        val_files.remove(path)
        train_labels = np.array([label_from_path(p, strict=strict_labels) for p in train_files])
        if _has_label_coverage(train_labels):
            return train_files, val_files

    # Fallback: use all files for training if coverage cannot be met.
    return files, []


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a baseline log-mel + logistic model.")
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--model-out", type=Path, default=Path("models/baseline.joblib"))
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--window-s", type=float, default=4.0)
    parser.add_argument("--hop-s", type=float, default=0.5)
    parser.add_argument("--train-split", type=float, default=0.8)
    parser.add_argument("--seed", type=int, default=13)
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    window_config = WindowConfig(
        sample_rate=args.sample_rate,
        window_s=args.window_s,
        hop_s=args.hop_s,
        strict_labels=not args.allow_heuristics,
    )
    feature_config = BaselineFeatureConfig(sample_rate=args.sample_rate)

    files = list_wav_files(args.samples_dir)
    if len(files) < 2:
        raise ValueError("Need at least 2 WAV files for train/val split")

    train_files, val_files = _split_files_with_coverage(
        files,
        train_split=args.train_split,
        seed=args.seed,
        strict_labels=not args.allow_heuristics,
    )

    train_ds = WindowedWavDataset(args.samples_dir, window_config, files=train_files)
    val_ds = WindowedWavDataset(args.samples_dir, window_config, files=val_files) if val_files else None

    print(f"Train files: {len(train_files)}  Val files: {len(val_files)}")
    print(f"Train windows: {len(train_ds)}")
    if val_ds is not None:
        print(f"Val windows: {len(val_ds)}")

    x_train, y_train = _build_matrix(train_ds, feature_config)
    x_val, y_val = (None, None)
    if val_ds is not None:
        x_val, y_val = _build_matrix(val_ds, feature_config)

    estimator = build_estimator(random_state=args.seed)
    estimator.fit(x_train, y_train)

    bundle = BaselineBundle(config=feature_config, estimator=estimator)
    save_bundle(bundle, args.model_out)
    print(f"Saved model to {args.model_out}")

    train_probs = bundle.predict_proba(x_train)
    _print_metrics("Train", y_train, train_probs)
    if x_val is not None and y_val is not None and len(y_val) > 0:
        val_probs = bundle.predict_proba(x_val)
        _print_metrics("Val", y_val, val_probs)


if __name__ == "__main__":
    main()
