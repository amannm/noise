from __future__ import annotations

import argparse
import json
from collections import deque
from pathlib import Path

import numpy as np
import torch

from src.beats.model import NoiseClassifier, load_beats_checkpoint
from src.beats.preprocess import beats_fbank
from src.infer.hysteresis import Debouncer, Hysteresis
from src.train.eval import derive_state
from src.utils.audio import load_audio, window_waveform


def main() -> None:
    parser = argparse.ArgumentParser(description="Streaming-style inference over audio.")
    parser.add_argument("--audio", type=Path, required=True, help="Audio file to simulate streaming")
    parser.add_argument("--beats-checkpoint", type=Path, required=True)
    parser.add_argument("--model-state", type=Path, required=True)
    parser.add_argument("--window-sec", type=float, default=6.0)
    parser.add_argument("--hop-sec", type=float, default=1.5)
    parser.add_argument("--agg-window-n", type=int, default=7)
    parser.add_argument("--ac-on", type=float, default=0.80)
    parser.add_argument("--ac-off", type=float, default=0.60)
    parser.add_argument("--fr-on", type=float, default=0.75)
    parser.add_argument("--fr-off", type=float, default=0.55)
    parser.add_argument("--debounce-k", type=int, default=2)
    parser.add_argument("--device", type=str, default="cuda" if torch.cuda.is_available() else "cpu")
    args = parser.parse_args()

    beats = load_beats_checkpoint(args.beats_checkpoint)
    model = NoiseClassifier(beats)
    state_dict = torch.load(args.model_state, map_location="cpu")
    model.load_state_dict(state_dict)
    model.to(args.device)
    model.eval()

    waveform, sr = load_audio(args.audio, target_sr=16000, mono=True)
    windows = window_waveform(waveform, sr, args.window_sec, args.hop_sec)

    history = deque(maxlen=args.agg_window_n)
    ac_hyst = Hysteresis(args.ac_on, args.ac_off)
    fr_hyst = Hysteresis(args.fr_on, args.fr_off)
    debouncer = Debouncer(args.debounce_k)

    events = []
    with torch.no_grad():
        for idx, window in enumerate(windows):
            fbank = beats_fbank(window, sample_rate=sr).to(args.device)
            logits = model(fbank)
            p = torch.sigmoid(logits).cpu().numpy()[0]
            history.append((float(p[0]), float(p[1])))

            if len(history) < args.agg_window_n:
                continue

            arr = np.array(history)
            med_ac = float(np.median(arr[:, 0]))
            med_fr = float(np.median(arr[:, 1]))

            ac_on = ac_hyst.update(med_ac)
            fr_on = fr_hyst.update(med_fr)
            state = derive_state(1 if ac_on else 0, 1 if fr_on else 0)
            debounced = debouncer.update(state)
            if debounced is not None:
                events.append(
                    {
                        "window_index": idx,
                        "status": debounced,
                        "p_ac": med_ac,
                        "p_fridge": med_fr,
                    }
                )

    print(json.dumps({"events": events}))


if __name__ == "__main__":
    main()
