# TRAINING: What Must Be Done Before Inference

This project does **not** ship with a trained model. You must complete the steps below before using any of the batch/stream/live inference tools.

---

## Quickstart
Replace `/path/to/BEATs_iter3_plus_AS2M.pt` with your local checkpoint path:
```bash
uv sync
uv run python scripts/prepare_manifests.py
uv run python scripts/build_windows.py
uv run python src/train/train.py \
  --beats-checkpoint /path/to/BEATs_iter3_plus_AS2M.pt
uv run python src/train/thresholds.py \
  --beats-checkpoint /path/to/BEATs_iter3_plus_AS2M.pt \
  --model-state models/<run_id>/model.pt
```

---

## 1) Prerequisites
- **Python 3.12+**
- **uv** installed and available on PATH
- **BEATs checkpoint file**: `BEATs_iter3_plus_AS2M.pt`
  - You must provide the local path to this file when training and when running inference.

---

## 2) Install Dependencies
From the project root:
```bash
uv sync
```

---

## 3) Verify / Prepare Data
The system expects `.m4a` files in `./samples` named like:
```
ac-on-fridge-off-day.m4a
ac-on-fridge-on-night.m4a
ac-off-fridge-on-day.m4a
ac-off-fridge-off-night.m4a
```
These names are **parsed for labels**, so keep the pattern:
`ac-(on|off)-fridge-(on|off)-(day|night).m4a`

---

## 4) Build Manifests
Generate file‑level and window‑level manifests (required for training):
```bash
uv run python scripts/prepare_manifests.py
uv run python scripts/build_windows.py
```
Outputs:
- `data/manifests/files.csv`
- `data/manifests/windows.parquet`

---

## 5) Train the Model (Stage 1)
Train the classifier head with BEATs frozen:
```bash
uv run python src/train/train.py \
  --beats-checkpoint /path/to/BEATs_iter3_plus_AS2M.pt
```
This creates a run directory in `models/` containing:
- `model.pt` (full model state)
- `head.pt` (head‑only state)
- `best_metrics.json`

---

## 6) (Optional) Stage 2 Fine‑Tune
Unfreeze the last 1–2 BEATs blocks **only if** validation improves:
```bash
uv run python src/train/train.py \
  --beats-checkpoint /path/to/BEATs_iter3_plus_AS2M.pt \
  --unfreeze-blocks 1
```

---

## 7) Select Thresholds
Pick `t_ac` and `t_fr` on the validation set:
```bash
uv run python src/train/thresholds.py \
  --beats-checkpoint /path/to/BEATs_iter3_plus_AS2M.pt \
  --model-state models/<run_id>/model.pt
```
Output:
- `src/config/thresholds.yaml`

---

## 8) Assess Model Quality
Before deploying inference, review validation quality at the **file level** (median over windows):
- **F1 (ac)** and **F1 (fridge)** should be stable across day/night splits.
- **3‑state accuracy** should be high and aligned with the priority rule (`ac-on` overrides fridge).
- Prefer **consistent performance** over a single high score from one split.

Where to look:
- `models/<run_id>/best_metrics.json` (best epoch summary)
- `models/<run_id>/metrics.jsonl` (epoch‑by‑epoch history)

Recommended checks:
- **Cross‑split sanity:** run training twice with `--val-daypart day` and `--val-daypart night`, compare F1s.
- **Threshold sensitivity:** re‑run `thresholds.py` with a tighter grid if F1 is unstable.
- **Qualitative spot checks:** run `src/infer/batch.py` on a few known files and confirm the JSON output matches expected state.

If quality is poor:
- Re‑check labels in `data/manifests/files.csv` (filename parsing must be correct).
- Increase training epochs modestly.
- Try Stage‑2 unfreezing (`--unfreeze-blocks 1`) **only** if validation improves.

---

## 9) Ready for Inference
Once you have:
- `models/<run_id>/model.pt`
- `src/config/thresholds.yaml`

You can run:
- Batch inference: `src/infer/batch.py`
- Streaming simulation: `src/infer/stream.py`
- Live mic inference: `src/infer/live.py`

---

## Notes
- All scripts must be run with **`uv`**.
- File‑level split is required; random window splits are invalid.
- The live inference tools will **not** work until training and threshold selection are complete.
