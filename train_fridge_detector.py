import numpy as np
import librosa
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import argparse

def extract_features(y, sr):
    mel = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64, fmin=20, fmax=4000)
    log_mel = librosa.power_to_db(mel, ref=np.max)
    mfcc = librosa.feature.mfcc(S=log_mel, n_mfcc=13)
    feat = np.concatenate([
        log_mel.mean(axis=1), log_mel.std(axis=1),
        mfcc.mean(axis=1), mfcc.std(axis=1),
    ])
    freqs = librosa.fft_frequencies(sr=sr, n_fft=2048)
    S = np.abs(librosa.stft(y, n_fft=2048, hop_length=512))**2
    band_low = S[(freqs >= 20) & (freqs <= 200), :].mean()
    band_mid = S[(freqs > 200) & (freqs <= 2000), :].mean()
    ratio = np.array([band_low / (band_mid + 1e-9)])
    feat = np.concatenate([feat, ratio])
    return feat

def windows(y, sr, win_s=2.0, hop_s=1.0):
    win = int(win_s * sr)
    hop = int(hop_s * sr)
    for start in range(0, max(0, len(y) - win + 1), hop):
        yield y[start:start + win]

def build_dataset(path, label, sr=16000, win_s=2.0, hop_s=1.0):
    y, sr = librosa.load(path, sr=sr, mono=True)
    X, Y = [], []
    for w in windows(y, sr, win_s, hop_s):
        if np.max(np.abs(w)) < 1e-4:
            continue
        X.append(extract_features(w, sr))
        Y.append(label)
    return np.array(X), np.array(Y)

def main(args):
    X_on, y_on = build_dataset(args.on_wav, 1, sr=args.sr, win_s=args.win_s, hop_s=args.hop_s)
    X_off, y_off = build_dataset(args.off_wav, 0, sr=args.sr, win_s=args.win_s, hop_s=args.hop_s)
    X = np.vstack([X_on, X_off])
    y = np.concatenate([y_on, y_off])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=2000))
    ])
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred, target_names=["FRIDGE_OFF", "FRIDGE_ON"]))
    joblib.dump(
        {"model": model, "sr": args.sr, "win_s": args.win_s, "hop_s": args.hop_s},
        args.out
    )
    print(f"Saved model to {args.out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--on_wav", required=True)
    p.add_argument("--off_wav", required=True)
    p.add_argument("--out", default="fridge_detector.joblib")
    p.add_argument("--sr", type=int, default=16000)
    p.add_argument("--win_s", type=float, default=2.0)
    p.add_argument("--hop_s", type=float, default=1.0)
    main(p.parse_args())
