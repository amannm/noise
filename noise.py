import argparse
import time
from collections import deque

import joblib
import librosa
import numpy as np
import sounddevice as sd
import soundfile as sf
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

APPLIANCES = {
    "ac": {
        "label": "AC",
        "model": "models/ac_detector.joblib",
        "on_wav": "samples/ac_on.wav",
        "off_wav": "samples/all_off.wav",
    },
    "fridge": {
        "label": "FRIDGE",
        "model": "models/fridge_detector.joblib",
        "on_wav": "samples/fridge_on.wav",
        "off_wav": "samples/all_off.wav",
    },
}


def extract_features(y, sr):
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64, fmin=20, fmax=4000)
    log_mel = librosa.power_to_db(mel, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_mel, n_mfcc=13)
    feat = np.concatenate([
        log_mel.mean(axis=1), log_mel.std(axis=1),
        mfcc.mean(axis=1), mfcc.std(axis=1),
    ])
    freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512)) ** 2
    band_low = S[(freqs >= 20) & (freqs <= 200), :].mean()
    band_mid = S[(freqs > 200) & (freqs <= 2000), :].mean()
    ratio = np.array([band_low / (band_mid + 1e-9)])
    return np.concatenate([feat, ratio])


def windows(y, sr, win_s, hop_s):
    win = int(win_s * sr)
    hop = int(hop_s * sr)
    for start in range(0, max(0, len(y) - win + 1), hop):
        yield y[start:start + win]


def build_dataset(path, label, sr, win_s, hop_s):
    y, sr = librosa.load(path, sr=sr, mono=True)
    X, Y = [], []
    for w in windows(y, sr, win_s, hop_s):
        if np.max(np.abs(w)) < 1e-4:
            continue
        X.append(extract_features(w, sr))
        Y.append(label)
    return np.array(X), np.array(Y)


def train(args):
    info = APPLIANCES[args.appliance]
    on_wav = args.on_wav or info["on_wav"]
    off_wav = args.off_wav or info["off_wav"]
    out = args.out or info["model"]
    X_on, y_on = build_dataset(on_wav, 1, sr=args.sr, win_s=args.win_s, hop_s=args.hop_s)
    X_off, y_off = build_dataset(off_wav, 0, sr=args.sr, win_s=args.win_s, hop_s=args.hop_s)
    X = np.vstack([X_on, X_off])
    y = np.concatenate([y_on, y_off])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000)),
    ])
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred, target_names=[f"{info['label']}_OFF", f"{info['label']}_ON"]))
    joblib.dump({"model": model, "sr": args.sr, "win_s": args.win_s, "hop_s": args.hop_s}, out)
    print(f"Saved model to {out}")


def detect(args):
    info = APPLIANCES[args.appliance]
    bundle = joblib.load(args.model or info["model"])
    model = bundle["model"]
    sr = bundle["sr"]
    win_s = bundle["win_s"]
    hop_s = bundle["hop_s"]
    win = int(win_s * sr)
    hop = int(hop_s * sr)
    buf = deque(maxlen=win)
    votes = deque(maxlen=args.votes)
    on_th = args.on_th
    off_th = args.off_th
    state = None

    def callback(indata, frames, time_info, status):
        nonlocal state
        if status:
            print(status)
        x = indata[:, 0]
        for s in x:
            buf.append(float(s))
        if len(buf) == win:
            y = np.array(buf, dtype=np.float32)
            feat = extract_features(y, sr).reshape(1, -1)
            p_on = float(model.predict_proba(feat)[0, 1])
            if state is None:
                vote = 1 if p_on >= 0.5 else 0
            else:
                if state == 0 and p_on >= on_th:
                    vote = 1
                elif state == 1 and p_on <= off_th:
                    vote = 0
                else:
                    vote = state
            votes.append(vote)
            new_state = 1 if (sum(votes) > len(votes) / 2) else 0
            ts = time.strftime("%H:%M:%S")
            if state != new_state:
                state = new_state
                print(f"[{ts}] {info['label']} = {'ON' if state else 'OFF'}  (p_on={p_on:.2f})")
            else:
                print(f"[{ts}] p_on={p_on:.2f}  state={'ON' if state else 'OFF'}", end="\r", flush=True)
            if hop < win:
                y2 = y[hop:]
                buf.clear()
                buf.extend(y2.tolist())

    print("Starting mic stream... (Ctrl+C to stop)")
    with sd.InputStream(channels=1, samplerate=sr, blocksize=hop, callback=callback):
        while True:
            time.sleep(0.5)


def record(args):
    info = APPLIANCES[args.appliance]
    out = args.out or info["on_wav"]
    sr = args.sr
    frames = int(args.seconds * sr)
    print(f"Recording {args.seconds:.0f}s to {out}...")
    audio = sd.rec(frames, samplerate=sr, channels=1, dtype="float32")
    sd.wait()
    sf.write(out, audio, sr, subtype="PCM_16")
    print(f"Saved {out}")


def build_parser():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)

    p_train = sp.add_parser("train")
    p_train.add_argument("appliance", choices=APPLIANCES.keys())
    p_train.add_argument("--on-wav")
    p_train.add_argument("--off-wav")
    p_train.add_argument("--out")
    p_train.add_argument("--sr", type=int, default=16000)
    p_train.add_argument("--win-s", type=float, default=2.0)
    p_train.add_argument("--hop-s", type=float, default=1.0)
    p_train.set_defaults(func=train)

    p_detect = sp.add_parser("detect")
    p_detect.add_argument("appliance", choices=APPLIANCES.keys())
    p_detect.add_argument("--model")
    p_detect.add_argument("--votes", type=int, default=12)
    p_detect.add_argument("--on-th", type=float, default=0.70)
    p_detect.add_argument("--off-th", type=float, default=0.30)
    p_detect.set_defaults(func=detect)

    p_record = sp.add_parser("record")
    p_record.add_argument("appliance", choices=APPLIANCES.keys())
    p_record.add_argument("--out")
    p_record.add_argument("--sr", type=int, default=16000)
    p_record.add_argument("--seconds", type=float, default=180.0)
    p_record.set_defaults(func=record)

    return p


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
