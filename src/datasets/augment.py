from __future__ import annotations

import math
import random
from typing import Tuple

import torch
import torchaudio.functional as F


def apply_random_gain(waveform: torch.Tensor, gain_db_range: Tuple[float, float]) -> torch.Tensor:
    min_db, max_db = gain_db_range
    gain_db = random.uniform(min_db, max_db)
    gain = 10 ** (gain_db / 20.0)
    return waveform * gain


def mix_with_snr(
    signal: torch.Tensor, noise: torch.Tensor, snr_db: float
) -> torch.Tensor:
    signal_rms = torch.sqrt(torch.mean(signal**2))
    noise_rms = torch.sqrt(torch.mean(noise**2))
    if noise_rms.item() == 0:
        return signal
    target_noise_rms = signal_rms / (10 ** (snr_db / 20.0))
    noise = noise * (target_noise_rms / (noise_rms + 1e-8))
    return signal + noise


def _shelf_coefficients(
    kind: str,
    sample_rate: int,
    cutoff_hz: float,
    gain_db: float,
    slope: float = 1.0,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Design low/high shelf filter coefficients (RBJ cookbook)."""
    a = 10 ** (gain_db / 40.0)
    w0 = 2 * math.pi * (cutoff_hz / sample_rate)
    cos_w0 = math.cos(w0)
    sin_w0 = math.sin(w0)
    alpha = sin_w0 / 2 * math.sqrt((a + 1 / a) * (1 / slope - 1) + 2)
    beta = 2 * math.sqrt(a) * alpha

    if kind == "low":
        b0 = a * ((a + 1) - (a - 1) * cos_w0 + beta)
        b1 = 2 * a * ((a - 1) - (a + 1) * cos_w0)
        b2 = a * ((a + 1) - (a - 1) * cos_w0 - beta)
        a0 = (a + 1) + (a - 1) * cos_w0 + beta
        a1 = -2 * ((a - 1) + (a + 1) * cos_w0)
        a2 = (a + 1) + (a - 1) * cos_w0 - beta
    elif kind == "high":
        b0 = a * ((a + 1) + (a - 1) * cos_w0 + beta)
        b1 = -2 * a * ((a - 1) + (a + 1) * cos_w0)
        b2 = a * ((a + 1) + (a - 1) * cos_w0 - beta)
        a0 = (a + 1) - (a - 1) * cos_w0 + beta
        a1 = 2 * ((a - 1) - (a + 1) * cos_w0)
        a2 = (a + 1) - (a - 1) * cos_w0 - beta
    else:
        raise ValueError(f"Unknown shelf type: {kind}")

    b = torch.tensor([b0, b1, b2], dtype=torch.float32)
    a_coeffs = torch.tensor([a0, a1, a2], dtype=torch.float32)
    b = b / a0
    a_coeffs = a_coeffs / a0
    return a_coeffs, b


def apply_eq_tilt(
    waveform: torch.Tensor,
    sample_rate: int,
    low_freq_hz: float,
    high_freq_hz: float,
    gain_db: float,
) -> torch.Tensor:
    """Apply opposing low/high shelf filters for a gentle tilt."""
    a_low, b_low = _shelf_coefficients(
        "low", sample_rate, low_freq_hz, gain_db
    )
    a_high, b_high = _shelf_coefficients(
        "high", sample_rate, high_freq_hz, -gain_db
    )
    filtered = F.lfilter(waveform, a_low, b_low)
    filtered = F.lfilter(filtered, a_high, b_high)
    return filtered


def spec_augment(
    features: torch.Tensor,
    time_masks: int,
    freq_masks: int,
    max_time_mask: int,
    max_freq_mask: int,
) -> torch.Tensor:
    """Apply SpecAugment-style masking to a (frames, mel) tensor."""
    augmented = features.clone()
    num_frames, num_mels = augmented.shape

    for _ in range(time_masks):
        if num_frames == 0:
            break
        t = random.randint(0, max_time_mask)
        if t == 0:
            continue
        t0 = random.randint(0, max(0, num_frames - t))
        augmented[t0 : t0 + t, :] = 0

    for _ in range(freq_masks):
        if num_mels == 0:
            break
        f = random.randint(0, max_freq_mask)
        if f == 0:
            continue
        f0 = random.randint(0, max(0, num_mels - f))
        augmented[:, f0 : f0 + f] = 0

    return augmented
