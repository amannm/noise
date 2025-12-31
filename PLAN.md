# PLAN: Live Appliance On/Off Detection via Audio

This plan operationalizes `SPEC.md` into a buildable system. It is organized by workstreams and iterations, with concrete deliverables, validation steps, and decision points.

---

## 0) Guiding Principles
- **Presence-first:** train on steady-state windows, derive **events** via smoothing + hysteresis.
- **Low latency, high stability:** prefer conservative defaults (reduce flapping) and only tighten if stable.
- **BEATs-first:** reuse pretrained features; only unfreeze later if needed.
- **Config-driven:** all thresholds and timing parameters live in config for fast iteration.
- **Observable:** always log probabilities and events for diagnosis.

---

## Progress Update (Dec 31, 2025)
- **Baseline pipeline complete:** windowing + log-mel + logistic baseline, offline eval, smoothing/hysteresis, and live loop are implemented.
- **Calibration shipped:** steady-state threshold calibration produces config overrides.
- **Remaining for BEATs-first:** BEATs encoder + temporal head integration and optional ONNX/CoreML acceleration.

---

## 1) Project Structure (Current + Planned)
```
noise/
  PLAN.md
  SPEC.md
  THEORY.md
  samples/
  src/
    noise/
      audio/
        capture.py            # live mic ingest (planned; realtime loop uses sounddevice directly)
        resample.py           # 44.1k -> 16k
        buffer.py             # ring buffer
        featurize.py          # log-mel frontend
      model/
        baseline.py           # log-mel + logistic regression bundle (current)
        beats.py              # BEATs wrapper (planned)
        head.py               # temporal head (planned)
        pipeline.py           # end-to-end forward (planned)
      inference/
        smoother.py           # median + EMA
        hysteresis.py         # state machine
        offline.py            # offline steady-state checks
        realtime.py           # live loop
      training/
        dataset.py            # windowing + labels
        train.py              # training loop
        eval.py               # offline metrics
        calibrate.py          # threshold calibration
      config/
        defaults.yaml         # all params
        loader.py             # config helpers
      utils/
        logging.py            # event/prob logging
        time.py               # timestamp helpers
  scripts/
    run_train.sh
    run_eval.sh
    run_calibrate.sh
    run_dataset_summary.sh
    run_realtime.sh
  tests/
    test_hysteresis.py
    test_smoothing.py
    test_resample.py
    test_featurize.py
    test_dataset.py
    test_ring_buffer.py
```
Notes:
- Use `uv` for all script entrypoints.
- Keep BEATs model weights in a `models/` or cache dir (gitignored).

---

## 2) Iteration Plan (High-Level)

### Iteration 1: Baseline presence model + offline sanity checks (DONE)
Goal: produce stable probability streams per device from steady-state WAVs.

### Iteration 2: Event detection (smoothing + hysteresis) (DONE)
Goal: clean on/off events on steady-state files (no false transitions).

### Iteration 3: Live inference loop (DONE)
Goal: real-time probabilities + events from microphone input.

### Iteration 4: Calibration + tuning (DONE)
Goal: auto-thresholds from steady-state clips; reduced manual tuning.

### Iteration 5: BEATs integration + optimization (NEXT)
Goal: BEATs encoder + temporal head, optional ONNX/CoreML acceleration, stable CPU usage.

---

## 3) Workstreams and Detailed Steps

### A) Data + Windowing
1. **Inventory data**: confirm all states exist (`none`, `ac`, `fridge`, `both`) and sample rates.
2. **Windowing strategy**:
   - Inference-consistent windows (default 4.0s, hop 0.5s).
   - Each window inherits file-level labels.
3. **Dataset module**:
   - Read WAV; resample to 16k.
   - Slice into windows + hops.
   - Return `(log_mel, labels)` for training.
4. **Train/val split**:
   - Split by file (not by window) to prevent leakage.

Deliverables:
- `training/dataset.py` with deterministic windowing.
- A small CLI to print counts per class and verify label coverage.


### B) Audio Frontend (BEATs-compatible)
1. **Resampling**: high-quality bandlimited resampler to 16k.
2. **Log-mel**: 128 bins, 25ms window, 10ms hop.
3. **Feature shape sanity**: match BEATs expected input shape for tokenization.

Deliverables:
- `audio/resample.py`, `audio/featurize.py` with unit tests for shapes.


### C) Model: BEATs + Temporal Head
1. **BEATs wrapper**:
   - Load pretrained BEATs weights.
   - Produce **time token embeddings** per window.
2. **Head v1 (simple, fast)**:
   - Option: 1D CNN + BiGRU + linear.
   - Output: `p_ac`, `p_fridge` (sigmoid).
3. **Training strategy**:
   - Phase 1: freeze BEATs, train head only.
   - Phase 2: unfreeze last N BEATs blocks if needed.
4. **Loss**: multi-label BCE-with-logits.

Deliverables:
- `model/beats.py`, `model/head.py`, `training/train.py`.
- Config to select head type.


### D) Offline Evaluation
1. **Metrics**:
   - AUROC / AUPRC per class.
   - Probability histograms for present/absent.
2. **Calibration check**:
   - Assess separation of `P_present` vs `P_absent`.

Deliverables:
- `training/eval.py` outputs metrics + plots.


### E) Smoothing + Hysteresis
1. **Smoothing**:
   - Median filter over last N hops (default 9).
   - EMA with `tau=6s` (alpha derived from hop).
2. **Hysteresis machine**:
   - Per-device `T_on`, `T_off`, `N_on_s`, `N_off_s`, `cooldown_s`.
   - Internal counters based on hop timing.
3. **Unit tests**:
   - Verify transitions, cooldown enforcement, and no flapping.

Deliverables:
- `inference/smoother.py`, `inference/hysteresis.py` + tests.


### F) Live Inference Pipeline
1. **Audio capture**:
   - 1s chunks via CoreAudio / `sounddevice`.
2. **Ring buffer**:
   - Keep 6s of audio; slide inference window.
3. **Inference loop**:
   - Every hop (0.5s): window -> log-mel -> BEATs -> head.
   - Smooth -> hysteresis -> emit events.
4. **Logging**:
   - Persist probabilities per hop.
   - Event log with timestamps + state transitions.

Deliverables:
- `inference/realtime.py` with CLI options (device index, window/hop).


### G) Auto-Calibration from Steady-State Clips
1. **Probability collection**:
   - Run model over steady-state files.
   - Separate `P_present` / `P_absent` distributions.
2. **Threshold selection**:
   - `T_off = percentile(P_absent, 95-97)`.
   - `T_on = percentile(P_present, 10-15)`.
   - Enforce `T_on >= T_off + 0.10`.
3. **Persist calibration**:
   - Save calibrated thresholds in `defaults.yaml` or a derived config.

Deliverables:
- `training/calibrate.py` (or `inference/calibrate.py`).


### H) Optimization + Deployment
1. **ONNX export** for head + BEATs (if feasible).
2. **onnxruntime** with CoreML EP (Apple accel).
3. **Benchmark** CPU usage and latency.

Deliverables:
- `model/export_onnx.py` + benchmark script.

---

## 4) Configuration Plan
All defaults in a single YAML file, with overrides via CLI args.

Key groups:
- **Audio**: sample_rate, mel_bins, win_ms, hop_ms.
- **Inference**: chunk_s, window_s, hop_s, ring_buffer_s.
- **Smoothing**: median_N, ema_tau_s.
- **Hysteresis**: device-specific thresholds and timing.
- **Model**: BEATs checkpoint path, head type, freeze level.

Deliverable:
- `config/defaults.yaml` + a small loader utility.

---

## 5) Validation Strategy

### Offline (steady-state)
- **No false transitions** on any steady-state file.
- Strong separation in probability histograms.

### Live (manual toggles)
- **AC on/off** detected within 2–10s depending on params.
- **Fridge cycle** detected with minimal flapping.

### Regression checks
- Keep a fixed subset of WAVs for sanity tests.
- Store calibration thresholds and compare across model versions.

---

## 6) Risk Areas + Mitigations
- **Overlapping distributions** (present vs absent):
  - Increase smoothing window or extend inference window.
  - Adjust thresholds outward.
- **Latency too high**:
  - Switch to 2s window + 0.5s hop; adjust hysteresis times.
- **CPU spikes**:
  - Freeze BEATs; use ONNX/CoreML.
- **Cross-talk between AC and fridge**:
  - Consider optional combined-state Viterbi smoothing.

---

## 7) Milestones & Deliverables
1. **M1: Offline baseline** (DONE)
   - Training + evaluation from steady-state clips.
2. **M2: Event logic** (DONE)
   - Smoothing + hysteresis tests, no false transitions offline.
3. **M3: Live loop** (DONE)
   - Real-time stream + logs.
4. **M4: Calibration** (DONE)
   - Auto thresholds persisted.
5. **M5: Optimization** (PENDING)
   - ONNX/CoreML inference; latency benchmarked.

---

## 8) Acceptance Criteria (Mapped)
- Stable, non-flapping events: validated in M2 + M3.
- Response within 2–10s: verified in live tests.
- Real-time MacBook performance: benchmarked in M5.
- Calibration using steady-state clips only: delivered in M4.

---

## 9) Immediate Next Actions
1. Add BEATs encoder wrapper + temporal head (keep baseline path as fallback).
2. Add BEATs training loop (freeze encoder, train head).
3. Add BEATs eval + calibration parity with baseline scripts.
4. Benchmark latency; consider ONNX/CoreML export.
