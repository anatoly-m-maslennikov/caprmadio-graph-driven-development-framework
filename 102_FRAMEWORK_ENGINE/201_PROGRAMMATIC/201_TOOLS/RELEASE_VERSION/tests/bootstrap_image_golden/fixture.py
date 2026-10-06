"""Retained bootstrap-image fixture; payloads are data, never discovered tests."""

from __future__ import annotations

import json
from pathlib import Path


PAYLOADS = Path(__file__).with_name("payloads.json")


def materialize(root: Path) -> None:
    for relative, text in json.loads(PAYLOADS.read_text(encoding="utf-8")).items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
    compiled = root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
    for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
        (compiled / role).mkdir(parents=True, exist_ok=True)
