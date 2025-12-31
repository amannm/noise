from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import torch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.audio import load_audio


def compute_windows(
    waveform: torch.Tensor,
    sample_rate: int,
    window_sec: float,
    hop_sec: float,
) -> tuple[list[float], list[float], list[float]]:
    window_samples = int(round(window_sec * sample_rate))
    hop_samples = int(round(hop_sec * sample_rate))
    total_samples = waveform.size(-1)

    if total_samples < window_samples:
        raise ValueError(
            f"Audio too short for windowing: {total_samples} samples"
        )

    starts = list(range(0, total_samples - window_samples + 1, hop_samples))
    start_secs: list[float] = []
    end_secs: list[float] = []
    rms_vals: list[float] = []

    for start in starts:
        end = start + window_samples
        window = waveform[..., start:end]
        rms = torch.sqrt(torch.mean(window**2)).item()
        start_secs.append(start / sample_rate)
        end_secs.append(end / sample_rate)
        rms_vals.append(rms)

    return start_secs, end_secs, rms_vals


def drop_outliers(
    start_secs: list[float],
    end_secs: list[float],
    rms_vals: list[float],
    drop_top_pct: float,
) -> tuple[list[float], list[float], list[float]]:
    if drop_top_pct <= 0:
        return start_secs, end_secs, rms_vals

    n = len(rms_vals)
    if n == 0:
        return start_secs, end_secs, rms_vals

    k = int(round(n * drop_top_pct))
    if k <= 0:
        return start_secs, end_secs, rms_vals

    order = np.argsort(np.array(rms_vals))  # ascending
    drop_idx = set(order[-k:])

    kept_start: list[float] = []
    kept_end: list[float] = []
    kept_rms: list[float] = []
    for idx, (s, e, r) in enumerate(zip(start_secs, end_secs, rms_vals)):
        if idx in drop_idx:
            continue
        kept_start.append(s)
        kept_end.append(e)
        kept_rms.append(r)
    return kept_start, kept_end, kept_rms


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build window-level manifest with outlier removal."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("data/manifests/files.csv"),
        help="Input file-level manifest CSV",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/manifests/windows.parquet"),
        help="Output window-level manifest parquet",
    )
    parser.add_argument("--target-sr", type=int, default=16000)
    parser.add_argument("--window-sec", type=float, default=6.0)
    parser.add_argument("--hop-sec", type=float, default=1.5)
    parser.add_argument("--drop-top-pct", type=float, default=0.01)
    args = parser.parse_args()

    df = pd.read_csv(args.manifest)
    rows: list[dict[str, object]] = []

    for row in df.itertuples(index=False):
        waveform, sr = load_audio(row.path, target_sr=args.target_sr, mono=True)
        start_secs, end_secs, rms_vals = compute_windows(
            waveform, sr, args.window_sec, args.hop_sec
        )
        start_secs, end_secs, rms_vals = drop_outliers(
            start_secs, end_secs, rms_vals, args.drop_top_pct
        )

        for s, e, rms in zip(start_secs, end_secs, rms_vals):
            rows.append(
                {
                    "recording_id": row.recording_id,
                    "path": row.path,
                    "start_sec": s,
                    "end_sec": e,
                    "rms": rms,
                    "ac": row.ac,
                    "fridge": row.fridge,
                }
            )

    if not rows:
        raise ValueError("No windows generated; check inputs.")

    out_df = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_parquet(args.output, index=False)


if __name__ == "__main__":
    main()
