from __future__ import annotations

import argparse
import json
import sys
import threading
import time
from collections import deque
from pathlib import Path
from typing import Iterable, Optional

import numpy as np
import sounddevice as sd
import torch
import tomllib
import torchaudio.functional as F

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.beats.model import NoiseClassifier, load_beats_checkpoint
from src.beats.preprocess import beats_fbank
from src.infer.hysteresis import Debouncer, Hysteresis
from src.train.eval import derive_state
from src.utils.audio import load_audio


DEFAULTS = {
    "input_sr": 44100,
    "window_sec": 6.0,
    "hop_sec": 1.5,
    "agg_window_n": 7,
    "ac_on": 0.80,
    "ac_off": 0.60,
    "fr_on": 0.75,
    "fr_off": 0.55,
    "debounce_k": 2,
    "sd_device": None,
    "max_lag_sec": 30.0,
}


def load_config(path: Path) -> dict:
    if not path.exists():
        return {}
    data = tomllib.loads(path.read_text())
    return data


def list_devices(json_output: bool) -> None:
    devices = sd.query_devices()
    default_input, default_output = sd.default.device
    if json_output:
        payload = {
            "default_input": default_input,
            "default_output": default_output,
            "devices": devices,
        }
        print(json.dumps(payload))
        return

    print(f"Default input device: {default_input}")
    print(f"Default output device: {default_output}")
    for idx, dev in enumerate(devices):
        direction = []
        if dev.get("max_input_channels", 0) > 0:
            direction.append("in")
        if dev.get("max_output_channels", 0) > 0:
            direction.append("out")
        label = "/".join(direction) if direction else "-"
        print(f"[{idx}] {label} {dev.get('name')}")


class LiveProcessor:
    def __init__(self, args, model: NoiseClassifier) -> None:
        self.args = args
        self.model = model
        self.window_samples = int(round(args.window_sec * args.input_sr))
        self.history = deque(maxlen=args.agg_window_n)
        self.ac_hyst = Hysteresis(args.ac_on, args.ac_off)
        self.fr_hyst = Hysteresis(args.fr_on, args.fr_off)
        self.debouncer = Debouncer(args.debounce_k)
        self.audio_buffer: deque[np.ndarray] = deque()
        self.buffered = 0
        self.infer_index = 0

    def process_block(self, block: np.ndarray, source: Optional[str] = None) -> Optional[dict]:
        self.audio_buffer.append(block)
        self.buffered += len(block)

        while self.buffered > self.window_samples and self.audio_buffer:
            removed = self.audio_buffer.popleft()
            self.buffered -= len(removed)

        if self.buffered < self.window_samples:
            return None

        window = np.concatenate(list(self.audio_buffer))[-self.window_samples :]
        t0 = time.perf_counter()
        window_tensor = torch.from_numpy(window).to(torch.float32).unsqueeze(0)
        if self.args.input_sr != 16000:
            window_tensor = F.resample(
                window_tensor, orig_freq=self.args.input_sr, new_freq=16000
            )
        fbank = beats_fbank(window_tensor, sample_rate=16000).to(self.args.device)
        with torch.no_grad():
            logits = self.model(fbank)
            p = torch.sigmoid(logits).cpu().numpy()[0]
        self.history.append((float(p[0]), float(p[1])))

        if len(self.history) < self.args.agg_window_n:
            return None

        arr = np.array(self.history)
        med_ac = float(np.median(arr[:, 0]))
        med_fr = float(np.median(arr[:, 1]))

        ac_on = self.ac_hyst.update(med_ac)
        fr_on = self.fr_hyst.update(med_fr)
        state = derive_state(1 if ac_on else 0, 1 if fr_on else 0)
        debounced = self.debouncer.update(state)
        process_ms = (time.perf_counter() - t0) * 1000.0

        payload = {
            "timestamp": time.time(),
            "status": state,
            "p_ac": med_ac,
            "p_fridge": med_fr,
            "window_index": self.infer_index,
            "process_ms": process_ms,
        }
        if source is not None:
            payload["source"] = source
        if debounced is not None:
            payload["debounced_status"] = debounced

        self.infer_index += 1
        return payload


def iter_blocks_from_file(path: Path, input_sr: int, hop_samples: int) -> Iterable[np.ndarray]:
    waveform, _ = load_audio(path, target_sr=input_sr, mono=True)
    samples = waveform.squeeze(0).cpu().numpy()
    for start in range(0, len(samples) - hop_samples + 1, hop_samples):
        yield samples[start : start + hop_samples]


def main() -> None:
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument(
        "--config",
        type=Path,
        default=Path("src/config/live.toml"),
        help="Path to live config TOML",
    )
    pre.add_argument("--list-devices", action="store_true", help="List audio devices")
    pre.add_argument(
        "--list-devices-json", action="store_true", help="List devices as JSON"
    )
    pre_args, _ = pre.parse_known_args()
    if pre_args.list_devices or pre_args.list_devices_json:
        list_devices(pre_args.list_devices_json)
        return
    cfg = load_config(pre_args.config)

    parser = argparse.ArgumentParser(description="Live mic inference.", parents=[pre])
    parser.add_argument("--beats-checkpoint", type=Path, required=True)
    parser.add_argument("--model-state", type=Path, required=True)
    parser.add_argument(
        "--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu"
    )
    parser.add_argument("--input-sr", type=int, default=cfg.get("input_sr", DEFAULTS["input_sr"]))
    parser.add_argument("--window-sec", type=float, default=cfg.get("window_sec", DEFAULTS["window_sec"]))
    parser.add_argument("--hop-sec", type=float, default=cfg.get("hop_sec", DEFAULTS["hop_sec"]))
    parser.add_argument("--agg-window-n", type=int, default=cfg.get("agg_window_n", DEFAULTS["agg_window_n"]))
    parser.add_argument("--ac-on", type=float, default=cfg.get("ac_on", DEFAULTS["ac_on"]))
    parser.add_argument("--ac-off", type=float, default=cfg.get("ac_off", DEFAULTS["ac_off"]))
    parser.add_argument("--fr-on", type=float, default=cfg.get("fr_on", DEFAULTS["fr_on"]))
    parser.add_argument("--fr-off", type=float, default=cfg.get("fr_off", DEFAULTS["fr_off"]))
    parser.add_argument("--debounce-k", type=int, default=cfg.get("debounce_k", DEFAULTS["debounce_k"]))
    parser.add_argument("--max-lag-sec", type=float, default=cfg.get("max_lag_sec", DEFAULTS["max_lag_sec"]))
    parser.add_argument(
        "--sd-device",
        type=str,
        default=cfg.get("sd_device", DEFAULTS["sd_device"]),
        help="Sounddevice input device",
    )
    parser.add_argument(
        "--only-changes",
        action="store_true",
        help="Emit output only when debounced status changes",
    )
    parser.add_argument(
        "--log-jsonl",
        type=Path,
        default=None,
        help="Append output JSON lines to file",
    )
    parser.add_argument(
        "--dry-run",
        type=Path,
        default=None,
        help="Replay an audio file or directory through streaming logic",
    )
    args = parser.parse_args()

    if isinstance(args.sd_device, str):
        if args.sd_device.strip() == "":
            args.sd_device = None
        elif args.sd_device.isdigit():
            args.sd_device = int(args.sd_device)

    beats = load_beats_checkpoint(args.beats_checkpoint)
    model = NoiseClassifier(beats)
    state_dict = torch.load(args.model_state, map_location="cpu")
    model.load_state_dict(state_dict)
    model.to(args.device)
    model.eval()

    window_samples = int(round(args.window_sec * args.input_sr))
    hop_samples = int(round(args.hop_sec * args.input_sr))
    if hop_samples <= 0 or window_samples <= 0:
        raise ValueError("Invalid window/hop settings")

    log_file = None
    if args.log_jsonl is not None:
        args.log_jsonl.parent.mkdir(parents=True, exist_ok=True)
        log_file = args.log_jsonl.open("a")

    def emit(payload: dict) -> None:
        serialized = json.dumps(payload)
        print(serialized, flush=True)
        if log_file is not None:
            log_file.write(serialized + "\n")
            log_file.flush()

    stream_kwargs = {
        "samplerate": args.input_sr,
        "channels": 1,
        "dtype": "float32",
        "blocksize": hop_samples,
    }
    if args.sd_device is not None:
        stream_kwargs["device"] = args.sd_device

    try:
        if args.dry_run is not None:
            dry_path = args.dry_run
            if not dry_path.exists():
                raise FileNotFoundError(f"Dry-run path not found: {dry_path}")
            if dry_path.is_dir():
                audio_files = sorted(
                    [
                        p
                        for p in dry_path.iterdir()
                        if p.suffix.lower() in {".m4a", ".wav", ".flac"}
                    ]
                )
            else:
                audio_files = [dry_path]
            if not audio_files:
                raise ValueError(f"No audio files found in {dry_path}")

            for audio_path in audio_files:
                processor = LiveProcessor(args, model)
                blocks = iter_blocks_from_file(audio_path, args.input_sr, hop_samples)
                for block in blocks:
                    payload = processor.process_block(block, source=str(audio_path))
                    if payload is None:
                        continue
                    if args.only_changes and "debounced_status" not in payload:
                        continue
                    emit(payload)
        else:
            processor = LiveProcessor(args, model)
            block_queue: deque[np.ndarray] = deque()
            queue_samples = 0
            queue_lock = threading.Condition()
            callback_error: list[str] = []

            max_queue_samples = None
            if args.max_lag_sec is not None and args.max_lag_sec > 0:
                max_queue_samples = int(round(args.max_lag_sec * args.input_sr))

            def callback(indata, frames, time_info, status) -> None:
                nonlocal queue_samples
                with queue_lock:
                    if status.input_overflow:
                        callback_error.append("Audio input overflowed in callback")
                        queue_lock.notify()
                        raise sd.CallbackStop
                    block = indata[:, 0].copy()
                    block_queue.append(block)
                    queue_samples += len(block)
                    if max_queue_samples is not None and queue_samples > max_queue_samples:
                        callback_error.append("Audio processing lag exceeded max_lag_sec")
                        queue_lock.notify()
                        raise sd.CallbackStop
                    queue_lock.notify()

            with sd.InputStream(callback=callback, **stream_kwargs):
                while True:
                    with queue_lock:
                        while not block_queue and not callback_error:
                            queue_lock.wait()
                        if callback_error:
                            raise RuntimeError(callback_error[0])
                        block = block_queue.popleft()
                        queue_samples -= len(block)

                    payload = processor.process_block(block)
                    if payload is None:
                        continue
                    if args.only_changes and "debounced_status" not in payload:
                        continue
                    emit(payload)
    except KeyboardInterrupt:
        return
    finally:
        if log_file is not None:
            log_file.close()


if __name__ == "__main__":
    main()
