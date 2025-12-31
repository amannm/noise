from __future__ import annotations

import numpy as np


class RingBuffer:
    """Fixed-size ring buffer for streaming audio samples."""

    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._capacity = int(capacity)
        self._buffer = np.zeros(self._capacity, dtype=np.float32)
        self._write_pos = 0
        self._filled = 0

    @property
    def capacity(self) -> int:
        return self._capacity

    def __len__(self) -> int:
        return self._filled

    def clear(self) -> None:
        self._write_pos = 0
        self._filled = 0

    def push(self, audio: np.ndarray) -> None:
        data = np.asarray(audio, dtype=np.float32).reshape(-1)
        if data.size == 0:
            return
        if data.size >= self._capacity:
            self._buffer[:] = data[-self._capacity :]
            self._write_pos = 0
            self._filled = self._capacity
            return

        end = self._write_pos + data.size
        if end <= self._capacity:
            self._buffer[self._write_pos : end] = data
        else:
            first = self._capacity - self._write_pos
            self._buffer[self._write_pos :] = data[:first]
            self._buffer[: end - self._capacity] = data[first:]
        self._write_pos = end % self._capacity
        self._filled = min(self._capacity, self._filled + data.size)

    def read_latest(self, length: int | None = None) -> np.ndarray:
        if self._filled == 0:
            return np.zeros(0, dtype=np.float32)
        if length is None or length > self._filled:
            length = self._filled
        length = int(length)
        if length <= 0:
            return np.zeros(0, dtype=np.float32)

        start = (self._write_pos - length) % self._capacity
        end = start + length
        if end <= self._capacity:
            return np.array(self._buffer[start:end], copy=True)
        tail = self._capacity - start
        return np.concatenate(
            [self._buffer[start:], self._buffer[: length - tail]], axis=0
        ).astype(np.float32, copy=False)
