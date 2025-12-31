# PLAN: Apartment Noise State Classifier (AC / Fridge / Neither)

This plan translates `SPEC.md` into an implementable, end‑to‑end system: data prep → training → evaluation → batch + streaming + live inference. It assumes a fixed apartment/mic and uses BEATs preprocessing and encoder exactly as specified.

---

## 0) Guiding Principles (from SPEC)
- **Use BEATs_iter3_plus_AS2M.pt** + **BEATs reference preprocessing** (Kaldi fbank, 16 kHz, 128 bins, (x-mean)/(2*std)).
- **Multi‑label** outputs (`ac`, `fridge`), 3‑state derivation with priority rule.
- **File‑level validation only** (no random window split).
- **No fallback behaviors**; no legacy/backcompat.
- **All Python execution via `uv`.**

---

## 1) Repository Layout (current + planned)
```
./
  TRAINING.md
  PLAN.md
  SPEC.md
  samples/                # raw .m4a inputs
  reference/unilm/beats/  # BEATs reference code
  models/                 # trained heads + configs
  data/
    manifests/
      files.csv           # file-level metadata + labels
      windows.parquet      # window-level index (file, start, end, label)
    cache/                 # optional cached fbank or waveform
  src/
    config/
      thresholds.yaml
      live.toml            # live inference defaults
    datasets/
      window_dataset.py
      augment.py
    beats/
      preprocess.py        # wrapper around BEATs preprocessing
      model.py             # BEATs encoder wrapper + pooling + head
    train/
      train.py
      eval.py
      thresholds.py
    infer/
      batch.py
      stream.py
      hysteresis.py
      live.py
    utils/
      audio.py
  scripts/
    prepare_manifests.py
    build_windows.py
    list_devices.py
```

Notes:
- Use `models/` for trained heads + threshold configs.
- Use `data/manifests` for deterministic window indexing and splits.
- Keep BEATs wrapper minimal and faithful to reference code.

---

## 2) Data Inventory & Labeling
**Goal:** build authoritative file‑level manifest with labels and metadata.

### 2.1 Inspect samples
- List `./samples/*.m4a`, capture duration, sample rate, and filename.
- Decide label source:
  - If filenames encode state (preferred), parse into labels.
  - If not, define `src/config/labels.yaml` with explicit mapping.

### 2.2 File‑level manifest
Create `data/manifests/files.csv` with columns:
- `path` (relative)
- `duration_sec`
- `sample_rate`
- `ac` (0/1)
- `fridge` (0/1)
- `state` (`ac-on` / `fridge-on` / `both-off`)
- `daypart` or `split_group` (e.g., day/night)
- `recording_id` (unique file id)

**Acceptance:** every file labeled; no ambiguous state.

---

## 3) Windowing + Outlier Removal
**Goal:** build window index at file‑level with outlier pruning.

### 3.1 Window extraction
- Window length: **6.0 s**, hop: **1.5 s**.
- Compute windows on **resampled 16 kHz** mono signal.
- Keep window timestamps (start_sec, end_sec).

### 3.2 Outlier removal
- For each file, compute RMS per window.
- Drop top **1%** highest‑RMS windows (optionally extend to spectral flux in future).
- Save remaining windows to `data/manifests/windows.parquet` with:
  - `recording_id`, `path`, `start_sec`, `end_sec`, `ac`, `fridge`.

**Acceptance:** window count matches expectations; outliers removed only per file.

---

## 4) Feature Extraction (BEATs‑compliant)
**Goal:** strictly match BEATs preprocessing.

### 4.1 BEATs fbank wrapper
Implement `src/beats/preprocess.py` to:
- Resample to 16k; mono.
- Generate Kaldi fbank with **num_mel_bins=128**, **frame_length=25ms**, **frame_shift=10ms**.
- Normalize `(fbank - mean) / (2 * std)` using BEATs reference.

**Implementation:** import BEATs preprocessing from `reference/unilm/beats`, avoid re‑implementing logic. Wrap minimal API: `waveform -> fbank`.

### 4.2 Caching strategy (optional)
- Default: compute on‑the‑fly in dataset.
- If needed, add cache flag to persist fbank to `data/cache/` keyed by file+window.

---

## 5) Augmentation
**Goal:** match spec, on‑the‑fly only.

### 5.1 Waveform domain
- Random gain ±6 dB **always**.
- 50% mix with a random **both‑off** window, SNR uniform [8,25] dB.
- EQ tilt (30%): low‑shelf 150–300 Hz ±3 dB, high‑shelf 2–5 kHz ±3 dB.

### 5.2 Feature domain
- SpecAugment **always**:
  - Time masks: 2, up to ~0.4 s of frames each.
  - Freq masks: 2, up to 20 mel bins.

**Avoid:** heavy reverbs, large time‑stretch.

---

## 6) Model Architecture
**Goal:** BEATs encoder + attention pooling + small head.

### 6.1 Encoder
- Load `BEATs_iter3_plus_AS2M.pt`.
- Stage 1: frozen.
- Stage 2: unfreeze last 1–2 transformer blocks.

### 6.2 Pooling
Attention pooling over frame embeddings:
- `alpha_t = softmax(w^T h_t)`
- `pooled = sum(alpha_t * h_t)`

### 6.3 Head
- Dropout(0.2)
- Linear D→256
- GELU
- Dropout(0.2)
- Linear 256→2 (ac, fridge)

Loss: `BCEWithLogitsLoss` with `pos_weight` if imbalanced.

---

## 7) Training Pipeline
**Goal:** stage‑wise training with file‑level validation and deployment‑aligned metrics.

### 7.1 Splits (file‑level only)
- Use `daypart` or `recording_id` to split.
- Preferred: train on day files, validate on night (and swap in second run).
- Alternate: leave‑one‑recording‑out (LOO) if few files.

### 7.2 Stage 1 (required)
- Freeze BEATs; train head only.
- Optimizer: AdamW, lr=1e‑3, wd=1e‑2.
- Cosine decay with warmup ~200 steps.
- Early stop on file‑level metrics.

### 7.3 Stage 2 (optional)
- Unfreeze last 1–2 blocks.
- lrs: BEATs=2e‑5, head=3e‑4, wd=1e‑2.
- Early stop; skip if validation degrades.

### 7.4 Evaluation & logging
- Aggregate window predictions by file using **median**.
- Report F1 for `ac`, F1 for `fridge`, and 3‑state accuracy.
- Save logs to `models/<run_id>/metrics.jsonl`, `best_metrics.json`, and `train_config.json`.

---

## 8) Threshold Selection & Hysteresis
**Goal:** stable 3‑state output with priority rule.

### 8.1 Validation thresholding
- Choose `t_ac`, `t_fr` maximizing validation F1 (grid search on val set).
- Defaults: `t_ac=0.75`, `t_fr=0.70`.
- Save to `src/config/thresholds.yaml`.

### 8.2 Streaming hysteresis
- AC: `t_on=0.80`, `t_off=0.60`
- Fridge: `t_on=0.75`, `t_off=0.55`
- Priority: if AC on ⇒ `ac-on` regardless of fridge.
- Debounce: require K=2 consecutive updates.

---

## 9) Inference

### 9.1 Batch inference (`src/infer/batch.py`)
Pipeline:
1. Load file, resample to 16k mono.
2. Window (6s / 1.5s hop).
3. BEATs + head → window probabilities.
4. Aggregate with median per file.
5. Apply thresholds + priority rule.
6. Output JSON: `{"status": "ac-on"|"fridge-on"|"both-off"}`.

### 9.2 Streaming inference (`src/infer/stream.py`)
- Maintain rolling buffer of audio.
- Every hop, infer last window.
- Keep last N=7 window probabilities.
- Compute medians, apply hysteresis per label.
- Derive 3‑state output with debounce (K=2).

### 9.3 Live inference (`src/infer/live.py`)
- Live mic input with `sounddevice`.
- Device discovery via `--list-devices` / `--list-devices-json`.
- Optional JSONL logging (`--log-jsonl`) and dry‑run replay of files/dirs (`--dry-run`).
- `src/config/live.toml` provides defaults; CLI flags override.

---

## 10) Configuration & CLI
- Config files:
  - `src/config/thresholds.yaml` (validation thresholds)
  - `src/config/live.toml` (live inference defaults)
- CLI entrypoints are plain Python scripts (argparse):
  - `scripts/prepare_manifests.py`
  - `scripts/build_windows.py`
  - `scripts/list_devices.py`
  - `src/train/train.py`
  - `src/train/thresholds.py`
  - `src/infer/batch.py`
  - `src/infer/stream.py`
  - `src/infer/live.py`
- All scripts run via `uv` (see `TRAINING.md` for the canonical sequence).

---

## 11) Validation & Testing
**Lightweight but targeted:**
- Unit tests:
  - Window indexing correctness (count + boundaries).
  - Outlier removal drops correct fraction.
  - BEATs fbank shape + normalization range sanity.
  - Threshold + hysteresis logic.
- Integration test:
  - Train stage 1 for 1 epoch on small subset, run batch inference.
- Quality checks (file-level):
  - Cross‑split (day vs night) F1 stability.
  - Threshold sensitivity on validation grid.
  - Spot‑check JSON outputs on known files.

---

## 12) Milestones & Deliverables
1. **Data manifest + label mapping**
   - `data/manifests/files.csv` (filename parsing or optional label map).
2. **Window index + outlier removal**
   - `data/manifests/windows.parquet`.
3. **BEATs preprocessing wrapper + dataset**
   - `src/beats/preprocess.py`, `src/datasets/window_dataset.py`.
4. **Model + training pipeline**
   - `src/beats/model.py`, `src/train/train.py`, `src/train/eval.py`.
5. **Threshold selection + configs**
   - `src/train/thresholds.py`, `src/config/thresholds.yaml`.
6. **Batch + streaming + live inference**
   - `src/infer/batch.py`, `src/infer/stream.py`, `src/infer/live.py`.
7. **Ops helpers**
   - `scripts/list_devices.py`, `TRAINING.md`.
8. **Acceptance validation**
   - Metrics report + demo JSON outputs.

---

## 13) Acceptance Checklist (from SPEC)
- Training completes without data leakage.
- File‑level validation shows stable/high F1 for `ac` and `fridge`.
- Streaming inference produces stable state output (minimal flapping).
- CLI outputs JSON with exact status values.

---

## 14) Immediate Next Actions (for implementation)
1. Run the training sequence in `TRAINING.md`.
2. Review `best_metrics.json` and compare day/night splits.
3. Generate `thresholds.yaml`, then validate with batch inference.
4. Dry‑run live inference on `samples/` before using a mic.
