import numpy as np
import sounddevice as sd
import joblib
import librosa
from collections import deque
import time

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

def main():
    bundle = joblib.load("ac_detector.joblib")
    model = bundle["model"]
    sr = bundle["sr"]
    win_s = bundle["win_s"]
    hop_s = bundle["hop_s"]

    win = int(win_s * sr)
    hop = int(hop_s * sr)

    buf = deque(maxlen=win)
    votes = deque(maxlen=12)  # ~12 seconds if hop_s=1.0

    # Hysteresis thresholds
    on_th = 0.70
    off_th = 0.30
    state = None  # unknown at start

    def callback(indata, frames, time_info, status):
        nonlocal state
        if status:
            print(status)
        x = indata[:, 0]
        for s in x:
            buf.append(float(s))

        # Run inference every time buffer is full and we have a new hop
        # (simple approach: check length and only evaluate when enough new samples arrive)
        # We'll use a crude timer: evaluate when len(buf)==win and every callback we have enough frames
        if len(buf) == win:
            y = np.array(buf, dtype=np.float32)
            feat = extract_features(y, sr).reshape(1, -1)
            p_on = float(model.predict_proba(feat)[0, 1])

            # Convert probability to vote with hysteresis
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

            if state != new_state:
                state = new_state
                print(f"[{time.strftime('%H:%M:%S')}] AC = {'ON' if state else 'OFF'}  (p_on={p_on:.2f})")
            else:
                print(f"[{time.strftime('%H:%M:%S')}] p_on={p_on:.2f}  state={'ON' if state else 'OFF'}", end="\r")

            # Drop hop samples from left by rebuilding deque:
            if hop < win:
                y2 = y[hop:]
                buf.clear()
                buf.extend(y2.tolist())

    print("Starting mic stream... (Ctrl+C to stop)")
    with sd.InputStream(channels=1, samplerate=sr, blocksize=hop, callback=callback):
        while True:
            time.sleep(0.5)

if __name__ == "__main__":
    # mic permissions: macOS will prompt the first time.
    import sys
    try:
        import sounddevice
    except ImportError:
        pass
    main()