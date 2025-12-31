from __future__ import annotations

import numpy as np
import librosa


def _to_mono(audio: np.ndarray) -> np.ndarray:
    if audio.ndim == 1:
        return audio
    if audio.ndim == 2:
        return np.mean(audio, axis=1)
    raise ValueError(f"Unexpected audio shape: {audio.shape}")


def resample_audio(
    audio: np.ndarray,
    orig_sr: int,
    target_sr: int,
) -> np.ndarray:
    """Resample audio to target_sr using a high-quality bandlimited resampler."""
    audio = _to_mono(np.asarray(audio, dtype=np.float32))
    if orig_sr == target_sr:
        return audio
    return librosa.resample(audio, orig_sr=orig_sr, target_sr=target_sr, res_type="kaiser_best").astype(
        np.float32
    )
