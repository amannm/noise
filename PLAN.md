# PLAN: Live Appliance On/Off Detection via Audio (BEATs-First)

## 0) Scope and Goals
- Detect **AC present** and **fridge present** in real time.
- Emit **clean on/off events** with minimal flapping.
- Optimize for tiny, weakly labeled steady-state audio and low-latency MacBook inference.
- Use **BEATs encoder → temporal head → probability smoothing → hysteresis**.

Non-goals (this iteration): full SED boundary training, multi-room localization, diarization.

---

## Status Key (as of December 31, 2025)
- DONE: implemented in repo and ready to use.
- PARTIAL: implemented but missing dependencies, integrations, or coverage.
- MISSING: not implemented yet.

## Current Implementation Snapshot
- Phase 0 — Repo Audit: DONE (core modules present); PARTIAL (external BEATs artifacts + runtime docs); MISSING (UI/dashboard, onnxruntime CoreML EP wiring).
- Phase 1 — Data + Labeling: DONE (windowing + labels + summary CLI); PARTIAL (hard dependency on filename conventions).
- Phase 2 — Feature + Model Stack: DONE (resample/log-mel, BEATs wrapper, CNN+GRU head); PARTIAL (alt heads, BEATs checkpoint + repo are external).
- Phase 3 — Training: DONE (baseline + BEATs head-only training + AUROC/AUPRC); PARTIAL (no partial fine-tune/LoRA, no calibration stats logging).
- Phase 4 — Calibration: DONE (percentile thresholds + merged config).
- Phase 5 — Realtime Inference: DONE (capture → buffer → model → smoothing → hysteresis → logging).
- Phase 6 — Offline Validation: PARTIAL (offline replay exists, no plots or report).
- Phase 7 — Deployment: PARTIAL (ONNX/CoreML export exists, no onnxruntime CoreML EP runtime).
- Phase 8 — Tests: PARTIAL (unit tests exist, no integration/CI gating).
- Phase 10 — Docs/Runbook: PARTIAL (scripts exist, no consolidated runbook/README).

---

## Priority Backlog (Suggested Order)
**P0 (Unblocks real use)**
- Add a concise runbook/README with exact `uv` commands for: dataset summary, train (baseline + BEATs), calibrate, offline check, realtime streaming.
- Add an end-to-end offline integration check that:
  - runs inference on each steady-state WAV
  - asserts zero events when `--require-no-events` is enabled
  - emits a short summary report

**P1 (Performance + portability)**
- Add onnxruntime CoreML EP runtime path (optional flag) and parity check vs PyTorch.
- Add a small parity script to compare PyTorch vs ONNX logits on a fixed window.

**P2 (Quality + robustness)**
- Log calibration stats (present/absent mean/std and overlap) to help tune thresholds.
- Add optional plots for probability distributions (saved to `artifacts/`).
- Add optional filename validation / allow a labels manifest to reduce reliance on naming conventions.

**P3 (Nice-to-have)**
- UI/dashboard for live probabilities + event timeline.
- Alternative temporal heads (Conformer-lite / Transformer).

---

## 1) Phase 0 — Repo Audit + Alignment to SPEC
Status (as of December 31, 2025):
- DONE: Core pipeline modules exist (`src/noise/audio/*`, `src/noise/inference/*`, `src/noise/model/*`, `src/noise/training/*`, `src/noise/config/defaults.yaml`).
- PARTIAL: BEATs runtime depends on external artifacts (`models/BEATs_iter3_plus_AS2M.pt`, BEATs repo on `PYTHONPATH`, `torch`).
- MISSING: UI/dashboard, onnxruntime CoreML EP runtime wiring, consolidated runbook.

**Deliverable:** a mapping of SPEC requirements to implemented modules and gaps.
- Verify existing module coverage:
  - Audio capture + ring buffer (`src/noise/audio/*`, `src/noise/inference/realtime.py`)
  - Resampling and log-mel (`src/noise/audio/resample.py`, `src/noise/audio/featurize.py`)
  - BEATs encoder wrapper + temporal head (`src/noise/model/beats.py`, `src/noise/model/head.py`)
  - Presence inference pipeline + smoothing + hysteresis (`src/noise/inference/*`)
  - Training + calibration scripts (`src/noise/training/*`, `scripts/*`)
  - Defaults/config (`src/noise/config/defaults.yaml`)
- List missing pieces (if any):
  - BEATs checkpoint availability and expected location.
  - Optional ONNX/CoreML export readiness and dependencies.
  - CLI documentation and example configs.
  - UI/dashboard (optional).
- Output: short checklist of completed vs missing, then proceed to fill gaps below.

---

## 2) Phase 1 — Data + Labeling Pipeline (Steady-State)
**Goal:** reliably window steady-state WAVs into labeled training/eval examples.

Status (as of December 31, 2025):
- DONE: Windowed dataset + label map + resampling (`src/noise/training/dataset.py`).
- DONE: Dataset summary CLI (`src/noise/training/dataset.py`, `scripts/run_dataset_summary.sh`).
- PARTIAL: Strong reliance on filename conventions (heuristics are optional but not validated).

### 2.1 Data conventions
- Confirm `./samples` has four steady-state WAVs: `all_off`, `ac_on`, `fridge_on`, `all_on`.
- Maintain label map:
  - `none` → (0,0)
  - `ac` → (1,0)
  - `fridge` → (0,1)
  - `both` → (1,1)

### 2.2 Windowing configuration
- Use inference-consistent windowing:
  - Default window = 4.0 s, hop = 0.5 s.
  - Iter3+ window = 2.0 s, hop = 0.5 s (optional later).
- Ensure resampling to 16 kHz before windowing.
- Use cached audio per file to keep training fast.

### 2.3 Dataset summary utility
- Provide a script or command to list:
  - per-file duration, sample rate, label, #windows
  - total windows, label balance

**Deliverable:** repeatable dataset summary (for sanity and reproducibility).

---

## 3) Phase 2 — Feature + Model Stack (BEATs-First)
**Goal:** BEATs-compatible preprocessing and a temporal head for multi-label presence.

Status (as of December 31, 2025):
- DONE: Resampling + log-mel (`src/noise/audio/resample.py`, `src/noise/audio/featurize.py`).
- DONE: BEATs wrapper + token extraction (`src/noise/model/beats.py`).
- DONE: CNN + (Bi)GRU temporal head (`src/noise/model/head.py`).
- PARTIAL: Alternative heads (Conformer/Transformer) not implemented.
- PARTIAL: BEATs checkpoint + repo are external dependencies.

### 3.1 Preprocessing (BEATs-compatible)
- Resample 44.1 kHz → 16 kHz (bandlimited).
- Compute log-mel:
  - 128 mel bins
  - 25 ms window / 10 ms hop

### 3.2 BEATs encoder integration
- Load pretrained BEATs checkpoint locally.
- Keep encoder frozen initially for stability and speed.
- Use **time-resolved tokens** (not global pooling).

### 3.3 Temporal head (multi-label)
- Select and implement one head:
  - 1D CNN + (Bi)GRU (default)
  - Conformer-lite (optional)
  - Transformer encoder + attentive pooling (optional)
- Output two logits: `[p_ac, p_fridge]`.
- Loss: BCE with logits (multi-label).

**Deliverable:** model bundle that can produce `p_ac`, `p_fridge` for any window.

---

## 4) Phase 3 — Training Pipeline (Presence Detection)
**Goal:** train on weak labels from steady-state audio.

Status (as of December 31, 2025):
- DONE: Baseline trainer (`src/noise/training/train.py`).
- DONE: BEATs head-only trainer + metrics (`src/noise/training/train_beats.py`).
- PARTIAL: No partial fine-tune/LoRA path implemented.
- PARTIAL: No calibration-stat logging (present vs absent means/vars).

### 4.1 Training flow
- Use same window/hop as inference.
- Each window inherits file-level labels.
- Head-only training first (linear probe).
- Optional: partial fine-tuning or LoRA after baseline works.

### 4.2 Evaluation
- Use AUROC and AUPRC per class on held-out windows.
- Print calibration-friendly stats: mean/std of probabilities for present vs absent.
- Record training metadata (config, checkpoint path, git hash if desired).

### 4.3 Outputs
- Save head checkpoint with embedded head config.
- Keep baseline classifier (log-mel + logistic) for sanity checks.

**Deliverable:** trained head checkpoint with metrics and reproducible config.

---

## 5) Phase 4 — Calibration from Steady-State WAVs
**Goal:** pick `T_on` and `T_off` thresholds that match the audio domain.

Status (as of December 31, 2025):
- DONE: Calibration script with percentiles + min-gap, plus merged config output (`src/noise/training/calibrate.py`).

### 5.1 Procedure
- Run model over all steady-state files.
- For each device:
  - `P_absent`: probs when device is OFF
  - `P_present`: probs when device is ON
- Set:
  - `T_off = percentile(P_absent, 95–97)`
  - `T_on  = percentile(P_present, 10–15)`
- Enforce `T_on >= T_off + 0.10`
- If distributions overlap, increase smoothing/window length or widen thresholds.

### 5.2 Output
- Generate a calibrated config file (YAML) that overrides hysteresis thresholds.

**Deliverable:** `calibrated.yaml` (or similar) checked into artifacts.

---

## 6) Phase 5 — Real-Time Inference Pipeline
**Goal:** low-latency streaming detection and stable on/off events.

Status (as of December 31, 2025):
- DONE: Realtime streaming loop + ring buffer + resample (`src/noise/inference/realtime.py`, `src/noise/audio/*`).
- DONE: Smoothing + hysteresis (`src/noise/inference/smoother.py`, `src/noise/inference/hysteresis.py`).
- DONE: Probability/event CSV logging (`src/noise/utils/logging.py`).

### 6.1 Audio ingestion
- Capture mono input via CoreAudio / sounddevice.
- Chunk size = 1.0 s (default).
- Resample to 16 kHz.

### 6.2 Ring buffer + windowing
- Ring buffer = 6.0 s.
- Inference window = 4.0 s (2.0 s optional iter3+).
- Hop = 0.5 s.

### 6.3 Probability smoothing
- Median filter across last N hops:
  - N=9 default (4.5 s).
  - N=7 for 2s window.
- EMA with tau:
  - tau=6 s default (alpha ≈ 0.92 for 0.5 s hop).
  - tau=4 s optional faster response.

### 6.4 Hysteresis state machine
Per device:
- `T_on > T_off`
- Require on/off persistence durations (N_on_s, N_off_s).
- Cooldown between transitions.
- Default robust config:
  - AC: `T_on=0.75`, `T_off=0.35`, `N_on=4s`, `N_off=8s`, `cooldown=20s`
  - Fridge: `T_on=0.65`, `T_off=0.30`, `N_on=6s`, `N_off=12s`, `cooldown=20s`

### 6.5 Outputs + logging
- Emit events with timestamps: `device`, `kind`, `prob`, `step`.
- Persist probability stream and smoothed stream (CSV) for debugging.

**Deliverable:** CLI entry that streams audio and prints/logs stable events.

---

## 7) Phase 6 — Offline Validation and Iteration Loop
**Goal:** ensure stability before live testing.

Status (as of December 31, 2025):
- PARTIAL: Offline replay + event checks exist (`src/noise/inference/offline.py`).
- MISSING: Probability distribution plots or automated validation report.

### 7.1 Offline replay
- Run the inference pipeline on steady-state WAVs and verify:
  - No spurious on/off transitions.
  - Probability separation between present vs absent.
- Plot or log probability distributions for each device.

### 7.2 Live smoke test
- Turn AC/fridge on/off and verify:
  - Detection latency within 2–10 seconds.
  - No flapping once stable.

**Deliverable:** a short validation report (metrics + observed latency).

---

## 8) Phase 7 — Deployment and Optimization
**Goal:** reduce latency/CPU and enable portable runtime.

Status (as of December 31, 2025):
- PARTIAL: ONNX export for head/full model (`src/noise/model/export_onnx.py`).
- PARTIAL: CoreML export for head/ONNX (`src/noise/model/export_coreml.py`).
- MISSING: onnxruntime CoreML EP runtime path + parity validation script.

### 8.1 ONNX export
- Export the temporal head + BEATs encoder to ONNX.
- Validate parity vs PyTorch outputs on a small audio batch.

### 8.2 CoreML acceleration (optional)
- Run ONNX with onnxruntime + CoreML EP on macOS.
- Optionally convert to CoreML for native deployment.

**Deliverable:** ONNX artifact and a runtime option switch.

---

## 9) Phase 8 — Testing and Quality Gates
**Goal:** keep behavior stable and prevent regressions.

Status (as of December 31, 2025):
- PARTIAL: Unit tests exist for resample/featurize/dataset/buffer/smoothing/hysteresis (`tests/*`).
- MISSING: Integration tests for end-to-end offline inference and calibration output.

### 9.1 Unit tests
- Hysteresis logic (thresholds, persistence, cooldown).
- Median + EMA smoothing behavior.
- Ring buffer behavior.
- Resampling and log-mel feature shape correctness.

### 9.2 Integration checks
- End-to-end inference on a known WAV (offline).
- Calibration script output structure and thresholds in config.

**Deliverable:** passing test suite (`uv run pytest`) and minimal integration checks.

---

## 10) Documentation and Runbook
**Goal:** make the system easy to operate and iterate.

Status (as of December 31, 2025):
- PARTIAL: Helper scripts exist (`scripts/*`) but no consolidated README/runbook.

- Quickstart steps:
  1. Place steady-state WAVs in `./samples`.
  2. Train head (head-only).
  3. Calibrate thresholds.
  4. Run realtime inference with calibrated config.
- Include typical commands and expected outputs.

---

## 11) Risks + Mitigations
- **Tiny dataset → overfitting.**
  - Mitigate with frozen encoder + conservative head capacity.
- **Threshold overlap.**
  - Use stronger smoothing or longer windows; widen thresholds.
- **CPU usage spikes.**
  - Reduce window size, increase hop, or use ONNX/CoreML.
- **Background noise drift.**
  - Recalibrate thresholds from new steady-state samples.

---

## 12) Acceptance Criteria (from SPEC)
- Stable, non-flapping AC/fridge on/off events.
- 2–10 second response time (configurable).
- Real-time performance on MacBook without sustained CPU spikes.
- Calibration works using only steady-state WAVs.
