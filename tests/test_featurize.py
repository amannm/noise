import unittest

import numpy as np

from noise.audio.featurize import log_mel_spectrogram


class TestLogMelSpectrogram(unittest.TestCase):
    def test_log_mel_shape_and_dtype(self) -> None:
        sr = 16000
        duration_s = 1.0
        t = np.linspace(0.0, duration_s, int(sr * duration_s), endpoint=False)
        audio = 0.1 * np.sin(2 * np.pi * 440.0 * t).astype(np.float32)

        mel = log_mel_spectrogram(audio, sample_rate=sr, n_mels=64)

        self.assertEqual(mel.dtype, np.float32)
        self.assertEqual(mel.shape[0], 64)
        self.assertGreater(mel.shape[1], 0)


if __name__ == "__main__":
    unittest.main()
