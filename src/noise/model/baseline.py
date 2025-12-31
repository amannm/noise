from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from noise.audio.featurize import log_mel_spectrogram

LABELS = ("ac", "fridge")


@dataclass(frozen=True)
class BaselineFeatureConfig:
    sample_rate: int = 16000
    n_mels: int = 128
    win_ms: float = 25.0
    hop_ms: float = 10.0
    include_std: bool = True

    def feature_dim(self) -> int:
        return self.n_mels * (2 if self.include_std else 1)


@dataclass
class BaselineBundle:
    config: BaselineFeatureConfig
    estimator: Pipeline

    @property
    def sample_rate(self) -> int:
        return self.config.sample_rate

    def predict_proba(self, features: np.ndarray) -> np.ndarray:
        probs = self.estimator.predict_proba(features)
        if isinstance(probs, list):
            positive = np.stack([item[:, 1] for item in probs], axis=1)
        else:
            positive = probs
        return positive.astype(np.float32, copy=False)

    def predict_proba_from_audio(self, audio: np.ndarray) -> np.ndarray:
        features = extract_features(audio, self.config)
        probs = self.predict_proba(features[None, :])
        return probs[0]


def build_estimator(random_state: int | None = 0) -> Pipeline:
    base = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        solver="liblinear",
        random_state=random_state,
    )
    model = MultiOutputClassifier(base)
    return Pipeline(
        [
            ("scaler", StandardScaler()),
            ("clf", model),
        ]
    )


def summarize_log_mel(log_mel: np.ndarray, *, include_std: bool = True) -> np.ndarray:
    if log_mel.ndim != 2:
        raise ValueError(f"Expected log-mel shape (n_mels, frames), got {log_mel.shape}")
    mean = np.mean(log_mel, axis=1)
    if not include_std:
        return mean.astype(np.float32, copy=False)
    std = np.std(log_mel, axis=1)
    return np.concatenate([mean, std], axis=0).astype(np.float32, copy=False)


def extract_features(audio: np.ndarray, config: BaselineFeatureConfig) -> np.ndarray:
    log_mel = log_mel_spectrogram(
        audio,
        sample_rate=config.sample_rate,
        n_mels=config.n_mels,
        win_ms=config.win_ms,
        hop_ms=config.hop_ms,
    )
    return summarize_log_mel(log_mel, include_std=config.include_std)


def extract_feature_matrix(
    audios: Iterable[np.ndarray],
    config: BaselineFeatureConfig,
) -> np.ndarray:
    features = [extract_features(audio, config) for audio in audios]
    if not features:
        return np.zeros((0, config.feature_dim()), dtype=np.float32)
    return np.stack(features, axis=0)


def save_bundle(bundle: BaselineBundle, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(bundle, path)


def load_bundle(path: Path) -> BaselineBundle:
    bundle = joblib.load(path)
    if not isinstance(bundle, BaselineBundle):
        raise TypeError(f"Unexpected bundle type at {path}: {type(bundle)}")
    return bundle
