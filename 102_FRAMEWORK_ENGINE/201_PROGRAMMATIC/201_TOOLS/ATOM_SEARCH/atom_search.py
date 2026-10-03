#!/usr/bin/env python3
"""Search CAPRMEDIO Markdown Atoms."""
from pathlib import Path
import sys

SCRIPT = Path(__file__).resolve()
TOOLS = SCRIPT.parents[1]
for parent in SCRIPT.parents:
    if parent.name in {".caprmedio_install", ".caprmedio_runtime"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
sys.path.insert(0, str(TOOLS))
from atom_operations import cli  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(cli("ATOM_SEARCH"))
