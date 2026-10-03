"""Filesystem and registry boundaries for the CA-R-1049 relation-rebinding Doer."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tomllib
from pathlib import Path
from typing import Any

from .contract import ATOM_ID, load_request
from .frontmatter import fields, split_document
from .models import Plan, RebindError, Request, State

TOOLS_ROOT = Path(__file__).resolve().parents[2]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from project_runtime import atomic_tempfile  # noqa: E402
CONTROL = ".caprmedio"
INACTIVE = frozenset({"archive", "drafts", "done", "solved", "canceled", "cancelled"})
ROLE = re.compile(r"^0[1-9]_[a-z0-9_]+$")
FILENAME_ID = re.compile(r"^(CA-[CAPRMEDO]-[0-9]{3,})(?:-[A-Z][A-Z0-9_]*)*--")
def _repository(value: str) -> Path:
    """Resolve the repository that contains the requested control-plane path."""
    candidate = Path(value).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise RebindError("repository-not-found", "cannot resolve a Git repository")
def collect_state(root: Path, request: Request) -> State:
    """Collect source and only the registry facts required by requested rewrites."""
    source = _source(root, request.source_path)
    active_ids = frozenset()
    if request.rewrite_map:
        _validate_rewrite_relations(request, _relation_registry(root))
        active_ids = _active_target_ids(root)
    return State(root, source, source.relative_to(root).as_posix(), source.read_bytes(), active_ids)
def apply_plan(state: State, plan: Plan, request: Request) -> None:
    """Atomically replace only the sealed source carrier after a final digest check."""
    current = state.source.read_bytes()
    if hashlib.sha256(current).hexdigest() != request.expected_sha256:
        raise RebindError("source-digest-mismatch", "source changed after the plan was sealed")
    _atomic_write(state.source, plan.output)
    if hashlib.sha256(state.source.read_bytes()).hexdigest() != plan.receipt["result"]["sha256"]:
        raise RebindError("result-digest-mismatch", "applied carrier differs from sealed result")
def _source(root: Path, value: str) -> Path:
    """Resolve one existing active Markdown Atom below the control plane."""
    source = (root / value).resolve()
    control = (root / CONTROL).resolve()
    try:
        relative = source.relative_to(control)
    except ValueError as error:
        raise RebindError("path-invalid", "source path must remain below .caprmedio") from error
    if not source.is_file() or source.suffix != ".md" or _inactive(relative) or not _role_path(relative):
        raise RebindError("source-not-active-atom", "source must be one active Markdown Atom carrier")
    split_document(source.read_bytes())
    return source


def _relation_registry(root: Path) -> dict[str, dict[str, str]]:
    """Load direct and inverse relation metadata from the canonical TOML dictionary."""
    path = _tool_root() / "caprmedio_relation_types.toml"
    try:
        payload = tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        raise RebindError("relation-registry-invalid", "cannot load caprmedio relation-type dictionary") from error
    rows = payload.get("relation_types")
    if not isinstance(rows, list):
        raise RebindError("relation-registry-invalid", "relation-type dictionary has no relation_types array")
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise RebindError("relation-registry-invalid", "relation-type dictionary has an invalid row")
        direct, inverse = row.get("direct_name"), row.get("inverse_name")
        if not isinstance(direct, str) or not isinstance(inverse, str) or direct in result or inverse in result:
            raise RebindError("relation-registry-invalid", "relation names must be globally unique")
        result[direct] = {"kind": "direct", **{key: str(row.get(key, "")) for key in ("status", "declaration_carrier")}}
        result[inverse] = {"kind": "inverse", "status": str(row.get("status", "")), "declaration_carrier": ""}
    return result


def _validate_rewrite_relations(request: Request, registry: dict[str, dict[str, str]]) -> None:
    """Admit only active direct Atom-carrier relation names for rewrite actions."""
    for relation in sorted(request.rewrite_map):
        metadata = registry.get(relation)
        if metadata is None:
            raise RebindError("relation-unregistered", f"relation is not registered: {relation}")
        if metadata["kind"] == "inverse":
            raise RebindError("relation-inverse", f"inverse relation cannot be stored: {relation}")
        if metadata["status"] != "active":
            raise RebindError("relation-deferred", f"relation is not active: {relation}")
        if metadata["declaration_carrier"] != "atom_carrier":
            raise RebindError("relation-carrier-invalid", f"relation cannot be stored in an Atom carrier: {relation}")


def _active_target_ids(root: Path) -> frozenset[str]:
    """Return IDs with exactly one syntactically valid active Atom carrier each."""
    found: dict[str, int] = {}
    control = root / CONTROL
    for path in control.rglob("*.md"):
        relative = path.relative_to(control)
        atom_id = _candidate_id(path, relative)
        if atom_id:
            found[atom_id] = found.get(atom_id, 0) + 1
    return frozenset(atom_id for atom_id, count in found.items() if count == 1)


def _candidate_id(path: Path, relative: Path) -> str | None:
    """Accept one active CCE Markdown Atom whose ID derives from its filename."""
    match = FILENAME_ID.match(path.name)
    if not match or _inactive(relative) or not _role_path(relative) or not ATOM_ID.fullmatch(match.group(1)):
        return None
    try:
        frontmatter, _ = split_document(path.read_bytes())
        blocks = fields(frontmatter)
    except (OSError, RebindError):
        return None
    return match.group(1) if "version" in blocks else None


def _inactive(relative: Path) -> bool:
    """Recognize all non-active lifecycle folders without inferring another state."""
    return any(part.casefold() in INACTIVE for part in relative.parts)


def _role_path(relative: Path) -> bool:
    """Require a conventional content-role directory before treating a file as an Atom."""
    return any(ROLE.fullmatch(part) for part in relative.parts[:-1])


def _tool_root() -> Path:
    """Locate the installed or canonical TOOLS directory containing the registry."""
    return Path(__file__).resolve().parents[2]


def _atomic_write(path: Path, value: bytes) -> None:
    """Write through Project Temporary State and replace without backups or copies."""
    descriptor, temporary_name = atomic_tempfile(path, "rebind_atom_relations")
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(value)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        temporary.unlink(missing_ok=True)
        raise


def _envelope(*, ok: bool, mode: str, result: dict[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    """Return the shared machine-readable CLI envelope."""
    diagnostics = [] if error is None else [{"code": getattr(error, "code", "rebind-failed"), "message": str(error)}]
    return {"schema_version": 1, "tool": {"capability_id": "REBIND_ATOM_RELATIONS", "kind": "doer"}, "ok": ok, "mode": mode, "diagnostics": diagnostics, "result": result or {}}


def _describe() -> dict[str, Any]:
    """Describe the explicit, one-carrier, relation-only mutation contract."""
    return {
        "input_schema": {
            "input": "one exact JSON request",
            "mutation_default": "dry-run",
            "apply": "one sealed active source carrier only",
            "frontmatter_mutations": ["version", "updated_at", "declared relation targets"],
            "rewrite_relations": "registered active direct atom_carrier relations only",
            "removal_relations": "exact one-occurrence cleanup; semantic admission is not required",
        },
        "governing_atoms": ["CA-R-1049", "CA-M-156", "CA-E-252", "CA-D-413"],
        "journal": "not_performed",
        "git": "not_performed",
    }


def cli(argv: list[str] | None = None) -> int:
    """Run describe or one dry-run/apply request for CA-R-1049."""
    parser = argparse.ArgumentParser(prog="rebind-atom-relations")
    parser.add_argument("--repository", default=".")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("describe")
    run = commands.add_parser("run")
    run.add_argument("--input", required=True, metavar="JSON_FILE_OR_DASH")
    run.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    if args.command == "describe":
        print(json.dumps(_envelope(ok=True, mode="read-only", result=_describe()), sort_keys=True, separators=(",", ":")))
        return 0
    mode = "apply" if args.apply else "dry-run"
    try:
        request = load_request(args.input)
        state = collect_state(_repository(args.repository), request)
        from rebind_atom_relations import plan_relation_rebinding
        plan = plan_relation_rebinding(request, state)
        if args.apply:
            apply_plan(state, plan, request)
        print(json.dumps(_envelope(ok=True, mode=mode, result={"receipt": plan.receipt}), sort_keys=True, separators=(",", ":")))
        return 0
    except (RebindError, OSError) as error:
        print(json.dumps(_envelope(ok=False, mode=mode, error=error), sort_keys=True, separators=(",", ":")))
        return 2
