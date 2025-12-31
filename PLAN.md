# PLAN: Live Appliance On/Off Detection (BEATs-first)

This plan is aligned to `THEORY.md` and `SPEC.md`, and is focused on completing a robust, real-time AC/fridge on/off detector using a BEATs encoder + temporal head + hysteresis state machine. It assumes the current repo state (baseline model + BEATs head training/inference + smoothing/hysteresis + offline/realtime scripts) and lists the remaining work to harden, verify, and ship the full system.

## Goals (from SPEC)
- Detect AC and fridge on/off events with stable, non-flapping behavior.
- Real-time inference on a MacBook (low latency, no sustained CPU spikes).
- Works with tiny, weakly labeled steady-state clips.
- Calibration from steady-state clips produces usable hysteresis thresholds.

## Current State (Observed)
- Data pipeline: windowed dataset from steady-state `.wav` files in `samples/`.
- Baseline model: log-mel summary + logistic regression; training/eval scripts exist.
- BEATs path: encoder loader + temporal head + head-only training + inference bundle.
- Smoothing + hysteresis state machine implemented and tested.
- Offline inference + calibration scripts implemented.
- Realtime capture + ring buffer + inference + logging implemented.
- Export utilities: ONNX/CoreML for head or full model.

## Key Gaps / Decisions to Resolve
1. **BEATs input frontend**
   - Verify whether the BEATs model in use expects raw waveform or log-mel/fbank inputs.
   - If it expects fbank/log-mel, update `noise.model.beats.encode_audio()` to compute the correct frontend (and keep it consistent with training/inference).
   - If it expects waveform, document that the BEATs module includes its own frontend and keep current behavior.

2. **Performance constraints**
   - Confirm the chosen BEATs variant runs in real time at the desired hop/window on the target MacBook.
   - If too slow, decide between: smaller model, shorter window, ONNX/CoreML runtime, or CPU/GPU device settings.

3. **Default runtime profile**
   - Choose between the 4s window (robust) vs 2s iter3+ profile for production default.
   - Ensure the config reflects that choice and matches trained head expectations.

4. **Threshold calibration stability**
   - Confirm calibrated thresholds have a clear gap between present vs absent distributions.
   - Decide if extra smoothing or longer window is required for fridge stability.

5. **Deployment target**
   - Decide whether to ship PyTorch runtime only or include ONNX/CoreML acceleration as a required step.

---

## Implementation Plan (Phased)

### Phase 0 — Environment & Dependencies (1 session)
**Goal:** Ensure a repeatable environment and available dependencies.
- Confirm `uv` is the only tool used to run Python (per project rules).
- Validate required Python deps are installed from `pyproject.toml`.
- Decide how to provide BEATs:
  - Option A: install the official BEATs repo on `PYTHONPATH`.
  - Option B: vendor it locally and add it to package path.
- Install optional deps only if needed:
  - `torch` (required for BEATs training/inference).
  - `onnx`, `onnxruntime` (export + runtime).
  - `coremltools` (Core ML conversion).

**Deliverable:** A working environment that can run training/inference commands via `uv`.

---

### Phase 1 — Data & Labeling Sanity (1 session)
**Goal:** Confirm steady-state clips map cleanly to labels and windowing is correct.
- Run dataset summary using `noise.training.dataset` (or `scripts/run_dataset_summary.sh`).
- Confirm label mapping in `noise.training.dataset.LABEL_MAP` matches the file names.
- Validate window/hop parameters in `src/noise/config/defaults.yaml` produce enough windows per file.
- If new clips are added, update label map or enable heuristics as needed.

**Deliverable:** Verified dataset windowing + labels with no missing/incorrect labels.

---

### Phase 2 — Baseline Model (Fast Sanity) (0.5–1 session)
**Goal:** Establish a working baseline as a sanity check.
- Train baseline via `noise.training.train` (or `scripts/run_train.sh`).
- Evaluate with `noise.training.eval` to confirm presence separation.
- Archive baseline metrics for comparison with BEATs.

**Deliverable:** Baseline model and basic metrics saved in `models/`.

---

### Phase 3 — BEATs Encoder + Temporal Head (Core Model) (1–2 sessions)
**Goal:** Train and validate the BEATs temporal head as primary model.
1. **Frontend verification**
   - Inspect BEATs API expectations and verify that the current `encode_audio` input is correct.
   - If log-mel/fbank is required, implement frontend in `noise.model.beats.encode_audio()` using:
     - existing `noise.audio.featurize.log_mel_spectrogram`, or
     - torchaudio fbank if BEATs expects the Kaldi-style fbank.
   - Add a small unit test or scripted check to confirm expected tensor shapes.

2. **Head training**
   - Train head via `noise.training.train_beats`.
   - Confirm head input dim (e.g., 768 for iter3+ AS2M) matches BEATs output.
   - Save head checkpoint to `models/beats_head.pt`.

3. **Validation**
   - Run `noise.training.eval` on steady-state windows.
   - Generate histograms to assess class separation for thresholds.

**Deliverable:** BEATs head checkpoint + validation metrics + confirmed frontend.

---

### Phase 4 — Threshold Calibration (1 session)
**Goal:** Produce calibrated hysteresis thresholds from steady-state clips.
- Run `noise.training.calibrate` to generate `calibrated.yaml`.
- Verify that `t_on` and `t_off` maintain the required gap (`>= 0.10`).
- If overlap persists:
  - Increase smoothing window or EMA tau.
  - Increase inference window length (especially for fridge).
  - Re-run calibration.

**Deliverable:** Calibrated config file and documented threshold values.

---

### Phase 5 — Offline Validation (0.5–1 session)
**Goal:** Ensure no spurious events are emitted on steady-state clips.
- Run `noise.inference.offline` with `--require-no-events` using calibrated config.
- Review per-file event counts and probability logs (if enabled).
- Iterate thresholds or smoothing if events appear.

**Deliverable:** Offline run passes with zero false transitions on steady-state files.

---

### Phase 6 — Realtime Pipeline Validation (1–2 sessions)
**Goal:** Validate real-time streaming on the target machine.
- Run `noise.inference.realtime` with calibrated config.
- Verify capture device selection, CPU usage, and stable event logging.
- Check end-to-end latency vs. desired response window (2–10s).
- Fine-tune `window_s`, `hop_s`, `median_N`, `ema_tau_s`, and hysteresis durations.

**Deliverable:** Stable realtime event stream with reasonable latency and low flapping.

---

### Phase 7 — Performance / Deployment (Optional, but recommended) (1–2 sessions)
**Goal:** Optimize runtime for lower CPU and faster inference.
- Export head or full model via `noise.model.export_onnx`.
- (Optional) Convert to Core ML via `noise.model.export_coreml`.
- Decide runtime path:
  - PyTorch (fast iteration)
  - ONNX runtime
  - ONNX + CoreML EP (preferred for Apple hardware)
- If ONNX/CoreML is adopted, add a runtime switch in `noise.model.loader` and realtime inference to select backend.

**Deliverable:** Optimized inference path, documented and optionally wired into runtime.

---

### Phase 8 — Observability & UX (0.5–1 session)
**Goal:** Improve introspection and operational usability.
- Ensure probability and event CSV logs are easy to inspect.
- Add a lightweight summary report for realtime runs (optional).
- Document recommended configuration presets (robust vs. faster iter3+).

**Deliverable:** Clear logging outputs + human-friendly debugging workflow.

---

### Phase 9 — Testing & Documentation (1 session)
**Goal:** Make the system reliable and easy to reproduce.
- Add tests for:
  - BEATs frontend correctness (shape + expected ranges).
  - Head inference shape handling.
  - Calibration output invariants (gap enforcement).
- Update or add a short runbook in repo root (or expand `SPEC.md`):
  - Training commands (baseline + BEATs).
  - Calibration and offline checks.
  - Realtime usage and common parameters.

**Deliverable:** Tests for core logic + docs covering the full workflow.

---

## Acceptance Checklist (Release-ready)
- [ ] BEATs frontend confirmed and consistent across training/inference.
- [ ] BEATs head trained and saved with validated metrics.
- [ ] Calibrated thresholds produce no false events on steady-state clips.
- [ ] Realtime run emits stable events with acceptable latency.
- [ ] Performance acceptable on target MacBook.
- [ ] Optional ONNX/CoreML path verified (if chosen).
- [ ] Tests cover smoothing/hysteresis + BEATs inference integration.
- [ ] Runbook docs updated with `uv` commands.

---

## Suggested Command Map (All via `uv`)
- Baseline train: `uv run python -m noise.training.train`
- BEATs train: `uv run python -m noise.training.train_beats`
- Evaluate: `uv run python -m noise.training.eval`
- Calibrate: `uv run python -m noise.training.calibrate`
- Offline check: `uv run python -m noise.inference.offline --require-no-events`
- Realtime: `uv run python -m noise.inference.realtime`
- ONNX export: `uv run python -m noise.model.export_onnx`
- Core ML export: `uv run python -m noise.model.export_coreml`
