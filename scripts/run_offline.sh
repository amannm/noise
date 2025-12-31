#!/usr/bin/env bash
set -euo pipefail

uv run python -m noise.inference.offline "$@"
