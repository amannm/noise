from __future__ import annotations

import argparse
import json

import sounddevice as sd


def main() -> None:
    parser = argparse.ArgumentParser(description="List available audio input devices.")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    devices = sd.query_devices()
    default_input, default_output = sd.default.device

    if args.json:
        payload = {
            "default_input": default_input,
            "default_output": default_output,
            "devices": devices,
        }
        print(json.dumps(payload))
        return

    print(f"Default input device: {default_input}")
    print(f"Default output device: {default_output}")
    for idx, dev in enumerate(devices):
        direction = []
        if dev.get("max_input_channels", 0) > 0:
            direction.append("in")
        if dev.get("max_output_channels", 0) > 0:
            direction.append("out")
        label = "/".join(direction) if direction else "-"
        print(f"[{idx}] {label} {dev.get('name')}")


if __name__ == "__main__":
    main()
