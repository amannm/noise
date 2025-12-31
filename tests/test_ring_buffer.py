import unittest

import numpy as np

from noise.audio.buffer import RingBuffer


class TestRingBuffer(unittest.TestCase):
    def test_basic_push_and_read(self) -> None:
        ring = RingBuffer(5)
        ring.push(np.array([1, 2, 3], dtype=np.float32))
        self.assertEqual(len(ring), 3)
        self.assertTrue(np.allclose(ring.read_latest(3), [1, 2, 3]))

        ring.push(np.array([4, 5], dtype=np.float32))
        self.assertEqual(len(ring), 5)
        self.assertTrue(np.allclose(ring.read_latest(5), [1, 2, 3, 4, 5]))

    def test_wraparound_and_overflow(self) -> None:
        ring = RingBuffer(5)
        ring.push(np.array([1, 2, 3, 4, 5, 6, 7], dtype=np.float32))
        self.assertTrue(np.allclose(ring.read_latest(5), [3, 4, 5, 6, 7]))

        ring.push(np.array([8, 9], dtype=np.float32))
        self.assertTrue(np.allclose(ring.read_latest(5), [5, 6, 7, 8, 9]))


if __name__ == "__main__":
    unittest.main()
