from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
import soundfile as sf

from noise.audio.resample import resample_audio

LABEL_MAP: dict[str, tuple[int, int]] = {
    "ac_on": (1, 0),
    "fridge_on": (0, 1),
    "all_on": (1, 1),
    "all_off": (0, 0),
}


@dataclass(frozen=True)
class WindowConfig:
    sample_rate: int = 16000
    window_s: float = 4.0
    hop_s: float = 0.5
    strict_labels: bool = True

    def window_len(self) -> int:
        return int(round(self.sample_rate * self.window_s))

    def hop_len(self) -> int:
        return int(round(self.sample_rate * self.hop_s))


@dataclass(frozen=True)
class WindowRef:
    file_path: Path
    start: int
    label: tuple[int, int]


class WindowedWavDataset:
    """Windowed steady-state dataset with cached audio per file."""

    def __init__(
        self,
        samples_dir: Path,
        config: WindowConfig,
        *,
        files: list[Path] | None = None,
    ) -> None:
        self.samples_dir = samples_dir
        self.config = config
        self.files = sorted(files) if files is not None else _list_wav_files(samples_dir)
        if not self.files:
            raise FileNotFoundError(f"No .wav files provided for dataset at {samples_dir}")
        self._audio_cache: dict[Path, np.ndarray] = {}
        self._index: list[WindowRef] = []
        self._build_index()

    def __len__(self) -> int:
        return len(self._index)

    def __getitem__(self, idx: int) -> tuple[np.ndarray, np.ndarray, dict[str, str | int]]:
        ref = self._index[idx]
        audio = self._audio_cache[ref.file_path]
        window_len = self.config.window_len()
        window = audio[ref.start : ref.start + window_len]
        label = np.asarray(ref.label, dtype=np.float32)
        meta = {"file": str(ref.file_path), "start": ref.start}
        return window, label, meta

    def _build_index(self) -> None:
        window_len = self.config.window_len()
        hop_len = self.config.hop_len()
        if window_len <= 0 or hop_len <= 0:
            raise ValueError("window_s and hop_s must be > 0")

        for path in self.files:
            label = _label_from_path(path, strict=self.config.strict_labels)
            audio, _ = _load_audio(path, target_sr=self.config.sample_rate)
            self._audio_cache[path] = audio
            for start in _window_indices(len(audio), window_len, hop_len):
                self._index.append(WindowRef(path, start, label))


@dataclass(frozen=True)
class DatasetSummary:
    total_files: int
    total_windows: int
    per_file: list[dict[str, object]]
    label_counts: dict[str, int]


def summarize_dataset(samples_dir: Path, config: WindowConfig) -> DatasetSummary:
    files = _list_wav_files(samples_dir)
    label_counts: dict[str, int] = {"none": 0, "ac": 0, "fridge": 0, "both": 0}
    per_file: list[dict[str, object]] = []

    window_len = config.window_len()
    hop_len = config.hop_len()

    total_windows = 0
    for path in files:
        label = _label_from_path(path, strict=config.strict_labels)
        audio, sr = _load_audio(path, target_sr=config.sample_rate)
        n_windows = _count_windows(len(audio), window_len, hop_len)
        total_windows += n_windows

        label_key = _label_key(label)
        label_counts[label_key] += n_windows

        duration_s = len(audio) / sr if sr else 0.0
        per_file.append(
            {
                "file": path.name,
                "label": label_key,
                "sample_rate": sr,
                "duration_s": round(duration_s, 2),
                "windows": n_windows,
            }
        )

    return DatasetSummary(
        total_files=len(files),
        total_windows=total_windows,
        per_file=per_file,
        label_counts=label_counts,
    )


def list_wav_files(samples_dir: Path) -> list[Path]:
    return _list_wav_files(samples_dir)


def label_from_path(path: Path, *, strict: bool = True) -> tuple[int, int]:
    return _label_from_path(path, strict=strict)


def _list_wav_files(samples_dir: Path) -> list[Path]:
    if not samples_dir.exists():
        raise FileNotFoundError(f"Samples dir not found: {samples_dir}")
    files = sorted(samples_dir.glob("*.wav"))
    if not files:
        raise FileNotFoundError(f"No .wav files found in {samples_dir}")
    return files


def _label_from_path(path: Path, *, strict: bool) -> tuple[int, int]:
    stem = path.stem.lower()
    if stem in LABEL_MAP:
        return LABEL_MAP[stem]
    if strict:
        raise ValueError(f"Unknown label for {path.name}. Add it to LABEL_MAP.")
    return _label_from_heuristic(stem)


def _label_from_heuristic(stem: str) -> tuple[int, int]:
    has_ac = "ac" in stem
    has_fridge = "fridge" in stem or "refrigerator" in stem
    if "all_off" in stem or "none" in stem:
        return (0, 0)
    if "all_on" in stem or "both" in stem:
        return (1, 1)
    return (1 if has_ac else 0, 1 if has_fridge else 0)


def _label_key(label: tuple[int, int]) -> str:
    ac, fridge = label
    if ac and fridge:
        return "both"
    if ac:
        return "ac"
    if fridge:
        return "fridge"
    return "none"


def _load_audio(path: Path, *, target_sr: int) -> tuple[np.ndarray, int]:
    audio, sr = sf.read(path, dtype="float32", always_2d=False)
    audio = resample_audio(audio, orig_sr=sr, target_sr=target_sr)
    return audio, target_sr


def _window_indices(n_samples: int, window_len: int, hop_len: int) -> Iterable[int]:
    if n_samples < window_len:
        return []
    return range(0, n_samples - window_len + 1, hop_len)


def _count_windows(n_samples: int, window_len: int, hop_len: int) -> int:
    if n_samples < window_len:
        return 0
    return 1 + (n_samples - window_len) // hop_len


def _print_summary(summary: DatasetSummary, config: WindowConfig, samples_dir: Path) -> None:
    print(f"Samples dir: {samples_dir}")
    print(f"Files: {summary.total_files}")
    print(f"Window: {config.window_s:.2f}s  Hop: {config.hop_s:.2f}s")
    print(f"Target sample rate: {config.sample_rate}")
    print(f"Total windows: {summary.total_windows}")
    print("\nPer-file:")
    for item in summary.per_file:
        print(
            f"  {item['file']}: label={item['label']} sr={item['sample_rate']} "
            f"duration={item['duration_s']}s windows={item['windows']}"
        )
    print("\nLabel counts:")
    for key in ("none", "ac", "fridge", "both"):
        print(f"  {key}: {summary.label_counts[key]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize steady-state windowing.")
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--sample-rate", type=int, default=16000)
    parser.add_argument("--window-s", type=float, default=4.0)
    parser.add_argument("--hop-s", type=float, default=0.5)
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    config = WindowConfig(
        sample_rate=args.sample_rate,
        window_s=args.window_s,
        hop_s=args.hop_s,
        strict_labels=not args.allow_heuristics,
    )
    summary = summarize_dataset(args.samples_dir, config)
    _print_summary(summary, config, args.samples_dir)


if __name__ == "__main__":
    main()
