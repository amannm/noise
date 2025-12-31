from __future__ import annotations

from pathlib import Path

import torch
import torchaudio


DEFAULT_TARGET_SR = 16000


def load_audio(
    path: str | Path,
    target_sr: int = DEFAULT_TARGET_SR,
    mono: bool = True,
) -> tuple[torch.Tensor, int]:
    """Load audio and resample to target_sr.

    Returns:
        waveform: Tensor shaped (channels, samples)
        sample_rate: target_sr
    """
    path = Path(path)
    waveform, sample_rate = torchaudio.load(path)
    waveform = waveform.to(torch.float32)

    if mono and waveform.size(0) > 1:
        waveform = waveform.mean(dim=0, keepdim=True)

    if sample_rate != target_sr:
        waveform = torchaudio.functional.resample(
            waveform, orig_freq=sample_rate, new_freq=target_sr
        )
        sample_rate = target_sr

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
