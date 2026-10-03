#!/usr/bin/env python3
"""Register and resolve revisions of native CAPRMEDIO Atoms."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = next(parent for parent in SCRIPT_PATH.parents if (parent / ".git").exists())
sys.pycache_prefix = str(REPOSITORY_ROOT / ".caprmedio_tmp/cache/python")

from artifact_metadata import repository_root
from work_journal import append_record, configured_journal_root, event_record


TIMESTAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}")


@dataclass(frozen=True)
class NativeAtom:
    artifact_id: str
    address: Path
    operation: str
    legacy_artifact_ids: tuple[str, ...] = ()
    legacy_addresses: tuple[Path, ...] = ()


LEGACY_FRAMEWORK_IDENTITY = "CAPR" + "MADIO"


NATIVE_ATOMS = {
    "framework-settings": NativeAtom(
        artifact_id="CAPRMEDIO-FRAMEWORK-SETTINGS",
        address=Path("caprmedio_framework_settings.toml"),
        operation="register_framework_settings_revision",
        legacy_artifact_ids=(f"{LEGACY_FRAMEWORK_IDENTITY}-FRAMEWORK-SETTINGS",),
        legacy_addresses=(
            Path(f"{LEGACY_FRAMEWORK_IDENTITY.lower()}_framework_settings.toml"),
        ),
    ),
}


def carrier_digest(root: Path, atom: NativeAtom) -> str:
    return hashlib.sha256((root / atom.address).read_bytes()).hexdigest()


def revision_records(root: Path, atom: NativeAtom) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted((root / configured_journal_root(root)).glob("src-work-journal-*.ndjson")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"{path}:{line_number}: invalid Work Journal JSON") from exc
            if record.get("kind") != "artifact_revision" or record.get("operation") != atom.operation:
                continue
            if record.get("event") not in {"completed", "recovered"}:
                continue
            accepted_ids = {atom.artifact_id, *atom.legacy_artifact_ids}
            accepted_addresses = {atom.address.as_posix(), *(path.as_posix() for path in atom.legacy_addresses)}
            subjects = record.get("governed_subjects")
            outputs = record.get("produced_outputs")
            if not isinstance(subjects, list) or len(subjects) != 1 or subjects[0] not in accepted_ids:
                raise RuntimeError(f"{path}:{line_number}: invalid native Atom revision binding")
            if not isinstance(outputs, list) or len(outputs) != 1 or outputs[0] not in accepted_addresses:
                raise RuntimeError(f"{path}:{line_number}: invalid native Atom revision binding")
            details = record.get("details")
            if not isinstance(details, dict):
                raise RuntimeError(f"{path}:{line_number}: missing native Atom revision details")
            try:
                version = int(details["version"])
                updated_at = str(details["updated_at"])
                digest = str(details["sha256"])
            except (KeyError, TypeError, ValueError) as exc:
                raise RuntimeError(f"{path}:{line_number}: invalid native Atom revision details") from exc
            if version != len(records) + 1 or not TIMESTAMP.fullmatch(updated_at) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise RuntimeError(f"{path}:{line_number}: invalid native Atom revision sequence")
            records.append({"version": version, "updated_at": updated_at, "sha256": digest})
    return records


def current_reference(root: Path, key: str) -> str:
    atom = NATIVE_ATOMS[key]
    records = revision_records(root, atom)
    if not records:
        raise RuntimeError(f"{atom.artifact_id} has no external Atom revision binding")
    current = records[-1]
    if current["sha256"] != carrier_digest(root, atom):
        raise RuntimeError(f"{atom.artifact_id} does not match its current external revision binding")
    return f"{atom.artifact_id}@{current['version']},{current['updated_at']}"


def register(root: Path, key: str, session_id: str, apply: bool) -> tuple[str, bool]:
    atom = NATIVE_ATOMS[key]
    records = revision_records(root, atom)
    digest = carrier_digest(root, atom)
    if records and records[-1]["sha256"] == digest:
        current = records[-1]
        return f"{atom.artifact_id}@{current['version']},{current['updated_at']}", False
    version = len(records) + 1
    if not apply:
        return f"{atom.artifact_id}@{version},pending", True
    record = event_record(
        root=root,
        event="completed",
        action_id=str(uuid.uuid4()),
        kind="artifact_revision",
        scope="project",
        operation=atom.operation,
        session_id=session_id,
        subjects=[atom.artifact_id],
        outputs=[atom.address.as_posix()],
        preceding_event=None,
        details={"version": str(version), "sha256": digest},
    )
    details = record["details"]
    assert isinstance(details, dict)
    details["updated_at"] = record["occurred_at"]
    reference = f"{atom.artifact_id}@{version},{record['occurred_at']}"
    append_record(root, record)
    return reference, True


def cli(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", choices=sorted(NATIVE_ATOMS))
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args(argv)
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")
    root = repository_root(Path(args.root))
    reference, changed = register(root, args.artifact, args.session_id or "dry-run", args.apply)
    print(f"reference={reference} changed={str(changed).lower()} apply={str(args.apply).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
