#!/usr/bin/env bash
set -euo pipefail

uv run python -m noise.model.export_coreml "$@"
