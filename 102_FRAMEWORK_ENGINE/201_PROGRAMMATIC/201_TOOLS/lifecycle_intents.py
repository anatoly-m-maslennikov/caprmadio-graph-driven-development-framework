"""Shared no-mutation lifecycle-intent support for CA-R-1041 and CA-R-1042."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from atom_operations import Atom, ToolError as AtomToolError, resolve_repository, scan_atoms


ATOM_ID = re.compile(r"^CA-[A-Z]+-[0-9]{3,}$")
INACTIVE_LIFECYCLE_SEGMENTS = frozenset({"archive", "drafts", "done", "solved", "canceled", "cancelled"})


class IntentError(RuntimeError):
    """Return one deterministic lifecycle-intent diagnostic."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


def load_payload(source: str) -> dict[str, Any]:
    """Read one JSON request for CA-M-128 or CA-M-129."""
    try:
        raw = sys.stdin.read() if source == "-" else Path(source).read_text(encoding="utf-8")
        payload = json.loads(raw)
    except OSError as error:
        raise IntentError("input-unreadable", "--input must name a readable JSON object") from error
    except json.JSONDecodeError as error:
        raise IntentError("input-json-invalid", "--input must contain one JSON object") from error
    if not isinstance(payload, dict):
        raise IntentError("input-json-invalid", "--input must contain one JSON object")
    return payload


def active_atoms(root: Path) -> dict[str, list[Atom]]:
    """Index active Atom IDs without rejecting unrelated duplicate identities."""
    try:
        atoms = scan_atoms(root)
    except AtomToolError as error:
        raise IntentError(error.code, str(error)) from error
    result: dict[str, list[Atom]] = {}
    for atom in atoms:
        if atom.atom_id is None or any(part.casefold() in INACTIVE_LIFECYCLE_SEGMENTS for part in atom.path.parts):
            continue
        result.setdefault(atom.atom_id, []).append(atom)
    return result


def required_atom_id(payload: Mapping[str, Any], field: str) -> str:
    """Read one canonical Atom ID supplied by the operator."""
    value = payload.get(field)
    if not isinstance(value, str) or not ATOM_ID.fullmatch(value):
        raise IntentError("atom-id-invalid", f"{field} must be an exact Atom ID such as CA-R-1041")
    return value


def required_context(payload: Mapping[str, Any]) -> dict[str, Any]:
    """Preserve explicit action context without giving it graph meaning."""
    value = payload.get("action_context")
    if not isinstance(value, Mapping):
        raise IntentError("action-context-required", "action_context must be a JSON object")
    return dict(value)


def optional_active_ids(payload: Mapping[str, Any], field: str, atoms: Mapping[str, list[Atom]]) -> list[str]:
    """Resolve supplied Atom IDs without inferring omitted participants."""
    value = payload.get(field, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise IntentError("atom-id-list-invalid", f"{field} must be an array of exact Atom IDs")
    if len(value) != len(set(value)):
        raise IntentError("atom-id-list-duplicate", f"{field} must not repeat one Atom ID")
    for item in value:
        if not ATOM_ID.fullmatch(item):
            raise IntentError("active-atom-required", f"{field} contains no active Atom: {item}")
        active_atom(item, atoms)
    return list(value)


def active_atom(atom_id: str, atoms: Mapping[str, list[Atom]]) -> Atom:
    """Return one requested active carrier and reject only its duplicate identity."""
    matches = atoms.get(atom_id, [])
    if not matches:
        raise IntentError("active-atom-required", f"no active Atom has ID {atom_id}")
    if len(matches) != 1:
        raise IntentError("active-atom-id-ambiguous", f"more than one active Atom has ID {atom_id}")
    return matches[0]


def carrier(atom: Atom) -> dict[str, str]:
    """Project the minimal carrier locator needed for a later handoff."""
    assert atom.atom_id is not None
    return {"atom_id": atom.atom_id, "path": atom.relative, "lifecycle": atom.lifecycle}


def deferred_handoff(tool_id: str, operation: str, atom_ids: Mapping[str, Any], action_context: Mapping[str, Any]) -> dict[str, Any]:
    """Describe the explicit non-executable pipeline handoff boundary."""
    return {
        "contract_version": 1,
        "producer": tool_id,
        "operation": operation,
        "atom_ids": dict(atom_ids),
        "action_context": dict(action_context),
        "relation_inference": "not_performed",
        "status": "deferred",
        "reason": "COMMIT_CONTEXT has no admitted lifecycle-intent input contract",
    }


def envelope(tool_id: str, *, ok: bool, mode: str, result: Mapping[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    """Produce the common machine-readable Tool envelope."""
    value: dict[str, Any] = {"schema_version": 1, "tool": {"capability_id": tool_id, "kind": "doer"}, "ok": ok, "mode": mode, "diagnostics": []}
    if error is not None:
        value["diagnostics"] = [{"code": getattr(error, "code", "operation-failed"), "message": str(error)}]
    if result is not None:
        value["result"] = dict(result)
    return value


def run_cli(tool_id: str, input_schema: Mapping[str, Any], build_intent: Callable[[Path, Mapping[str, Any]], dict[str, Any]]) -> int:
    """Run one lifecycle Doer as describe, dry-run, or blocked apply."""
    parser = argparse.ArgumentParser(prog=tool_id.lower().replace("_", "-"))
    parser.add_argument("--repository", default=".", help="CAPRMEDIO repository root")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe", help="print capability and input contract")
    run = commands.add_parser("run", help="validate and describe one lifecycle intent")
    run.add_argument("--input", required=True, metavar="JSON_FILE_OR_DASH")
    run.add_argument("--apply", action="store_true", help="currently blocked before all mutation")
    args = parser.parse_args()
    if args.command == "describe":
        print(json.dumps(envelope(tool_id, ok=True, mode="describe", result={"input_schema": dict(input_schema), "mutation_default": "dry-run", "apply_status": "blocked"}), sort_keys=True, separators=(",", ":")))
        return 0
    try:
        result = build_intent(resolve_repository(args.repository), load_payload(args.input))
        if args.apply:
            error = IntentError("apply-blocked", "lifecycle-intent serialization is not admitted by the commit pipeline")
            print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked", result=result, error=error), sort_keys=True, separators=(",", ":")))
            return 2
        print(json.dumps(envelope(tool_id, ok=True, mode="dry-run", result=result), sort_keys=True, separators=(",", ":")))
        return 0
    except (IntentError, AtomToolError, OSError) as error:
        print(json.dumps(envelope(tool_id, ok=False, mode="apply-blocked" if args.apply else "dry-run", error=error), sort_keys=True, separators=(",", ":")))
        return 2
