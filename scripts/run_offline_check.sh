#!/usr/bin/env bash
set -euo pipefail

REPORT_DIR="${REPORT_DIR:-artifacts}"
mkdir -p "${REPORT_DIR}"

uv run python -m noise.inference.offline \
  --require-no-events \
  --report "${REPORT_DIR}/offline_report.json" \
  --log-probs "${REPORT_DIR}/offline_probs.csv" \
  --log-events "${REPORT_DIR}/offline_events.csv" \
  "$@"
