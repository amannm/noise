from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

import numpy as np
import soundfile as sf
from scipy import signal

from noise.audio.resample import resample_audio
from noise.training.dataset import label_from_path, list_wav_files
from noise.training.splits import SplitConfig, compute_split_ranges


@dataclass(frozen=True)
class AugmentConfig:
    enabled: bool = True
    p_gain: float = 0.8
    gain_db_min: float = -6.0
    gain_db_max: float = 6.0
    p_filter: float = 0.5
    p_noise: float = 0.4
    noise_db_min: float = -30.0
    noise_db_max: float = -15.0
    p_time_mask: float = 0.3
    time_mask_max_s: float = 0.2


def augment_config_from_dict(raw: Mapping[str, object] | None) -> AugmentConfig:
    if not raw:
        return AugmentConfig()
    return AugmentConfig(
        enabled=bool(raw.get("enabled", True)),
        p_gain=float(raw.get("p_gain", 0.8)),
        gain_db_min=float(raw.get("gain_db_min", -6.0)),
        gain_db_max=float(raw.get("gain_db_max", 6.0)),
        p_filter=float(raw.get("p_filter", 0.5)),
        p_noise=float(raw.get("p_noise", 0.4)),
        noise_db_min=float(raw.get("noise_db_min", -30.0)),
        noise_db_max=float(raw.get("noise_db_max", -15.0)),
        p_time_mask=float(raw.get("p_time_mask", 0.3)),
        time_mask_max_s=float(raw.get("time_mask_max_s", 0.2)),
    )


@dataclass
class NoiseSource:
    audio: np.ndarray
    ranges: list[tuple[int, int]]

    def sample(self, length: int, rng: np.random.Generator) -> np.ndarray | None:
        if length <= 0:
            return None
        valid = [item for item in self.ranges if item[1] - item[0] >= length]
        if not valid:
            return None
        start, end = valid[int(rng.integers(0, len(valid)))]
        if end - start == length:
            return self.audio[start:end].copy()
        offset = int(rng.integers(start, end - length + 1))
        return self.audio[offset : offset + length].copy()


@dataclass
class NoisePool:
    sources: list[NoiseSource]

    def sample(self, length: int, rng: np.random.Generator) -> np.ndarray | None:
        if not self.sources:
            return None
        candidates = [src for src in self.sources if any(r[1] - r[0] >= length for r in src.ranges)]
        if not candidates:
            return None
        src = candidates[int(rng.integers(0, len(candidates)))]
        return src.sample(length, rng)


def build_noise_pool(
    samples_dir: Path,
    *,
    split_config: SplitConfig | None,
    sample_rate: int,
    strict_labels: bool,
) -> NoisePool | None:
    files = list_wav_files(samples_dir)
    noise_sources: list[NoiseSource] = []
    for path in files:
        if label_from_path(path, strict=strict_labels) != (0, 0):
            continue
        audio, _ = _load_audio(path, target_sr=sample_rate)
        duration_s = len(audio) / float(sample_rate) if sample_rate > 0 else 0.0
        if split_config is None:
            ranges_s = [(0.0, duration_s)]
        else:
            ranges_s = compute_split_ranges(duration_s, split_config).get("train", [])
        ranges = []
        for start_s, end_s in ranges_s:
            start_idx = max(0, int(round(start_s * sample_rate)))
            end_idx = max(0, int(round(end_s * sample_rate)))
            if end_idx > start_idx:
                ranges.append((start_idx, min(end_idx, len(audio))))
        if ranges:
            noise_sources.append(NoiseSource(audio=audio, ranges=ranges))
    if not noise_sources:
        return None
    return NoisePool(sources=noise_sources)


class AudioAugmenter:
    def __init__(
        self,
        config: AugmentConfig,
        *,
        sample_rate: int,
        noise_pool: NoisePool | None = None,
        seed: int | None = None,
    ) -> None:
        self.config = config
        self.sample_rate = sample_rate
        self.noise_pool = noise_pool
        self.rng = np.random.default_rng(seed)

    def __call__(self, audio: np.ndarray) -> np.ndarray:
        if audio.ndim == 1:
            return self._augment_one(audio)
        return np.stack([self._augment_one(item) for item in audio], axis=0)

    def _augment_one(self, audio: np.ndarray) -> np.ndarray:
        out = np.asarray(audio, dtype=np.float32).copy()
        if out.size == 0 or not self.config.enabled:
            return out

        out = self._apply_gain(out)
        out = self._apply_filter(out)
        out = self._apply_noise(out)
        out = self._apply_time_mask(out)
        return np.clip(out, -1.0, 1.0)

    def _apply_gain(self, audio: np.ndarray) -> np.ndarray:
        if self.rng.random() >= self.config.p_gain:
            return audio
        lo = min(self.config.gain_db_min, self.config.gain_db_max)
        hi = max(self.config.gain_db_min, self.config.gain_db_max)
        gain_db = float(self.rng.uniform(lo, hi))
        gain = float(10.0 ** (gain_db / 20.0))
        return audio * gain

    def _apply_filter(self, audio: np.ndarray) -> np.ndarray:
        if self.rng.random() >= self.config.p_filter:
            return audio
        nyquist = 0.5 * float(self.sample_rate)
        if nyquist <= 100:
            return audio
        kind = self.rng.choice(["lowpass", "highpass", "bandpass"])
        try:
            if kind == "lowpass":
                cutoff = float(self.rng.uniform(300.0, min(7000.0, nyquist - 100.0)))
                sos = signal.butter(4, cutoff, btype="lowpass", fs=self.sample_rate, output="sos")
            elif kind == "highpass":
                cutoff = float(self.rng.uniform(50.0, min(1200.0, nyquist - 100.0)))
                sos = signal.butter(4, cutoff, btype="highpass", fs=self.sample_rate, output="sos")
            else:
                low = float(self.rng.uniform(50.0, 1000.0))
                high = float(self.rng.uniform(low + 200.0, min(7000.0, nyquist - 100.0)))
                if high <= low:
                    return audio
                sos = signal.butter(4, (low, high), btype="bandpass", fs=self.sample_rate, output="sos")
        except ValueError:
            return audio

        try:
            return signal.sosfiltfilt(sos, audio).astype(np.float32, copy=False)
        except ValueError:
            return signal.sosfilt(sos, audio).astype(np.float32, copy=False)

    def _apply_noise(self, audio: np.ndarray) -> np.ndarray:
        if self.rng.random() >= self.config.p_noise or self.noise_pool is None:
            return audio
        noise = self.noise_pool.sample(len(audio), self.rng)
        if noise is None:
            return audio
        signal_rms = float(np.sqrt(np.mean(audio ** 2) + 1e-12))
        noise_rms = float(np.sqrt(np.mean(noise ** 2) + 1e-12))
        if noise_rms <= 0:
            return audio
        lo = min(self.config.noise_db_min, self.config.noise_db_max)
        hi = max(self.config.noise_db_min, self.config.noise_db_max)
        noise_db = float(self.rng.uniform(lo, hi))
        target_ratio = float(10.0 ** (noise_db / 20.0))
        scaled = noise * (signal_rms * target_ratio / noise_rms)
        return audio + scaled

    def _apply_time_mask(self, audio: np.ndarray) -> np.ndarray:
        if self.rng.random() >= self.config.p_time_mask:
            return audio
        max_len = int(round(self.config.time_mask_max_s * self.sample_rate))
        if max_len <= 1 or max_len >= audio.shape[0]:
            return audio
        mask_len = int(self.rng.integers(1, max_len + 1))
        start = int(self.rng.integers(0, audio.shape[0] - mask_len + 1))
        audio[start : start + mask_len] = 0.0
        return audio


def _load_audio(path: Path, *, target_sr: int) -> tuple[np.ndarray, int]:
    audio, sr = sf.read(path, dtype="float32", always_2d=False)
    audio = resample_audio(audio, orig_sr=sr, target_sr=target_sr)
    return audio, target_sr
