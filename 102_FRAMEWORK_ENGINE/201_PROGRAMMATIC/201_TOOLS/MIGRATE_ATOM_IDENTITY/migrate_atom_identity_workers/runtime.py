"""Filesystem boundary and CLI for the CA-R-1048 identity-migration Doer."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from .contract import ATOM_ID, load_request
from .models import MigrationError, Plan, Request, State

TOOLS_ROOT = Path(__file__).resolve().parents[2]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from project_runtime import atomic_tempfile  # noqa: E402


CONTROL = ".caprmedio"
INACTIVE = frozenset({"archive", "drafts", "done", "solved", "canceled", "cancelled"})
ROLE = re.compile(r"^0[1-9]_[a-z0-9_]+$")


def _repository(value: str) -> Path:
    candidate = Path(value).expanduser().resolve()
    for root in (candidate, *candidate.parents):
        if (root / ".git").exists():
            return root
    raise MigrationError("repository-not-found", "cannot resolve a Git repository")


def _carrier(root: Path, value: str, *, source: bool) -> tuple[Path, str, str]:
    path = (root / value).resolve()
    control = (root / CONTROL).resolve()
    try:
        relative = path.relative_to(control)
    except ValueError as error:
        raise MigrationError("path-invalid", "carrier path must remain below .caprmedio") from error
    if path.suffix != ".md" or any(part.casefold() in INACTIVE for part in relative.parts):
        raise MigrationError("carrier-invalid", "identity migration accepts active Markdown Atom carriers only")
    roles = [part for part in relative.parts[:-1] if ROLE.fullmatch(part)]
    if not roles or (source and not path.is_file()) or (not source and not path.parent.is_dir()):
        raise MigrationError("carrier-invalid", "carrier requires an active content-role location and existing parent")
    return path, path.relative_to(root).as_posix(), roles[-1]


def _identity_matches(path: Path, identity: str) -> bool:
    prefix = path.stem.partition("--")[0]
    if prefix == identity or prefix.startswith(identity + "-"):
        return True
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    return bool(re.search(rf"(?m)^atom_id:\s*[\"]?{re.escape(identity)}[\"]?\s*$", text))


def _collisions(root: Path, identity: str, source: Path) -> tuple[str, ...]:
    control = root / CONTROL
    matches = [path.relative_to(root).as_posix() for path in sorted(control.rglob("*.md")) if path != source and _identity_matches(path, identity)]
    return tuple(matches)


def collect_state(root: Path, request: Request) -> State:
    """Collect bounded source/destination facts; no carrier is modified here."""
    source, source_relative, source_role = _carrier(root, request.source_path, source=True)
    destination, destination_relative, destination_role = _carrier(root, request.destination_path, source=False)
    if destination.exists() and destination != source:
        raise MigrationError("destination-collision", "destination carrier already exists")
    return State(
        root, source, destination, source_relative, destination_relative, source.read_bytes(), source_role,
        destination_role, _collisions(root, request.new_atom_id, source),
        _collisions(root, request.approved_old_identity, source) if request.approved_old_identity else (),
    )


def _atomic_write(path: Path, value: bytes) -> None:
    descriptor, temporary_name = atomic_tempfile(path, "migrate_atom_identity")
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


def apply_plan(state: State, plan: Plan) -> None:
    """Apply one planned move-and-update with rollback on a failed source unlink."""
    if state.source == state.destination:
        _atomic_write(state.source, plan.output)
        return
    _atomic_write(state.destination, plan.output)
    if hashlib.sha256(state.destination.read_bytes()).hexdigest() != plan.receipt["result"]["sha256"]:
        state.destination.unlink(missing_ok=True)
        raise MigrationError("result-digest-mismatch", "destination digest differs from sealed plan")
    try:
        state.source.unlink()
    except BaseException:
        state.destination.unlink(missing_ok=True)
        raise


def _envelope(*, ok: bool, mode: str, result: dict[str, Any] | None = None, error: BaseException | None = None) -> dict[str, Any]:
    diagnostics = [] if error is None else [{"code": getattr(error, "code", "migration-failed"), "message": str(error)}]
    return {"schema_version": 1, "tool": {"capability_id": "MIGRATE_ATOM_IDENTITY", "kind": "doer"}, "ok": ok, "mode": mode, "diagnostics": diagnostics, "result": result or {}}


def _describe() -> dict[str, Any]:
    return {"input_schema": {"input": "one exact JSON request", "mutation_default": "dry-run", "apply": "one sealed source carrier only", "derived_frontmatter": "atom_id and tier are removal-only when present"}, "governing_atoms": ["CA-R-1048", "CA-M-155", "CA-E-251", "CA-D-412"], "journal": "not_performed", "git": "not_performed"}


def cli(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="migrate-atom-identity")
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
        from migrate_atom_identity import plan_identity_migration
        plan = plan_identity_migration(request, state)
        if args.apply:
            apply_plan(state, plan)
        print(json.dumps(_envelope(ok=True, mode=mode, result={"receipt": plan.receipt}), sort_keys=True, separators=(",", ":")))
        return 0
    except (MigrationError, OSError) as error:
        print(json.dumps(_envelope(ok=False, mode=mode, error=error), sort_keys=True, separators=(",", ":")))
        return 2
