from __future__ import annotations

import torch
import torchaudio.compliance.kaldi as ta_kaldi

F_BANK_MEAN = 15.41663
F_BANK_STD = 6.55582
TARGET_SAMPLE_RATE = 16000
NUM_MEL_BINS = 128
FRAME_LENGTH_MS = 25
FRAME_SHIFT_MS = 10


def _as_batch(waveform: torch.Tensor) -> torch.Tensor:
    if waveform.dim() == 1:
        return waveform.unsqueeze(0)
    if waveform.dim() == 2:
        # (channels, samples) -> mono -> (1, samples)
        if waveform.size(0) > 1:
            waveform = waveform.mean(dim=0, keepdim=False)
        return waveform.unsqueeze(0)
    if waveform.dim() == 3:
        # (batch, channels, samples) -> mono
        if waveform.size(1) > 1:
            waveform = waveform.mean(dim=1)
        return waveform
    raise ValueError(f"Unsupported waveform shape: {waveform.shape}")


def beats_fbank(
    waveform: torch.Tensor,
    sample_rate: int = TARGET_SAMPLE_RATE,
    fbank_mean: float = F_BANK_MEAN,
    fbank_std: float = F_BANK_STD,
) -> torch.Tensor:
    """Compute BEATs-compliant fbank features.

    Expects 16 kHz mono audio. Returns (batch, frames, mel).
    """
    if sample_rate != TARGET_SAMPLE_RATE:
        raise ValueError(
            f"Expected {TARGET_SAMPLE_RATE} Hz audio, got {sample_rate}"
        )

    batch = _as_batch(waveform)
    fbanks = []
    for sample in batch:
        # Match BEATs preprocessing: scale to int16 range
        sample = sample.unsqueeze(0) * (2**15)
        fbank = ta_kaldi.fbank(
            sample,
            num_mel_bins=NUM_MEL_BINS,
            sample_frequency=TARGET_SAMPLE_RATE,
            frame_length=FRAME_LENGTH_MS,
            frame_shift=FRAME_SHIFT_MS,
        )
        fbanks.append(fbank)
    fbank = torch.stack(fbanks, dim=0)
    fbank = (fbank - fbank_mean) / (2 * fbank_std)
    return fbank


def frame_count(window_sec: float) -> int:
    """Approximate frame count for a given window length in seconds."""
    # Frame shift is 10ms; use floor for conservative masking.
    return int(window_sec / (FRAME_SHIFT_MS / 1000.0))
