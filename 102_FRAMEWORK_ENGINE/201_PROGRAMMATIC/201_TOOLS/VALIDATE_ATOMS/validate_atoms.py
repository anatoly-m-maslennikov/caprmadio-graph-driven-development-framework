#!/usr/bin/env python3
"""Validate selected Atom carriers without changing inputs."""

import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True

from validate_atoms_workers.contracts import parse_request, request_error_report, validate_report  # noqa: E402
from validate_atoms_workers.read_io import protected, open_regular  # noqa: E402
from validate_atoms_workers.runtime import execute  # noqa: E402


def main() -> int:
    try:
        if len(sys.argv) != 3 or sys.argv[1] != "--input":
            raise ValueError("Expected --input path or --input -")
        if sys.argv[2] == "-":
            raw = sys.stdin.buffer.read(8 * 1024 * 1024 + 1)
        else:
            path = Path(sys.argv[2]).absolute()
            if protected(path):
                raise ValueError("Protected input.")
            import os

            with os.fdopen(open_regular(path), "rb") as stream:
                raw = stream.read(8 * 1024 * 1024 + 1)
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError("Request exceeds host input ceiling.")
        request = parse_request(raw.decode("utf-8"))
    except OSError, ValueError, UnicodeError, RecursionError:
        report = request_error_report()
    else:
        report = execute(request.model_dump(mode="json", exclude_unset=True))
    report = validate_report(report)
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return {"valid": 0, "invalid": 1, "incomplete": 2, "error": 3}[report["result"]]


if __name__ == "__main__":
    raise SystemExit(main())
