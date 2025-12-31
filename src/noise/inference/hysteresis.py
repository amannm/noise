from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class HysteresisConfig:
    t_on: float
    t_off: float
    n_on_s: float
    n_off_s: float
    cooldown_s: float


@dataclass(frozen=True)
class HysteresisEvent:
    device: str
    kind: str
    prob: float
    step: int


def _duration_to_hops(duration_s: float, hop_s: float, *, min_hops: int) -> int:
    if duration_s <= 0:
        return min_hops
    return max(min_hops, int(math.ceil(duration_s / hop_s)))


class HysteresisState:
    """Per-device hysteresis state machine."""

    def __init__(
        self,
        config: HysteresisConfig,
        *,
        hop_s: float,
        initial_on: bool = False,
    ) -> None:
        if hop_s <= 0:
            raise ValueError("hop_s must be > 0")
        if config.t_on <= config.t_off:
            raise ValueError("t_on must be > t_off for hysteresis")
        if not (0.0 <= config.t_on <= 1.0 and 0.0 <= config.t_off <= 1.0):
            raise ValueError("t_on/t_off must be in [0, 1]")
        if config.n_on_s < 0 or config.n_off_s < 0 or config.cooldown_s < 0:
            raise ValueError("n_on_s/n_off_s/cooldown_s must be >= 0")

        self.config = config
        self.hop_s = hop_s
        self.is_on = initial_on
        self.step = 0

        self._on_hops = _duration_to_hops(config.n_on_s, hop_s, min_hops=1)
        self._off_hops = _duration_to_hops(config.n_off_s, hop_s, min_hops=1)
        self._cooldown_hops = _duration_to_hops(config.cooldown_s, hop_s, min_hops=0)

        self._on_count = 0
        self._off_count = 0
        self._cooldown_remaining = 0

    def reset(self, *, initial_on: bool | None = None) -> None:
        if initial_on is not None:
            self.is_on = initial_on
        self.step = 0
        self._on_count = 0
        self._off_count = 0
        self._cooldown_remaining = 0

    def update(self, prob: float) -> bool | None:
        """Update with a new probability, returning True (on), False (off), or None."""
        self.step += 1
        if self._cooldown_remaining > 0:
            self._cooldown_remaining -= 1

        if self.is_on:
            if prob <= self.config.t_off:
                self._off_count += 1
            else:
                self._off_count = 0
            self._on_count = 0
            if self._off_count >= self._off_hops and self._cooldown_remaining == 0:
                self.is_on = False
                self._off_count = 0
                self._cooldown_remaining = self._cooldown_hops
                return False
            return None

        if prob >= self.config.t_on:
            self._on_count += 1
        else:
            self._on_count = 0
        self._off_count = 0
        if self._on_count >= self._on_hops and self._cooldown_remaining == 0:
            self.is_on = True
            self._on_count = 0
            self._cooldown_remaining = self._cooldown_hops
            return True
        return None


class MultiHysteresis:
    """Run multiple device hysteresis machines in parallel."""

    def __init__(
        self,
        configs: dict[str, HysteresisConfig],
        *,
        hop_s: float,
        initial_state: dict[str, bool] | None = None,
    ) -> None:
        initial_state = initial_state or {}
        self.states = {
            name: HysteresisState(config, hop_s=hop_s, initial_on=initial_state.get(name, False))
            for name, config in configs.items()
        }

    def reset(self, *, initial_state: dict[str, bool] | None = None) -> None:
        initial_state = initial_state or {}
        for name, state in self.states.items():
            state.reset(initial_on=initial_state.get(name))

    def update(self, probs: dict[str, float]) -> list[HysteresisEvent]:
        events: list[HysteresisEvent] = []
        for name, prob in probs.items():
            if name not in self.states:
                raise KeyError(f"Unknown device '{name}'")
            state = self.states[name]
            result = state.update(prob)
            if result is None:
                continue
            kind = "on" if result else "off"
            events.append(HysteresisEvent(device=name, kind=kind, prob=float(prob), step=state.step))
        return events
