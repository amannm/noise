from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pandas as pd
import torch
from torch.utils.data import Dataset

from src.beats.preprocess import beats_fbank, frame_count, TARGET_SAMPLE_RATE
from src.datasets.augment import (
    apply_eq_tilt,
    apply_random_gain,
    mix_with_snr,
    spec_augment,
)
from src.utils.audio import load_audio


@dataclass
class AugmentConfig:
    gain_db_min: float = -6.0
    gain_db_max: float = 6.0
    mix_prob: float = 0.5
    mix_snr_min: float = 8.0
    mix_snr_max: float = 25.0
    eq_prob: float = 0.3
    eq_low_min: float = 150.0
    eq_low_max: float = 300.0
    eq_high_min: float = 2000.0
    eq_high_max: float = 5000.0
    eq_gain_max: float = 3.0
    spec_time_masks: int = 2
    spec_freq_masks: int = 2
    spec_max_time_sec: float = 0.4
    spec_max_freq_bins: int = 20


class WindowDataset(Dataset):
    def __init__(
        self,
        manifest: str | Path | pd.DataFrame,
        target_sr: int = TARGET_SAMPLE_RATE,
        augment: bool = True,
        augment_cfg: Optional[AugmentConfig] = None,
        seed: Optional[int] = None,
        return_meta: bool = False,
    ) -> None:
        if isinstance(manifest, pd.DataFrame):
            self.df = manifest.reset_index(drop=True)
        else:
            self.df = pd.read_parquet(manifest)
        self.target_sr = target_sr
        self.augment = augment
        self.augment_cfg = augment_cfg or AugmentConfig()
        self.rng = random.Random(seed)
        self.return_meta = return_meta

        self._cache: dict[str, torch.Tensor] = {}
        self._both_off_indices = self.df.index[
            (self.df["ac"] == 0) & (self.df["fridge"] == 0)
        ].tolist()

    def __len__(self) -> int:
        return len(self.df)

    def _load_window(self, path: str, start_sec: float, end_sec: float) -> torch.Tensor:
        if path not in self._cache:
            waveform, _ = load_audio(path, target_sr=self.target_sr, mono=True)
            self._cache[path] = waveform
        waveform = self._cache[path]
        start_idx = int(round(start_sec * self.target_sr))
        end_idx = int(round(end_sec * self.target_sr))
        window = waveform[..., start_idx:end_idx]
        if window.numel() == 0:
            raise ValueError(f"Empty window for {path} at {start_sec}-{end_sec}")
        return window

    def _maybe_mix(self, signal: torch.Tensor) -> torch.Tensor:
        if not self._both_off_indices:
            return signal
        cfg = self.augment_cfg
        if self.rng.random() > cfg.mix_prob:
            return signal
        mix_idx = self.rng.choice(self._both_off_indices)
        mix_row = self.df.loc[mix_idx]
        noise = self._load_window(
            mix_row.path, mix_row.start_sec, mix_row.end_sec
        )
        snr = self.rng.uniform(cfg.mix_snr_min, cfg.mix_snr_max)
        return mix_with_snr(signal, noise, snr)

    def _maybe_eq(self, signal: torch.Tensor) -> torch.Tensor:
        cfg = self.augment_cfg
        if self.rng.random() > cfg.eq_prob:
            return signal
        low = self.rng.uniform(cfg.eq_low_min, cfg.eq_low_max)
        high = self.rng.uniform(cfg.eq_high_min, cfg.eq_high_max)
        gain = self.rng.uniform(-cfg.eq_gain_max, cfg.eq_gain_max)
        return apply_eq_tilt(signal, self.target_sr, low, high, gain)

    def _apply_augment(self, signal: torch.Tensor) -> torch.Tensor:
        cfg = self.augment_cfg
        signal = apply_random_gain(signal, (cfg.gain_db_min, cfg.gain_db_max))
        signal = self._maybe_mix(signal)
        signal = self._maybe_eq(signal)
        return signal

    def __getitem__(self, idx: int):
        row = self.df.iloc[idx]
        window = self._load_window(row.path, row.start_sec, row.end_sec)

        if self.augment:
            window = self._apply_augment(window)

        fbank = beats_fbank(window, sample_rate=self.target_sr)
        fbank = fbank.squeeze(0)  # (frames, mel)

        if self.augment:
            max_time_frames = frame_count(self.augment_cfg.spec_max_time_sec)
            fbank = spec_augment(
                fbank,
                time_masks=self.augment_cfg.spec_time_masks,
                freq_masks=self.augment_cfg.spec_freq_masks,
                max_time_mask=max_time_frames,
                max_freq_mask=self.augment_cfg.spec_max_freq_bins,
            )

        labels = torch.tensor([row.ac, row.fridge], dtype=torch.float32)
        if self.return_meta:
            meta = {
                "recording_id": row.recording_id,
                "path": row.path,
            }
            return fbank, labels, meta
        return fbank, labels
