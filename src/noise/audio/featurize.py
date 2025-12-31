from __future__ import annotations

import numpy as np
import librosa


def _n_fft_from_win_length(win_length: int) -> int:
    """Pick a power-of-two n_fft >= win_length for efficient FFT."""
    if win_length <= 0:
        raise ValueError("win_length must be > 0")
    return 1 << (win_length - 1).bit_length()


def log_mel_spectrogram(
    audio: np.ndarray,
    sample_rate: int,
    *,
    n_mels: int = 128,
    win_ms: float = 25.0,
    hop_ms: float = 10.0,
    fmin: float = 0.0,
    fmax: float | None = None,
) -> np.ndarray:
    """Compute log-mel spectrogram (dB) for BEATs-compatible frontend."""
    if sample_rate <= 0:
        raise ValueError("sample_rate must be > 0")
    win_length = int(round(sample_rate * win_ms / 1000.0))
    hop_length = int(round(sample_rate * hop_ms / 1000.0))
    if win_length <= 0 or hop_length <= 0:
        raise ValueError("win_ms/hop_ms too small for given sample_rate")
    n_fft = _n_fft_from_win_length(win_length)

    mel = librosa.feature.melspectrogram(
        y=np.asarray(audio, dtype=np.float32),
        sr=sample_rate,
        n_fft=n_fft,
        hop_length=hop_length,
        win_length=win_length,
        window="hann",
        center=True,
        power=2.0,
        n_mels=n_mels,
        fmin=fmin,
        fmax=fmax,
    )
    log_mel = librosa.power_to_db(mel, ref=1.0, amin=1e-10, top_db=None)
    return log_mel.astype(np.float32)
