from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


class CsvLogger:
    """Append-only CSV logger with header management."""

    def __init__(self, path: Path, fieldnames: Iterable[str]) -> None:
        self.path = path
        self.fieldnames = list(fieldnames)
        self._file = None
        self._writer: csv.DictWriter | None = None

    def open(self) -> "CsvLogger":
        self.path.parent.mkdir(parents=True, exist_ok=True)
        file_exists = self.path.exists() and self.path.stat().st_size > 0
        self._file = self.path.open("a", newline="", encoding="utf-8")
        self._writer = csv.DictWriter(self._file, fieldnames=self.fieldnames)
        if not file_exists:
            self._writer.writeheader()
            self._file.flush()
        return self

    def write(self, row: dict[str, object]) -> None:
        if self._writer is None:
            raise RuntimeError("CsvLogger is not open")
        self._writer.writerow(row)
        if self._file is not None:
            self._file.flush()

    def close(self) -> None:
        if self._file is not None:
            self._file.close()
        self._file = None
        self._writer = None

    def __enter__(self) -> "CsvLogger":
        return self.open()

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()
