import unittest
import tempfile
from collections import Counter
from pathlib import Path

import numpy as np
import soundfile as sf

from noise.training.dataset import WindowConfig, WindowedWavDataset, label_from_path


class TestWindowedWavDataset(unittest.TestCase):
    def test_window_counts_and_labels(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            sr = 16000
            duration_s = 2.0
            audio = np.zeros(int(sr * duration_s), dtype=np.float32)

            ac_path = tmp_path / "ac_on.wav"
            off_path = tmp_path / "all_off.wav"
            sf.write(ac_path, audio, sr)
            sf.write(off_path, audio, sr)

            config = WindowConfig(sample_rate=sr, window_s=1.0, hop_s=0.5, strict_labels=True)
            dataset = WindowedWavDataset(tmp_path, config)

            # 2 seconds with 1.0s window and 0.5s hop -> 3 windows per file
            self.assertEqual(len(dataset), 6)

            counts = Counter()
            for window, label, meta in dataset:
                self.assertEqual(len(window), config.window_len())
                expected = label_from_path(Path(meta["file"]), strict=True)
                self.assertEqual(tuple(label.astype(int)), expected)
                counts[Path(meta["file"]).name] += 1

            self.assertEqual(counts["ac_on.wav"], 3)
            self.assertEqual(counts["all_off.wav"], 3)


if __name__ == "__main__":
    unittest.main()
