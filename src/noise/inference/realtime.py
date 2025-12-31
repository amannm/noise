from __future__ import annotations

import argparse
import queue
import sys
import time
from pathlib import Path

import numpy as np
import sounddevice as sd

from noise.audio.buffer import RingBuffer
from noise.audio.resample import resample_audio
from noise.config.loader import load_config
from noise.inference.hysteresis import HysteresisConfig, MultiHysteresis
from noise.inference.smoother import ProbSmoother, SmoothingConfig
from noise.model.baseline import LABELS, load_bundle
from noise.utils.logging import CsvLogger
from noise.utils.time import local_now_iso


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


def _build_hysteresis(config: dict, hop_s: float) -> MultiHysteresis:
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
    return MultiHysteresis(configs, hop_s=hop_s)


def main() -> None:
    parser = argparse.ArgumentParser(description="Live inference loop for appliance detection.")
    parser.add_argument("--model-path", type=Path, default=Path("models/baseline.joblib"))
    parser.add_argument("--config", type=Path, default=Path("src/noise/config/defaults.yaml"))
    parser.add_argument("--device", type=int, default=None, help="Sounddevice input index")
    parser.add_argument("--input-sr", type=int, default=44100, help="Input device sample rate")
    parser.add_argument("--duration-s", type=float, default=None, help="Stop after N seconds")
    parser.add_argument("--log-probs", type=Path, default=None)
    parser.add_argument("--log-events", type=Path, default=None)
    args = parser.parse_args()

    config = load_config(args.config) if args.config else {}
    audio_cfg = _nested(config, "audio")
    infer_cfg = _nested(config, "inference")
    smooth_cfg = _nested(config, "smoothing")

    bundle = load_bundle(args.model_path)
    target_sr = bundle.config.sample_rate
    cfg_sr = _int(audio_cfg, "sample_rate", target_sr)
    if cfg_sr != target_sr:
        print(f"Warning: config sample_rate {cfg_sr} != model sample_rate {target_sr}. Using model value.")

    window_s = _float(infer_cfg, "window_s", 4.0)
    hop_s = _float(infer_cfg, "hop_s", 0.5)
    ring_buffer_s = _float(infer_cfg, "ring_buffer_s", 6.0)
    chunk_s = _float(infer_cfg, "chunk_s", hop_s)

    if window_s <= 0 or hop_s <= 0 or ring_buffer_s <= 0 or chunk_s <= 0:
        raise ValueError("window_s/hop_s/ring_buffer_s/chunk_s must be > 0")

    window_len = int(round(window_s * target_sr))
    hop_len = int(round(hop_s * target_sr))
    buffer_len = int(round(ring_buffer_s * target_sr))
    chunk_len = int(round(chunk_s * args.input_sr))

    if window_len <= 0 or hop_len <= 0 or buffer_len <= 0:
        raise ValueError("window/hop/buffer length too small")

    smoother = ProbSmoother(
        SmoothingConfig(
            median_N=_int(smooth_cfg, "median_N", 9),
            ema_tau_s=_float(smooth_cfg, "ema_tau_s", 6.0),
            hop_s=hop_s,
        )
    )
    hysteresis = _build_hysteresis(config, hop_s)

    ring = RingBuffer(buffer_len)
    samples_since = 0

    prob_logger = None
    event_logger = None
    if args.log_probs:
        prob_logger = CsvLogger(
            args.log_probs,
            [
                "timestamp",
                "p_ac",
                "p_fridge",
                "p_ac_smooth",
                "p_fridge_smooth",
            ],
        ).open()
    if args.log_events:
        event_logger = CsvLogger(
            args.log_events,
            ["timestamp", "device", "kind", "prob", "step"],
        ).open()

    audio_queue: queue.Queue[np.ndarray] = queue.Queue()

    def _callback(indata: np.ndarray, frames: int, time_info, status) -> None:
        if status:
            print(f"Sounddevice status: {status}", file=sys.stderr)
        audio_queue.put(indata.copy())

    stream = sd.InputStream(
        samplerate=args.input_sr,
        channels=1,
        dtype="float32",
        blocksize=chunk_len,
        device=args.device,
        callback=_callback,
    )

    start_time = time.time()
    try:
        with stream:
            print("Streaming... Press Ctrl+C to stop.")
            while True:
                if args.duration_s is not None and (time.time() - start_time) >= args.duration_s:
                    break
                block = audio_queue.get()
                block = block.reshape(-1)
                if args.input_sr != target_sr:
                    block = resample_audio(block, orig_sr=args.input_sr, target_sr=target_sr)
                ring.push(block)
                samples_since += len(block)

                while samples_since >= hop_len:
                    samples_since -= hop_len
                    if len(ring) < window_len:
                        continue
                    window = ring.read_latest(window_len)
                    probs = bundle.predict_proba_from_audio(window)
                    smooth = smoother.update(probs)
                    smooth_arr = np.asarray(smooth, dtype=np.float32).reshape(-1)

                    now = local_now_iso()
                    if prob_logger is not None:
                        prob_logger.write(
                            {
                                "timestamp": now,
                                "p_ac": float(probs[0]),
                                "p_fridge": float(probs[1]),
                                "p_ac_smooth": float(smooth_arr[0]),
                                "p_fridge_smooth": float(smooth_arr[1]),
                            }
                        )

                    events = hysteresis.update({"ac": float(smooth_arr[0]), "fridge": float(smooth_arr[1])})
                    for event in events:
                        print(f"{now} {event.device} -> {event.kind} (p={event.prob:.3f})")
                        if event_logger is not None:
                            event_logger.write(
                                {
                                    "timestamp": now,
                                    "device": event.device,
                                    "kind": event.kind,
                                    "prob": event.prob,
                                    "step": event.step,
                                }
                            )
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        if prob_logger is not None:
            prob_logger.close()
        if event_logger is not None:
            event_logger.close()


if __name__ == "__main__":
    main()
