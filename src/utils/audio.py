from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch


DEFAULT_TARGET_SR = 16000


@dataclass
class AudioInfo:
    sample_rate: int
    duration_sec: float
    channels: int


def probe_audio(path: str | Path) -> AudioInfo:
    path = Path(path)
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=sample_rate,channels,duration:format=duration",
        "-of",
        "json",
        str(path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"ffprobe failed for {path}: {result.stderr.strip()}"
        )
    data = json.loads(result.stdout or "{}")
    streams = data.get("streams") or []
    stream = streams[0] if streams else {}
    sample_rate = stream.get("sample_rate")
    channels = stream.get("channels")
    duration = stream.get("duration") or (data.get("format") or {}).get(
        "duration"
    )

    if sample_rate is None or duration is None:
        raise RuntimeError(f"ffprobe missing fields for {path}")

    return AudioInfo(
        sample_rate=int(sample_rate),
        duration_sec=float(duration),
        channels=int(channels or 1),
    )


def load_audio(
    path: str | Path,
    target_sr: int = DEFAULT_TARGET_SR,
    mono: bool = True,
) -> tuple[torch.Tensor, int]:
    """Load audio via ffmpeg and resample to target_sr.

    Returns:
        waveform: Tensor shaped (channels, samples)
        sample_rate: target_sr (or source sr if target_sr is None)
    """
    path = Path(path)
    info: AudioInfo | None = None
    if target_sr is None or not mono:
        info = probe_audio(path)

    cmd = [
        "ffmpeg",
        "-nostdin",
        "-i",
        str(path),
        "-f",
        "f32le",
        "-acodec",
        "pcm_f32le",
    ]
    if mono:
        cmd += ["-ac", "1"]
    if target_sr is not None:
        cmd += ["-ar", str(target_sr)]
    cmd += ["-loglevel", "error", "-"]

    result = subprocess.run(cmd, capture_output=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            f"ffmpeg failed for {path}: {result.stderr.decode().strip()}"
        )

    audio = np.frombuffer(result.stdout, dtype=np.float32).copy()
    if audio.size == 0:
        raise RuntimeError(f"ffmpeg returned empty audio for {path}")

    if mono:
        waveform = torch.from_numpy(audio).unsqueeze(0)
        sample_rate = target_sr if target_sr is not None else info.sample_rate
    else:
        if info is None:
            info = probe_audio(path)
        channels = max(1, int(info.channels))
        if audio.size % channels != 0:
            raise RuntimeError(
                f"Decoded samples not divisible by channels for {path}"
            )
        waveform = torch.from_numpy(audio.reshape(-1, channels).T)
        sample_rate = target_sr if target_sr is not None else info.sample_rate

    return waveform, sample_rate


def waveform_rms(waveform: torch.Tensor) -> float:
    """Compute RMS for a 1D/2D waveform (expects mono)."""
    if waveform.dim() == 2:
        waveform = waveform.squeeze(0)
    return torch.sqrt(torch.mean(waveform**2)).item()


def window_waveform(
    waveform: torch.Tensor,
    sample_rate: int,
    window_sec: float,
    hop_sec: float,
) -> list[torch.Tensor]:
    window_samples = int(round(window_sec * sample_rate))
    hop_samples = int(round(hop_sec * sample_rate))
    total_samples = waveform.size(-1)
    if total_samples < window_samples:
        raise ValueError("Audio shorter than window length")
    windows = []
    for start in range(0, total_samples - window_samples + 1, hop_samples):
        end = start + window_samples
        windows.append(waveform[..., start:end])
    return windows
