from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable

import numpy as np


def ema_alpha(hop_s: float, tau_s: float) -> float:
    """Compute EMA alpha from hop and time constant."""
    if hop_s <= 0:
        raise ValueError("hop_s must be > 0")
    if tau_s <= 0:
        raise ValueError("tau_s must be > 0")
    return float(np.exp(-hop_s / tau_s))


@dataclass(frozen=True)
class SmoothingConfig:
    median_N: int = 9
    ema_tau_s: float = 6.0
    hop_s: float = 0.5


class ProbSmoother:
    """Median + EMA smoothing for probability streams."""

    def __init__(self, config: SmoothingConfig) -> None:
        if config.median_N <= 0:
            raise ValueError("median_N must be >= 1")
        if config.hop_s <= 0:
            raise ValueError("hop_s must be > 0")
        if config.ema_tau_s <= 0:
            raise ValueError("ema_tau_s must be > 0")

        self.config = config
        self._alpha = ema_alpha(config.hop_s, config.ema_tau_s)
        self._window: deque[np.ndarray] = deque(maxlen=config.median_N)
        self._ema: np.ndarray | None = None

    def reset(self) -> None:
        self._window.clear()
        self._ema = None

    def update(self, probs: np.ndarray | float) -> np.ndarray | float:
        arr = np.asarray(probs, dtype=np.float32)
        self._window.append(arr)
        median = np.median(np.stack(self._window, axis=0), axis=0)
        if self._ema is None:
            self._ema = median
        else:
            self._ema = self._alpha * self._ema + (1.0 - self._alpha) * median
        result = np.array(self._ema, copy=True)
        if result.ndim == 0:
            return float(result)
        return result


def smooth_sequence(
    sequence: Iterable[np.ndarray | float],
    config: SmoothingConfig,
) -> list[np.ndarray | float]:
    smoother = ProbSmoother(config)
    return [smoother.update(item) for item in sequence]
