from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping

import yaml


def load_config(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Config at {path} must be a mapping")
    return data


def load_default_config() -> dict[str, Any]:
    default_path = Path(__file__).resolve().parent / "defaults.yaml"
    return load_config(default_path)


def merge_config(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge override into base without mutating inputs."""
    merged: dict[str, Any] = dict(base)
    for key, value in override.items():
        if (
            key in merged
            and isinstance(merged[key], dict)
            and isinstance(value, dict)
        ):
            merged[key] = merge_config(merged[key], value)
        else:
            merged[key] = value
    return merged


def get_nested(config: Mapping[str, Any], key: str, default: dict | None = None) -> dict[str, Any]:
    value = config.get(key, default or {})
    return value if isinstance(value, dict) else default or {}


def get_float(config: Mapping[str, Any], key: str, default: float) -> float:
    value = config.get(key, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def get_int(config: Mapping[str, Any], key: str, default: int) -> int:
    value = config.get(key, default)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def get_path(config: Mapping[str, Any], key: str, default: Path) -> Path:
    value = config.get(key, default)
    if isinstance(value, Path):
        return value
    if isinstance(value, str):
        return Path(value)
    return default
