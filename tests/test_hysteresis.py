import unittest

from noise.inference.hysteresis import HysteresisConfig, HysteresisState


class TestHysteresisState(unittest.TestCase):
    def test_on_transition_after_persistence(self) -> None:
        config = HysteresisConfig(
            t_on=0.7,
            t_off=0.3,
            n_on_s=2.0,
            n_off_s=2.0,
            cooldown_s=0.0,
        )
        state = HysteresisState(config, hop_s=0.5)
        sequence = [0.1, 0.8, 0.8, 0.8, 0.8]

        events = [state.update(prob) for prob in sequence]
        self.assertTrue(state.is_on)
        self.assertEqual(events.index(True), 4)

    def test_off_transition_after_persistence(self) -> None:
        config = HysteresisConfig(
            t_on=0.7,
            t_off=0.3,
            n_on_s=1.0,
            n_off_s=1.5,
            cooldown_s=0.0,
        )
        state = HysteresisState(config, hop_s=0.5, initial_on=True)
        sequence = [0.2, 0.2, 0.2]

        events = [state.update(prob) for prob in sequence]
        self.assertFalse(state.is_on)
        self.assertEqual(events[-1], False)

    def test_cooldown_blocks_immediate_toggle(self) -> None:
        config = HysteresisConfig(
            t_on=0.7,
            t_off=0.3,
            n_on_s=1.0,
            n_off_s=1.0,
            cooldown_s=2.0,
        )
        state = HysteresisState(config, hop_s=1.0)

        ev1 = state.update(0.8)
        ev2 = state.update(0.0)
        ev3 = state.update(0.0)

        self.assertEqual(ev1, True)
        self.assertIsNone(ev2)
        self.assertEqual(ev3, False)


if __name__ == "__main__":
    unittest.main()
