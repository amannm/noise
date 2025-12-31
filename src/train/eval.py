from __future__ import annotations

from collections import defaultdict
from typing import Dict, Iterable, Tuple

import numpy as np
import torch


def derive_state(ac: int, fridge: int) -> str:
    if ac == 1:
        return "ac-on"
    if fridge == 1:
        return "fridge-on"
    return "both-off"


def f1_score(y_true: Iterable[int], y_pred: Iterable[int]) -> float:
    y_true = np.array(list(y_true))
    y_pred = np.array(list(y_pred))
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    if tp == 0:
        return 0.0
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def evaluate_model(
    model: torch.nn.Module,
    dataloader: torch.utils.data.DataLoader,
    device: str,
    t_ac: float,
    t_fr: float,
) -> Dict[str, float]:
    model.eval()
    preds: Dict[str, list[tuple[float, float]]] = defaultdict(list)
    labels: Dict[str, tuple[int, int]] = {}

    with torch.no_grad():
        for fbanks, lbls, meta in dataloader:
            fbanks = fbanks.to(device)
            logits = model(fbanks)
            probs = torch.sigmoid(logits).cpu().numpy()
            lbls = lbls.cpu().numpy()
            recording_ids = meta["recording_id"]

            for i, rec_id in enumerate(recording_ids):
                preds[str(rec_id)].append((float(probs[i][0]), float(probs[i][1])))
                labels[str(rec_id)] = (int(lbls[i][0]), int(lbls[i][1]))

    y_true_ac = []
    y_pred_ac = []
    y_true_fr = []
    y_pred_fr = []
    y_true_state = []
    y_pred_state = []

    for rec_id, rec_preds in preds.items():
        arr = np.array(rec_preds)
        med_ac = float(np.median(arr[:, 0]))
        med_fr = float(np.median(arr[:, 1]))
        true_ac, true_fr = labels[rec_id]

        pred_ac = 1 if med_ac >= t_ac else 0
        pred_fr = 1 if med_fr >= t_fr else 0

        y_true_ac.append(true_ac)
        y_pred_ac.append(pred_ac)
        y_true_fr.append(true_fr)
        y_pred_fr.append(pred_fr)

        y_true_state.append(derive_state(true_ac, true_fr))
        y_pred_state.append(derive_state(pred_ac, pred_fr))

    f1_ac = f1_score(y_true_ac, y_pred_ac)
    f1_fr = f1_score(y_true_fr, y_pred_fr)
    state_acc = float(np.mean(np.array(y_true_state) == np.array(y_pred_state)))

    return {
        "f1_ac": f1_ac,
        "f1_fridge": f1_fr,
        "state_acc": state_acc,
        "num_files": float(len(y_true_state)),
    }
