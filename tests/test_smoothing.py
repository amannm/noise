import unittest

import numpy as np

from noise.inference.smoother import ProbSmoother, SmoothingConfig, ema_alpha


class TestProbSmoother(unittest.TestCase):
    def test_median_filter(self) -> None:
        config = SmoothingConfig(median_N=3, ema_tau_s=1e-6, hop_s=1.0)
        smoother = ProbSmoother(config)

        out1 = smoother.update(0.1)
        out2 = smoother.update(0.9)
        out3 = smoother.update(0.2)

        self.assertAlmostEqual(out1, 0.1, places=5)
        self.assertAlmostEqual(out2, 0.5, places=4)
        self.assertAlmostEqual(out3, 0.2, places=5)

    def test_ema_smoothing(self) -> None:
        config = SmoothingConfig(median_N=1, ema_tau_s=1.0, hop_s=1.0)
        smoother = ProbSmoother(config)
        alpha = ema_alpha(config.hop_s, config.ema_tau_s)

        out0 = smoother.update(0.0)
        self.assertAlmostEqual(out0, 0.0, places=6)

        out1 = smoother.update(1.0)
        expected1 = (1.0 - alpha) * 1.0
        self.assertAlmostEqual(out1, expected1, places=6)

        out2 = smoother.update(1.0)
        expected2 = alpha * expected1 + (1.0 - alpha) * 1.0
        self.assertAlmostEqual(out2, expected2, places=6)

    def test_vector_input(self) -> None:
        config = SmoothingConfig(median_N=1, ema_tau_s=1.0, hop_s=1.0)
        smoother = ProbSmoother(config)

        out = smoother.update(np.array([0.0, 1.0], dtype=np.float32))
        self.assertTrue(np.allclose(out, np.array([0.0, 1.0], dtype=np.float32)))


if __name__ == "__main__":
    unittest.main()
