from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class SplitConfig:
    train_s: float = 100.0
    val_s: float = 30.0
    test_s: float = 30.0
    gap_s: float = 10.0
    test_at_end: bool = True


def split_config_from_dict(raw: Mapping[str, object] | None) -> SplitConfig:
    if not raw:
        return SplitConfig()
    return SplitConfig(
        train_s=float(raw.get("train_s", 100.0)),
        val_s=float(raw.get("val_s", 30.0)),
        test_s=float(raw.get("test_s", 30.0)),
        gap_s=float(raw.get("gap_s", 10.0)),
        test_at_end=bool(raw.get("test_at_end", True)),
    )


def compute_split_ranges(duration_s: float, cfg: SplitConfig) -> dict[str, list[tuple[float, float]]]:
    if duration_s <= 0:
        return {"train": [], "val": [], "test": []}

    train_start = 0.0
    train_end = min(duration_s, max(0.0, cfg.train_s))

    gap_s = max(0.0, cfg.gap_s)
    val_start = min(duration_s, train_end + gap_s)
    val_end = min(duration_s, val_start + max(0.0, cfg.val_s))

    if cfg.test_at_end:
        test_end = duration_s
        test_start = max(val_end + gap_s, duration_s - max(0.0, cfg.test_s))
    else:
        test_start = min(duration_s, val_end + gap_s)
        test_end = min(duration_s, test_start + max(0.0, cfg.test_s))

    return {
        "train": _range_or_empty(train_start, train_end),
        "val": _range_or_empty(val_start, val_end),
        "test": _range_or_empty(test_start, test_end),
    }


def _range_or_empty(start: float, end: float) -> list[tuple[float, float]]:
    if end <= start:
        return []
    return [(start, end)]
