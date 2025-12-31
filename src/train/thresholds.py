from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import torch

from src.beats.model import NoiseClassifier, load_beats_checkpoint
from src.datasets.window_dataset import WindowDataset
from src.train.eval import f1_score
from src.train.train import filter_windows, split_by_daypart


def collect_medians(
    model: torch.nn.Module,
    dataloader: torch.utils.data.DataLoader,
    device: str,
) -> tuple[list[float], list[float], list[int], list[int]]:
    model.eval()
    preds: Dict[str, list[tuple[float, float]]] = {}
    labels: Dict[str, tuple[int, int]] = {}

    with torch.no_grad():
        for fbanks, lbls, meta in dataloader:
            fbanks = fbanks.to(device)
            logits = model(fbanks)
            probs = torch.sigmoid(logits).cpu().numpy()
            lbls = lbls.cpu().numpy()
            recording_ids = meta["recording_id"]

            for i, rec_id in enumerate(recording_ids):
                rec_id = str(rec_id)
                preds.setdefault(rec_id, []).append(
                    (float(probs[i][0]), float(probs[i][1]))
                )
                labels[rec_id] = (int(lbls[i][0]), int(lbls[i][1]))

    med_ac = []
    med_fr = []
    true_ac = []
    true_fr = []
    for rec_id, rec_preds in preds.items():
        arr = np.array(rec_preds)
        med_ac.append(float(np.median(arr[:, 0])))
        med_fr.append(float(np.median(arr[:, 1])))
        t_ac, t_fr = labels[rec_id]
        true_ac.append(t_ac)
        true_fr.append(t_fr)
    return med_ac, med_fr, true_ac, true_fr


def find_best_threshold(scores: list[float], labels: list[int], grid: list[float]) -> tuple[float, float]:
    best_t = grid[0]
    best_f1 = -1.0
    for t in grid:
        preds = [1 if s >= t else 0 for s in scores]
        f1 = f1_score(labels, preds)
        if f1 > best_f1:
            best_f1 = f1
            best_t = t
    return best_t, best_f1


def main() -> None:
    parser = argparse.ArgumentParser(description="Select validation thresholds.")
    parser.add_argument("--beats-checkpoint", type=Path, required=True)
    parser.add_argument("--model-state", type=Path, required=True)
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
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    parser.add_argument("--grid-min", type=float, default=0.5)
    parser.add_argument("--grid-max", type=float, default=0.95)
    parser.add_argument("--grid-step", type=float, default=0.05)
    parser.add_argument("--output", type=Path, default=Path("src/config/thresholds.yaml"))
    args = parser.parse_args()

    windows_df = pd.read_parquet(args.windows_manifest)
    train_ids, val_ids = split_by_daypart(args.files_manifest, args.val_daypart)
    val_df = filter_windows(windows_df, val_ids)

    val_ds = WindowDataset(val_df, augment=False, return_meta=True)
    val_loader = torch.utils.data.DataLoader(
        val_ds, batch_size=16, shuffle=False, num_workers=0
    )

    beats = load_beats_checkpoint(args.beats_checkpoint)
    model = NoiseClassifier(beats)
    state_dict = torch.load(args.model_state, map_location="cpu")
    model.load_state_dict(state_dict)
    model.to(args.device)

    grid = list(np.arange(args.grid_min, args.grid_max + 1e-6, args.grid_step))
    med_ac, med_fr, true_ac, true_fr = collect_medians(
        model, val_loader, args.device
    )

    t_ac, f1_ac = find_best_threshold(med_ac, true_ac, grid)
    t_fr, f1_fr = find_best_threshold(med_fr, true_fr, grid)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    content = (
        f"t_ac: {float(t_ac):.4f}\\n"
        f"t_fr: {float(t_fr):.4f}\\n"
        f"f1_ac: {float(f1_ac):.4f}\\n"
        f"f1_fridge: {float(f1_fr):.4f}\\n"
    )
    args.output.write_text(content)


if __name__ == "__main__":
    main()
