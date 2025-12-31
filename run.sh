#!/usr/bin/env bash
set -eu

uv run python src/infer/live.py \
  --beats-checkpoint models/BEATs_iter3_plus_AS2M.pt \
  --model-state models/run_20251231_133227/model.pt \
  --input-sr 16000 \
  --device mps \
  --max-lag-sec 2 \
  --only-changes

