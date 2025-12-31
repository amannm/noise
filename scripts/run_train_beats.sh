#!/usr/bin/env bash
set -euo pipefail

uv run python -m noise.training.train_beats "$@"
