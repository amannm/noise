from __future__ import annotations

import queue
from dataclasses import dataclass
from typing import Callable

import numpy as np
import sounddevice as sd

StatusHandler = Callable[[str], None]


@dataclass(frozen=True)
class CaptureConfig:
    sample_rate: int
    chunk_size: int
    device: int | None = None
    channels: int = 1
    dtype: str = "float32"


class AudioCapture:
    """Simple chunked audio capture using sounddevice."""

    def __init__(
        self,
        config: CaptureConfig,
        *,
        status_handler: StatusHandler | None = None,
        queue_maxsize: int = 0,
    ) -> None:
        if config.sample_rate <= 0:
            raise ValueError("sample_rate must be > 0")
        if config.chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")
        if config.channels <= 0:
            raise ValueError("channels must be > 0")
        if queue_maxsize < 0:
            raise ValueError("queue_maxsize must be >= 0")

        self._config = config
        self._status_handler = status_handler
        self._queue: queue.Queue[np.ndarray] = queue.Queue(maxsize=queue_maxsize)
        self._stream = sd.InputStream(
            samplerate=config.sample_rate,
            channels=config.channels,
            dtype=config.dtype,
            blocksize=config.chunk_size,
            device=config.device,
            callback=self._callback,
        )

    @property
    def config(self) -> CaptureConfig:
        return self._config

    def _callback(self, indata: np.ndarray, frames: int, time_info, status) -> None:
        if status and self._status_handler:
            self._status_handler(str(status))
        data = indata.copy()
        try:
            self._queue.put_nowait(data)
        except queue.Full:
            try:
                _ = self._queue.get_nowait()
            except queue.Empty:
                pass
            self._queue.put_nowait(data)

    def start(self) -> "AudioCapture":
        self._stream.start()
        return self

    def stop(self) -> None:
        self._stream.stop()

    def close(self) -> None:
        self._stream.close()

    def read(self, *, timeout: float | None = None) -> np.ndarray:
        return self._queue.get(timeout=timeout)

    def __enter__(self) -> "AudioCapture":
        return self.start()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()


def list_input_devices() -> list[dict[str, object]]:
    devices = list(sd.query_devices())
    return [dict(device) for device in devices if device.get("max_input_channels", 0) > 0]
