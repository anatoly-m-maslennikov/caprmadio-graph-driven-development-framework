#!/usr/bin/env python3
"""Inspect one COMMIT_TRIGGER and return sealed read-only commit context."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCRIPT_PATH = Path(__file__).resolve()
for _parent in SCRIPT_PATH.parents:
    if _parent.name == ".caprmedio_runtime":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio_install":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_tmp" / "cache" / "python")
        break
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

from commit_context_logic import CONTEXT_SCHEMA_VERSION, ContextError, gather_context, repository_root  # noqa: E402


CAPABILITY = "COMMIT_CONTEXT"
TOOL_KIND = "finder"


INPUT_SCHEMA: dict[str, Any] = {
    "schema_version": 1,
    "type": "COMMIT_TRIGGER",
    "required": [
        "schema_version",
        "trigger_id",
        "adapter.id",
        "source_event_id",
        "repository.root",
        "repository.identity",
        "observed_at",
        "before_path|after_path",
        "llm_session.app",
        "llm_session.uuid",
    ],
}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--repository", "--root", type=Path, default=Path("."), help="CAPRMEDIO repository root")
    result.add_argument("--pretty", action="store_true", help="pretty-print the machine result envelope")
    commands = result.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="print Tool capability metadata and input schema")
    run = commands.add_parser("run", help="gather sealed read-only context")
    run.add_argument("--input", required=True, metavar="JSON_FILE_OR_DASH", help="COMMIT_TRIGGER JSON file or - for stdin")
    return result


def read_json(value: str) -> dict[str, Any]:
    try:
        raw = sys.stdin.read() if value == "-" else Path(value).read_text(encoding="utf-8")
    except OSError as error:
        raise ContextError("input_unreadable", "--input must name a readable JSON file or -") from error
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as error:
        raise ContextError("input_json_invalid", "--input must contain one JSON object", line=error.lineno, column=error.colno) from error
    if not isinstance(parsed, dict):
        raise ContextError("input_json_invalid", "--input must contain one JSON object")
    return parsed


def envelope(*, ok: bool, diagnostics: list[dict[str, Any]], result: dict[str, Any] | None = None) -> dict[str, Any]:
    value: dict[str, Any] = {
        "schema_version": 1,
        "tool": {"capability_id": CAPABILITY, "kind": TOOL_KIND},
        "ok": ok,
        "mode": "read-only",
        "diagnostics": diagnostics,
    }
    if result is not None:
        value["result"] = result
    return value


def emit(value: dict[str, Any], *, pretty: bool) -> None:
    print(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2 if pretty else None, separators=None if pretty else (",", ":")))


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "describe":
        emit(
            envelope(
                ok=True,
                diagnostics=[],
                result={
                    "capability_id": CAPABILITY,
                    "kind": TOOL_KIND,
                    "read_only": True,
                    "input_schema": INPUT_SCHEMA,
                    "result_schema_version": CONTEXT_SCHEMA_VERSION,
                },
            ),
            pretty=args.pretty,
        )
        return 0
    try:
        context = gather_context(repository_root(args.repository), read_json(args.input))
    except ContextError as error:
        emit(envelope(ok=False, diagnostics=[error.diagnostic()]), pretty=args.pretty)
        return 2
    emit(envelope(ok=True, diagnostics=[], result={"context": context}), pretty=args.pretty)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
