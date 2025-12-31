from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.utils.audio import probe_audio

FILENAME_RE = re.compile(
    r"^ac-(on|off)-fridge-(on|off)-(day|night)\.m4a$"
)


def parse_labels(filename: str) -> dict[str, object]:
    match = FILENAME_RE.match(filename)
    if not match:
        raise ValueError(
            f"Filename does not match expected pattern: {filename}"
        )
    ac_state, fridge_state, daypart = match.groups()
    ac = 1 if ac_state == "on" else 0
    fridge = 1 if fridge_state == "on" else 0
    if ac == 1:
        state = "ac-on"
    elif fridge == 1:
        state = "fridge-on"
    else:
        state = "both-off"
    return {
        "ac": ac,
        "fridge": fridge,
        "state": state,
        "daypart": daypart,
    }


def build_manifest(samples_dir: Path) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for path in sorted(samples_dir.glob("*.m4a")):
        labels = parse_labels(path.name)
        info = probe_audio(path)
        duration_sec = info.duration_sec
        sample_rate = info.sample_rate
        recording_id = path.stem
        rows.append(
            {
                "path": str(path.as_posix()),
                "duration_sec": duration_sec,
                "sample_rate": sample_rate,
                "ac": labels["ac"],
                "fridge": labels["fridge"],
                "state": labels["state"],
                "daypart": labels["daypart"],
                "recording_id": recording_id,
            }
        )
    if not rows:
        raise ValueError(f"No .m4a files found in {samples_dir}")
    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build file-level manifest from samples directory."
    )
    parser.add_argument(
        "--samples-dir",
        type=Path,
        default=Path("samples"),
        help="Directory containing .m4a files",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/manifests/files.csv"),
        help="Output CSV path",
    )
    args = parser.parse_args()

    df = build_manifest(args.samples_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
