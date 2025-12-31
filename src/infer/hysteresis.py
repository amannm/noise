from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass
class Hysteresis:
    t_on: float
    t_off: float
    state: bool = False

    def update(self, value: float) -> bool:
        if not self.state and value >= self.t_on:
            self.state = True
        elif self.state and value <= self.t_off:
            self.state = False
        return self.state


class Debouncer:
    def __init__(self, k: int) -> None:
        self.k = k
        self.history: Deque[str] = deque(maxlen=k)
        self.current: str | None = None

    def update(self, state: str) -> str | None:
        self.history.append(state)
        if len(self.history) < self.k:
            return None
        if len(set(self.history)) == 1:
            if self.current != state:
                self.current = state
                return state
        return None
