# Noise: Live Appliance On/Off Detection via Audio

Concise runbook for training, calibration, offline checks, and live inference. All commands use `uv`.

## Prereqs
- `./samples` contains steady-state WAVs named: `all_off.wav`, `ac_on.wav`, `fridge_on.wav`, `all_on.wav`.
- Baseline model works out of the box after training.
- BEATs model requires `torch`, the official BEATs repo on `PYTHONPATH`, and a checkpoint at
  `models/BEATs_iter3_plus_AS2M.pt`.

## Runbook (exact `uv` commands)
Dataset summary:
```bash
uv run python -m noise.training.dataset --samples-dir samples
```

Train baseline model (writes `models/baseline.joblib`):
```bash
uv run python -m noise.training.train --config src/noise/config/defaults.yaml --samples-dir samples
```

Train BEATs head (writes `models/beats_head.pt`):
```bash
uv run python -m noise.training.train_beats \
  --config src/noise/config/defaults.yaml \
  --samples-dir samples \
  --checkpoint-path models/BEATs_iter3_plus_AS2M.pt \
  --head-out models/beats_head.pt
```

Calibrate thresholds (writes `artifacts/calibrated.yaml`):
```bash
uv run python -m noise.training.calibrate \
  --config src/noise/config/defaults.yaml \
  --samples-dir samples \
  --output artifacts/calibrated.yaml
```

Offline integration check (no events expected in steady-state files):
```bash
uv run python -m noise.inference.offline \
  --config artifacts/calibrated.yaml \
  --require-no-events \
  --report artifacts/offline_report.json \
  --log-probs artifacts/offline_probs.csv \
  --log-events artifacts/offline_events.csv
```

Realtime streaming (Ctrl+C to stop):
```bash
uv run python -m noise.inference.realtime \
  --config artifacts/calibrated.yaml \
  --log-probs artifacts/realtime_probs.csv \
  --log-events artifacts/realtime_events.csv
```

## Notes
- To use the BEATs model for inference, set `model.type: beats` in your config (or create a copy of
  `src/noise/config/defaults.yaml` with that change) and point `--config` to it.
- If you use non-standard sample filenames, add them to `LABEL_MAP` in `src/noise/training/dataset.py`
  or pass `--allow-heuristics` to dataset/training/offline commands.
- Helper wrappers live in `scripts/` (for example `scripts/run_offline_check.sh`) and all call `uv`.
