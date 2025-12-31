from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.beats.model import NoiseClassifier, load_beats_checkpoint
from src.datasets.window_dataset import WindowDataset
from src.train.eval import evaluate_model


def split_by_daypart(
    files_manifest: Path, val_daypart: str
) -> tuple[list[str], list[str]]:
    files_df = pd.read_csv(files_manifest)
    if "daypart" not in files_df.columns:
        raise ValueError("files.csv must include daypart column")
    train_ids = files_df[files_df.daypart != val_daypart].recording_id.tolist()
    val_ids = files_df[files_df.daypart == val_daypart].recording_id.tolist()
    if not train_ids or not val_ids:
        raise ValueError("Train/val split is empty; check daypart labels")
    return train_ids, val_ids


def filter_windows(
    windows_df: pd.DataFrame, recording_ids: list[str]
) -> pd.DataFrame:
    return windows_df[windows_df.recording_id.isin(recording_ids)].reset_index(
        drop=True
    )


def compute_pos_weight_from_df(df: pd.DataFrame) -> torch.Tensor:
    pos = torch.tensor([df["ac"].sum(), df["fridge"].sum()], dtype=torch.float32)
    total = torch.tensor([len(df), len(df)], dtype=torch.float32)
    neg = total - pos
    pos_weight = torch.where(pos > 0, neg / pos, torch.ones_like(pos))
    return pos_weight


def main() -> None:
    parser = argparse.ArgumentParser(description="Train noise classifier head.")
    parser.add_argument("--beats-checkpoint", type=Path, required=True)
    parser.add_argument(
        "--windows-manifest",
        type=Path,
        default=Path("data/manifests/windows.parquet"),
    )
    parser.add_argument(
        "--files-manifest",
        type=Path,
        default=Path("data/manifests/files.csv"),
    )
    parser.add_argument("--val-daypart", type=str, default="night")
    parser.add_argument("--epochs", type=int, default=12)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--lr-head", type=float, default=1e-3)
    parser.add_argument("--lr-beats", type=float, default=2e-5)
    parser.add_argument("--weight-decay", type=float, default=1e-2)
    parser.add_argument("--warmup-steps", type=int, default=200)
    parser.add_argument("--unfreeze-blocks", type=int, default=0)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    windows_df = pd.read_parquet(args.windows_manifest)
    train_ids, val_ids = split_by_daypart(args.files_manifest, args.val_daypart)
    train_df = filter_windows(windows_df, train_ids)
    val_df = filter_windows(windows_df, val_ids)

    train_ds = WindowDataset(train_df, augment=True, seed=args.seed)
    val_ds = WindowDataset(val_df, augment=False, return_meta=True)

    train_loader = DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True, num_workers=0
    )
    val_loader = DataLoader(
        val_ds, batch_size=args.batch_size, shuffle=False, num_workers=0
    )

    beats = load_beats_checkpoint(args.beats_checkpoint)
    model = NoiseClassifier(beats)

    if args.unfreeze_blocks > 0:
        model.unfreeze_last_blocks(args.unfreeze_blocks)
    else:
        model.freeze_beats()

    model.to(args.device)

    # Compute pos_weight from train labels
    pos_weight = compute_pos_weight_from_df(train_df).to(args.device)
    criterion = torch.nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    # Optimizer with separate lrs if unfreezing
    params: List[Dict[str, object]] = []
    head_params = [p for p in model.head.parameters() if p.requires_grad]
    params.append({"params": head_params, "lr": args.lr_head})
    if args.unfreeze_blocks > 0:
        beats_params = [p for p in model.beats.parameters() if p.requires_grad]
        params.append({"params": beats_params, "lr": args.lr_beats})

    optimizer = torch.optim.AdamW(params, weight_decay=args.weight_decay)

    total_steps = args.epochs * max(1, len(train_loader))
    warmup_steps = min(args.warmup_steps, total_steps)

    def lr_lambda(step: int) -> float:
        if step < warmup_steps:
            return step / max(1, warmup_steps)
        progress = (step - warmup_steps) / max(1, total_steps - warmup_steps)
        return 0.5 * (1.0 + np.cos(np.pi * progress))

    scheduler = torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)

    if args.output_dir is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output_dir = Path("models") / f"run_{timestamp}"
    args.output_dir.mkdir(parents=True, exist_ok=True)

    best_f1 = -1.0
    best_state = None
    best_head = None

    step = 0
    for epoch in range(1, args.epochs + 1):
        model.train()
        if args.unfreeze_blocks == 0:
            model.beats.eval()
        running_loss = 0.0

        for fbanks, labels in train_loader:
            fbanks = fbanks.to(args.device)
            labels = labels.to(args.device)

            optimizer.zero_grad()
            logits = model(fbanks)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            scheduler.step()

            running_loss += loss.item()
            step += 1

        avg_loss = running_loss / max(1, len(train_loader))

        metrics = evaluate_model(
            model, val_loader, device=args.device, t_ac=0.75, t_fr=0.70
        )
        metrics["train_loss"] = avg_loss
        metrics["epoch"] = epoch

        # Simple early-stop criterion: mean F1
        mean_f1 = 0.5 * (metrics["f1_ac"] + metrics["f1_fridge"])
        if mean_f1 > best_f1:
            best_f1 = mean_f1
            best_state = {
                "model": copy.deepcopy(model.state_dict()),
                "metrics": metrics,
            }
            best_head = copy.deepcopy(model.head.state_dict())

        with (args.output_dir / "metrics.jsonl").open("a") as f:
            f.write(json.dumps(metrics) + "\n")

    if best_state is not None:
        torch.save(best_state["model"], args.output_dir / "model.pt")
        if best_head is not None:
            torch.save(best_head, args.output_dir / "head.pt")
        with (args.output_dir / "best_metrics.json").open("w") as f:
            json.dump(best_state["metrics"], f, indent=2)

    config = vars(args).copy()
    for key, value in config.items():
        if isinstance(value, Path):
            config[key] = str(value)
    with (args.output_dir / "train_config.json").open("w") as f:
        json.dump(config, f, indent=2)


if __name__ == "__main__":
    main()
