import unittest

import numpy as np

from noise.audio.resample import resample_audio


class TestResampleAudio(unittest.TestCase):
    def test_resample_length_and_dtype(self) -> None:
        orig_sr = 44100
        target_sr = 16000
        audio = np.random.randn(orig_sr).astype(np.float32)

        out = resample_audio(audio, orig_sr=orig_sr, target_sr=target_sr)

        self.assertEqual(out.dtype, np.float32)
        self.assertTrue(abs(len(out) - target_sr) <= 2)

    def test_mono_conversion(self) -> None:
        sr = 16000
        stereo = np.stack([np.ones(sr), -np.ones(sr)], axis=1).astype(np.float32)

        out = resample_audio(stereo, orig_sr=sr, target_sr=sr)

        self.assertEqual(out.ndim, 1)
        self.assertEqual(len(out), sr)
        self.assertTrue(np.allclose(out, 0.0))


if __name__ == "__main__":
    unittest.main()
