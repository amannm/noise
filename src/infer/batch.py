from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import torch

from src.beats.model import NoiseClassifier, load_beats_checkpoint
from src.beats.preprocess import beats_fbank
from src.train.eval import derive_state
from src.utils.audio import load_audio, window_waveform


def load_thresholds(path: Path) -> tuple[float, float]:
    if not path.exists():
        raise FileNotFoundError(f"Threshold file not found: {path}")
    content = path.read_text().strip().splitlines()
    values = {}
    for line in content:
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, val = line.split(":", 1)
        values[key.strip()] = float(val.strip())
    return float(values.get("t_ac", 0.75)), float(values.get("t_fr", 0.70))


def main() -> None:
    parser = argparse.ArgumentParser(description="Batch inference for a single audio file.")
    parser.add_argument("--audio", type=Path, required=True)
    parser.add_argument("--beats-checkpoint", type=Path, required=True)
    parser.add_argument("--model-state", type=Path, required=True)
    parser.add_argument("--thresholds", type=Path, default=Path("src/config/thresholds.yaml"))
    parser.add_argument("--window-sec", type=float, default=6.0)
    parser.add_argument("--hop-sec", type=float, default=1.5)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    t_ac, t_fr = load_thresholds(args.thresholds)

    beats = load_beats_checkpoint(args.beats_checkpoint)
    model = NoiseClassifier(beats)
    state_dict = torch.load(args.model_state, map_location="cpu")
    model.load_state_dict(state_dict)
    model.to(args.device)
    model.eval()

    waveform, sr = load_audio(args.audio, target_sr=16000, mono=True)
    windows = window_waveform(waveform, sr, args.window_sec, args.hop_sec)

    probs = []
    with torch.no_grad():
        for window in windows:
            fbank = beats_fbank(window, sample_rate=sr).to(args.device)
            logits = model(fbank)
            p = torch.sigmoid(logits).cpu().numpy()[0]
            probs.append((float(p[0]), float(p[1])))

    if not probs:
        raise ValueError("No windows generated for inference")

    arr = np.array(probs)
    med_ac = float(np.median(arr[:, 0]))
    med_fr = float(np.median(arr[:, 1]))

    pred_ac = 1 if med_ac >= t_ac else 0
    pred_fr = 1 if med_fr >= t_fr else 0
    status = derive_state(pred_ac, pred_fr)

    output = {
        "status": status,
        "p_ac": med_ac,
        "p_fridge": med_fr,
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
