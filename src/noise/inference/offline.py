from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

from noise.audio.resample import resample_audio
from noise.config.loader import load_config
from noise.inference.hysteresis import HysteresisConfig, MultiHysteresis
from noise.inference.smoother import ProbSmoother, SmoothingConfig
from noise.model.baseline import LABELS, load_bundle
from noise.training.dataset import label_from_path, list_wav_files
from noise.utils.logging import CsvLogger


def _nested(config: dict, key: str, default: dict | None = None) -> dict:
    value = config.get(key, default or {})
    return value if isinstance(value, dict) else default or {}


def _float(config: dict, key: str, default: float) -> float:
    value = config.get(key, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _int(config: dict, key: str, default: int) -> int:
    value = config.get(key, default)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _load_audio(path: Path, *, target_sr: int) -> np.ndarray:
    audio, sr = sf.read(path, dtype="float32", always_2d=False)
    return resample_audio(audio, orig_sr=sr, target_sr=target_sr)


def _build_hysteresis(
    config: dict,
    *,
    hop_s: float,
    initial_state: dict[str, bool] | None = None,
) -> MultiHysteresis:
    hyst_cfg = _nested(config, "hysteresis")
    configs = {}
    for name in LABELS:
        entry = _nested(hyst_cfg, name)
        configs[name] = HysteresisConfig(
            t_on=_float(entry, "t_on", 0.7),
            t_off=_float(entry, "t_off", 0.3),
            n_on_s=_float(entry, "n_on_s", 4.0),
            n_off_s=_float(entry, "n_off_s", 8.0),
            cooldown_s=_float(entry, "cooldown_s", 20.0),
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
    parser.add_argument("--model-path", type=Path, default=Path("models/baseline.joblib"))
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
    parser.add_argument("--require-no-events", action="store_true")
    parser.add_argument("--allow-heuristics", action="store_true")
    args = parser.parse_args()

    bundle = load_bundle(args.model_path)
    target_sr = bundle.config.sample_rate

    config = load_config(args.config) if args.config else {}
    infer_cfg = _nested(config, "inference")
    smooth_cfg = _nested(config, "smoothing")

    window_s = args.window_s if args.window_s is not None else _float(infer_cfg, "window_s", 4.0)
    hop_s = args.hop_s if args.hop_s is not None else _float(infer_cfg, "hop_s", 0.5)

    if window_s <= 0 or hop_s <= 0:
        raise ValueError("window_s and hop_s must be > 0")

    window_len = int(round(window_s * target_sr))
    hop_len = int(round(hop_s * target_sr))
    if window_len <= 0 or hop_len <= 0:
        raise ValueError("window_len/hop_len too small for sample rate")

    smoother_config = SmoothingConfig(
        median_N=_int(smooth_cfg, "median_N", 9),
        ema_tau_s=_float(smooth_cfg, "ema_tau_s", 6.0),
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

    try:
        for path in files:
            label = label_from_path(path, strict=not args.allow_heuristics)
            audio = _load_audio(path, target_sr=target_sr)
            if len(audio) < window_len:
                print(f"{path.name}: skipped (audio shorter than window)")
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
            print(
                f"{path.name}: label={label_str} windows={file_windows} "
                f"events=ac:{file_events['ac']} fridge:{file_events['fridge']}"
            )
            if args.require_no_events and file_event_total > 0:
                any_failed = True

        print(f"\nSummary: files={len(files)} windows={total_windows} events={total_events}")
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
