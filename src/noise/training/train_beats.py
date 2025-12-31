from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path

import numpy as np
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split

from noise.config.loader import (
    get_float,
    get_int,
    get_nested,
    get_path,
    load_config,
    load_default_config,
)
from noise.model.baseline import LABELS
from noise.model.beats import BeatsConfig, encode_audio, load_beats_encoder
from noise.model.head import TemporalHeadConfig, build_temporal_head
from noise.model.pipeline import save_head_checkpoint
from noise.training.augment import AudioAugmenter, augment_config_from_dict, build_noise_pool
from noise.training.dataset import WindowConfig, WindowedWavDataset, label_from_path, list_wav_files
from noise.training.splits import split_config_from_dict


def _require_torch():
    try:
        import torch
    except ModuleNotFoundError as exc:  # pragma: no cover - optional dependency
        raise ModuleNotFoundError("torch is required for BEATs training.") from exc
    return torch


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

    for path in list(val_files):
        train_files.append(path)
        val_files.remove(path)
        train_labels = np.array([label_from_path(p, strict=strict_labels) for p in train_files])
        if _has_label_coverage(train_labels):
            return train_files, val_files

    return files, []


def _iter_batches(dataset: WindowedWavDataset, batch_size: int, indices: np.ndarray | None = None):
    batch_audio = []
    batch_labels = []
    iterable = (dataset[i] for i in indices) if indices is not None else dataset
    for audio, label, _ in iterable:
        batch_audio.append(audio)
        batch_labels.append(label)
        if len(batch_audio) >= batch_size:
            yield np.stack(batch_audio, axis=0), np.stack(batch_labels, axis=0)
            batch_audio.clear()
            batch_labels.clear()
    if batch_audio:
        yield np.stack(batch_audio, axis=0), np.stack(batch_labels, axis=0)


def _ensure_btd(tokens, *, input_dim: int | None = None):
    torch = _require_torch()
    if not isinstance(tokens, torch.Tensor):
        tokens = torch.as_tensor(tokens)
    if tokens.ndim == 2:
        tokens = tokens.unsqueeze(0)
    if tokens.ndim != 3:
        raise ValueError(f"Expected tokens shape (B,T,D), got {tokens.shape}")
    b, t, d = tokens.shape
    if input_dim is not None:
        if d == input_dim:
            return tokens
        if t == input_dim:
            return tokens.transpose(1, 2)
    if t > d:
        tokens = tokens.transpose(1, 2)
    return tokens


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


def main() -> None:
    parser = argparse.ArgumentParser(description="Train a BEATs encoder + temporal head (head-only).")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--checkpoint-path", type=Path, default=None, help="BEATs checkpoint path.")
    parser.add_argument("--head-out", type=Path, default=None, help="Output path for head checkpoint.")
    parser.add_argument("--device", type=str, default=None)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--hop-s", type=float, default=None)
    parser.add_argument("--train-split", type=float, default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--split-mode", type=str, default=None, choices=("ranges", "files", "windows"))
    parser.add_argument("--allow-heuristics", action="store_true")
    parser.add_argument("--no-augment", action="store_true", help="Disable audio augmentation for training.")
    parser.add_argument(
        "--window-split",
        action="store_true",
        help="Split train/val at the window level (ignores file boundaries).",
    )
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_default_config()
    audio_cfg = get_nested(config, "audio")
    infer_cfg = get_nested(config, "inference")
    model_cfg = get_nested(config, "model")
    train_cfg = get_nested(config, "training")

    beats_cfg = get_nested(model_cfg, "beats")
    checkpoint_path = args.checkpoint_path or get_path(
        beats_cfg, "checkpoint_path", Path("models/BEATs_iter3_plus_AS2M.pt")
    )
    head_out = args.head_out or get_path(beats_cfg, "head_path", Path("models/beats_head.pt"))
    device = args.device or beats_cfg.get("device") or "cpu"
    target_sr = get_int(beats_cfg, "target_sr", 16000)

    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)
    hop_s = args.hop_s if args.hop_s is not None else get_float(infer_cfg, "hop_s", 0.5)
    train_split = args.train_split if args.train_split is not None else get_float(train_cfg, "train_split", 0.8)
    seed = args.seed if args.seed is not None else get_int(train_cfg, "seed", 13)
    split_mode = args.split_mode or str(train_cfg.get("split_mode", "ranges")).lower()
    if args.window_split:
        split_mode = "windows"
    split_cfg = split_config_from_dict(get_nested(config, "splits"))
    augment_cfg = augment_config_from_dict(get_nested(train_cfg, "augment"))
    if args.no_augment:
        augment_cfg = replace(augment_cfg, enabled=False)

    cfg_sr = get_int(audio_cfg, "sample_rate", target_sr)
    if cfg_sr != target_sr:
        print(f"Warning: overriding sample_rate {cfg_sr} -> {target_sr} to match BEATs target_sr.")

    window_config = WindowConfig(
        sample_rate=target_sr,
        window_s=window_s,
        hop_s=hop_s,
        strict_labels=not args.allow_heuristics,
    )

    files = list_wav_files(args.samples_dir)
    if not files:
        raise ValueError("No WAV files found for training.")

    train_ds = None
    val_ds = None
    train_indices = None
    val_indices = None

    if split_mode == "windows":
        dataset = WindowedWavDataset(args.samples_dir, window_config, files=files)
        indices = np.arange(len(dataset))
        if train_split >= 1.0:
            train_indices = indices
            val_indices = np.array([], dtype=int)
        else:
            train_indices, val_indices = train_test_split(
                indices,
                train_size=train_split,
                random_state=seed,
                shuffle=True,
            )
        train_ds = dataset
        val_ds = dataset if val_indices.size > 0 else None
        print(f"Files: {len(files)} (window-level split)")
        print(f"Train windows: {len(train_indices)}")
        if val_indices.size > 0:
            print(f"Val windows: {len(val_indices)}")
    elif split_mode == "files":
        if len(files) < 2:
            raise ValueError("Need at least 2 WAV files for train/val split")

        train_files, val_files = _split_files_with_coverage(
            files,
            train_split=train_split,
            seed=seed,
            strict_labels=not args.allow_heuristics,
        )

        train_ds = WindowedWavDataset(args.samples_dir, window_config, files=train_files)
        val_ds = WindowedWavDataset(args.samples_dir, window_config, files=val_files) if val_files else None

        print(f"Train files: {len(train_files)}  Val files: {len(val_files)}")
        print(f"Train windows: {len(train_ds)}")
        if val_ds is not None:
            print(f"Val windows: {len(val_ds)}")
    elif split_mode == "ranges":
        train_config = WindowConfig(
            sample_rate=target_sr,
            window_s=window_s,
            hop_s=hop_s,
            strict_labels=not args.allow_heuristics,
            split="train",
            split_config=split_cfg,
        )
        val_config = WindowConfig(
            sample_rate=target_sr,
            window_s=window_s,
            hop_s=hop_s,
            strict_labels=not args.allow_heuristics,
            split="val",
            split_config=split_cfg,
        )

        train_ds = WindowedWavDataset(args.samples_dir, train_config, files=files)
        val_ds = WindowedWavDataset(args.samples_dir, val_config, files=files)
        if len(val_ds) == 0:
            val_ds = None
        print("Split mode: ranges (per-file time splits)")
        print(f"Train windows: {len(train_ds)}")
        if val_ds is not None:
            print(f"Val windows: {len(val_ds)}")
    else:
        raise ValueError(f"Unknown split mode: {split_mode}")

    augmenter = None
    if augment_cfg.enabled:
        noise_pool = None
        if augment_cfg.p_noise > 0:
            noise_pool = build_noise_pool(
                args.samples_dir,
                split_config=split_cfg if split_mode == "ranges" else None,
                sample_rate=target_sr,
                strict_labels=not args.allow_heuristics,
            )
        augmenter = AudioAugmenter(
            augment_cfg,
            sample_rate=target_sr,
            noise_pool=noise_pool,
            seed=seed,
        )

    torch = _require_torch()
    beats_config = BeatsConfig(checkpoint_path=checkpoint_path, target_sr=target_sr, device=device)
    encoder = load_beats_encoder(beats_config)

    head_cfg = None
    head_cfg_raw = beats_cfg.get("head")
    if isinstance(head_cfg_raw, dict):
        cfg_kwargs = dict(head_cfg_raw)
        input_dim = int(cfg_kwargs.pop("input_dim", 0))
        head_cfg = TemporalHeadConfig(input_dim=input_dim, **cfg_kwargs)

    head = None
    optimizer = None
    loss_fn = torch.nn.BCEWithLogitsLoss()

    for epoch in range(args.epochs):
        if head is not None:
            head.train()
        losses = []
        for batch_audio, batch_labels in _iter_batches(train_ds, args.batch_size, train_indices):
            if augmenter is not None:
                batch_audio = augmenter(batch_audio)
            with torch.no_grad():
                tokens = encode_audio(encoder, batch_audio, sample_rate=target_sr)
                tokens = _ensure_btd(tokens, input_dim=head_cfg.input_dim if head_cfg else None)

            if head is None:
                inferred_dim = tokens.shape[-1]
                if head_cfg is None:
                    head_cfg = TemporalHeadConfig(input_dim=inferred_dim)
                elif head_cfg.input_dim != inferred_dim:
                    head_cfg = replace(head_cfg, input_dim=inferred_dim)
                head = build_temporal_head(head_cfg)
                head.to(device)
                optimizer = torch.optim.AdamW(head.parameters(), lr=args.lr)

            labels = torch.as_tensor(batch_labels, device=device, dtype=torch.float32)
            logits = head(tokens)
            loss = loss_fn(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            losses.append(float(loss.detach().cpu()))

        mean_loss = float(np.mean(losses)) if losses else float("nan")
        print(f"Epoch {epoch + 1}/{args.epochs} loss={mean_loss:.4f}")

    if head is None:
        raise RuntimeError("Head was never initialized; dataset may be empty.")

    save_head_checkpoint(head_out, head, head_cfg)
    print(f"Saved head checkpoint to {head_out}")

    if val_ds is None:
        return

    head.eval()
    y_true = []
    y_prob = []
    with torch.no_grad():
        for batch_audio, batch_labels in _iter_batches(val_ds, args.batch_size, val_indices):
            tokens = encode_audio(encoder, batch_audio, sample_rate=target_sr)
            tokens = _ensure_btd(tokens, input_dim=head_cfg.input_dim if head_cfg else None)
            logits = head(tokens)
            probs = torch.sigmoid(logits).cpu().numpy()
            y_prob.append(probs)
            y_true.append(batch_labels)

    if y_true and y_prob:
        y_true_arr = np.concatenate(y_true, axis=0)
        y_prob_arr = np.concatenate(y_prob, axis=0)
        _print_metrics("Val", y_true_arr, y_prob_arr)


if __name__ == "__main__":
    main()
