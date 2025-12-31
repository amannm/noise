from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

from noise.audio.resample import resample_audio
from noise.config.loader import (
    get_float,
    get_int,
    get_nested,
    load_config,
    load_default_config,
)
from noise.inference.hysteresis import HysteresisConfig, MultiHysteresis
from noise.inference.smoother import ProbSmoother, SmoothingConfig
from noise.model.baseline import LABELS
from noise.model.loader import load_inference_model
from noise.training.dataset import label_from_path, list_wav_files
from noise.utils.logging import CsvLogger


def _load_audio(path: Path, *, target_sr: int) -> np.ndarray:
    audio, sr = sf.read(path, dtype="float32", always_2d=False)
    return resample_audio(audio, orig_sr=sr, target_sr=target_sr)


def _build_hysteresis(
    config: dict,
    *,
    hop_s: float,
    initial_state: dict[str, bool] | None = None,
) -> MultiHysteresis:
    hyst_cfg = get_nested(config, "hysteresis")
    configs = {}
    for name in LABELS:
        entry = get_nested(hyst_cfg, name)
        configs[name] = HysteresisConfig(
            t_on=get_float(entry, "t_on", 0.7),
            t_off=get_float(entry, "t_off", 0.3),
            n_on_s=get_float(entry, "n_on_s", 4.0),
            n_off_s=get_float(entry, "n_off_s", 8.0),
            cooldown_s=get_float(entry, "cooldown_s", 20.0),
        )
    return MultiHysteresis(configs, hop_s=hop_s, initial_state=initial_state)


def _iter_windows(audio: np.ndarray, window_len: int, hop_len: int):
    if window_len <= 0 or hop_len <= 0:
        return
    if audio.shape[0] < window_len:
        return
    for start in range(0, len(audio) - window_len + 1, hop_len):
        yield start, audio[start : start + window_len]


def _initial_state(mode: str, label: tuple[int, int]) -> dict[str, bool]:
    if mode == "label":
        return {"ac": bool(label[0]), "fridge": bool(label[1])}
    if mode == "on":
        return {"ac": True, "fridge": True}
    return {"ac": False, "fridge": False}


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline steady-state inference + event checks.")
    parser.add_argument("--samples-dir", type=Path, default=Path("samples"))
    parser.add_argument("--model-path", type=Path, default=None, help="Overrides baseline model or BEATs head path.")
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--window-s", type=float, default=None)
    parser.add_argument("--hop-s", type=float, default=None)
    parser.add_argument(
        "--initial-state",
        choices=("label", "off", "on"),
        default="label",
        help="Initial hysteresis state per file.",
    )
    parser.add_argument("--log-probs", type=Path, default=None)
    parser.add_argument("--log-events", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None, help="Write a JSON summary report.")
    parser.add_argument("--require-no-events", action="store_true")
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    config = load_config(args.config) if args.config else load_default_config()
    bundle = load_inference_model(config, model_path=args.model_path)
    target_sr = bundle.sample_rate

    infer_cfg = get_nested(config, "inference")
    smooth_cfg = get_nested(config, "smoothing")

    window_s = args.window_s if args.window_s is not None else get_float(infer_cfg, "window_s", 4.0)
    hop_s = args.hop_s if args.hop_s is not None else get_float(infer_cfg, "hop_s", 0.5)

    if window_s <= 0 or hop_s <= 0:
        raise ValueError("window_s and hop_s must be > 0")

    window_len = int(round(window_s * target_sr))
    hop_len = int(round(hop_s * target_sr))
    if window_len <= 0 or hop_len <= 0:
        raise ValueError("window_len/hop_len too small for sample rate")

    smoother_config = SmoothingConfig(
        median_N=get_int(smooth_cfg, "median_N", 9),
        ema_tau_s=get_float(smooth_cfg, "ema_tau_s", 6.0),
        hop_s=hop_s,
    )

    prob_logger = None
    event_logger = None
    if args.log_probs:
        prob_logger = CsvLogger(
            args.log_probs,
            [
                "file",
                "t_s",
                "p_ac",
                "p_fridge",
                "p_ac_smooth",
                "p_fridge_smooth",
            ],
        ).open()
    if args.log_events:
        event_logger = CsvLogger(
            args.log_events,
            ["file", "t_s", "device", "kind", "prob", "step"],
        ).open()

    files = list_wav_files(args.samples_dir)
    total_windows = 0
    total_events = 0
    any_failed = False
    failed_files: list[str] = []
    skipped_files: list[str] = []
    per_file_reports: list[dict[str, object]] = []

    try:
        for path in files:
            label = label_from_path(path, strict=not args.allow_heuristics)
            audio = _load_audio(path, target_sr=target_sr)
            if len(audio) < window_len:
                print(f"{path.name}: skipped (audio shorter than window)")
                skipped_files.append(path.name)
                continue

            initial_state = _initial_state(args.initial_state, label)
            hysteresis = _build_hysteresis(config, hop_s=hop_s, initial_state=initial_state)
            smoother = ProbSmoother(smoother_config)

            file_events = {name: 0 for name in LABELS}
            file_windows = 0

            for start, window in _iter_windows(audio, window_len, hop_len):
                file_windows += 1
                probs = bundle.predict_proba_from_audio(window)
                smooth = smoother.update(probs)
                smooth_arr = np.asarray(smooth, dtype=np.float32).reshape(-1)

                t_s = start / target_sr
                if prob_logger is not None:
                    prob_logger.write(
                        {
                            "file": path.name,
                            "t_s": round(t_s, 3),
                            "p_ac": float(probs[0]),
                            "p_fridge": float(probs[1]),
                            "p_ac_smooth": float(smooth_arr[0]),
                            "p_fridge_smooth": float(smooth_arr[1]),
                        }
                    )

                events = hysteresis.update({"ac": float(smooth_arr[0]), "fridge": float(smooth_arr[1])})
                for event in events:
                    file_events[event.device] += 1
                    if event_logger is not None:
                        event_logger.write(
                            {
                                "file": path.name,
                                "t_s": round(t_s, 3),
                                "device": event.device,
                                "kind": event.kind,
                                "prob": event.prob,
                                "step": event.step,
                            }
                        )

            total_windows += file_windows
            file_event_total = sum(file_events.values())
            total_events += file_event_total

            label_str = "ac" if label[0] else "none"
            if label[1]:
                label_str = "both" if label[0] else "fridge"
            per_file_reports.append(
                {
                    "file": path.name,
                    "label": label_str,
                    "duration_s": round(len(audio) / target_sr, 3),
                    "windows": file_windows,
                    "events": dict(file_events),
                    "event_total": file_event_total,
                }
            )
            print(
                f"{path.name}: label={label_str} windows={file_windows} "
                f"events=ac:{file_events['ac']} fridge:{file_events['fridge']}"
            )
            if args.require_no_events and file_event_total > 0:
                any_failed = True
                failed_files.append(path.name)

        print(f"\nSummary: files={len(files)} windows={total_windows} events={total_events}")

        summary = {
            "samples_dir": str(args.samples_dir),
            "config": str(args.config) if args.config else None,
            "model_path": str(args.model_path) if args.model_path else None,
            "window_s": window_s,
            "hop_s": hop_s,
            "files": len(files),
            "processed_files": len(per_file_reports),
            "skipped_files": skipped_files,
            "failed_files": failed_files,
            "total_windows": total_windows,
            "total_events": total_events,
            "require_no_events": args.require_no_events,
            "passed": not (args.require_no_events and any_failed),
            "per_file": per_file_reports,
        }

        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            with args.report.open("w", encoding="utf-8") as f:
                json.dump(summary, f, indent=2)
            print(f"Saved report to {args.report}")

        if args.require_no_events and any_failed:
            print("FAILED: events detected in steady-state files.")
            sys.exit(1)
    finally:
        if prob_logger is not None:
            prob_logger.close()
        if event_logger is not None:
            event_logger.close()


if __name__ == "__main__":
    main()
