#!/usr/bin/env python3
"""Plan one sealed CAPRMEDIO Atom identity migration.

Governing authority: CA-R-1048 and CA-M-155.  This pure manager accepts one
observed carrier state plus one explicit request; filesystem I/O stays in its
workers.  Journal and Git handoff remain deliberately outside this Doer.
"""

from __future__ import annotations

import hashlib
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any


TOOL_DIRECTORY = Path(__file__).resolve().parent
if str(TOOL_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(TOOL_DIRECTORY))

from migrate_atom_identity_workers.frontmatter import edit_fields, edit_relations, fields, scalar, split_document, validate_revision
from migrate_atom_identity_workers.models import MigrationError, Plan, Request, State


ROLE_DIRECTORY = {"01_concern": "C", "02_analysis": "A", "03_plan": "P", "04_requirement": "R", "05_method": "M", "06_evaluation": "E", "07_delivery": "D", "08_implementation": "I", "09_operations": "O"}


def plan_identity_migration(request: Request, state: State) -> Plan:
    """Build exactly one fully checked carrier move-and-update plan, without I/O."""
    _validate_carrier(request, state)
    frontmatter, body = split_document(state.source_bytes)
    _validate_preconditions(request, state, frontmatter)
    rewritten = edit_relations(frontmatter, request.relation_rewrite_map, request.relation_removal_map)
    updated = edit_fields(rewritten, request.frontmatter_removals, request.frontmatter_updates)
    output = ("---\n" + updated.rstrip("\n") + "\n---\n" + body).encode("utf-8")
    receipt = _receipt(request, state, output)
    return Plan(output, receipt)


def _validate_carrier(request: Request, state: State) -> None:
    if state.source.name != request.source_filename:
        raise MigrationError("source-filename-mismatch", "source filename differs from filename_tokens.source_filename")
    expected_name = "-".join(request.destination_prefix) + "--" + request.summary + ".md"
    if state.destination.name != expected_name:
        raise MigrationError("destination-filename-mismatch", "destination filename differs from exact filename tokens")
    role = request.new_atom_id.split("-")[1]
    if (
        state.source_role != state.destination_role
        or ROLE_DIRECTORY.get(state.destination_role) != role
    ):
        raise MigrationError("content-role-mismatch", "identity migration must preserve one matching content-role directory")
    if request.new_atom_id in state.new_identity_collisions:
        raise MigrationError("atom-id-collision", "new_atom_id already occurs in another carrier")


def _validate_preconditions(request: Request, state: State, frontmatter: str) -> None:
    digest = hashlib.sha256(state.source_bytes).hexdigest()
    if digest != request.expected_sha256:
        raise MigrationError("source-digest-mismatch", "source SHA-256 differs from expected_source_sha256")
    validate_revision(frontmatter, request.expected_version, request.frontmatter_removals, request.frontmatter_updates)
    blocks = fields(frontmatter)
    current = scalar(blocks["atom_id"][2], "atom_id") if "atom_id" in blocks else None
    prefix = state.source.stem.partition("--")[0]
    if request.classification == "identityless_legacy":
        if current or prefix.startswith("CA-"):
            raise MigrationError("identity-classification-mismatch", "identityless_legacy source already declares an identity")
        return
    assert request.approved_old_identity is not None
    known = request.approved_old_identity
    if current != known and not (prefix == known or prefix.startswith(known + "-")):
        raise MigrationError("old-identity-mismatch", "approved_old_identity does not match the source carrier")
    if request.classification == "duplicate_id_repair" and not state.old_identity_collisions:
        raise MigrationError("duplicate-id-unconfirmed", "duplicate_id_repair requires another carrier with approved_old_identity")


def _receipt(request: Request, state: State, output: bytes) -> dict[str, Any]:
    relation_changes = _relation_changes(request)
    movement = "MOVE+UPDATE" if state.source != state.destination else "UPDATE"
    return {
        "operation": "MIGRATE_ATOM_IDENTITY",
        "classification": request.classification,
        "action_type": movement,
        "source": {"path": state.source_relative, "sha256": request.expected_sha256, "version": request.expected_version, "approved_identity": request.approved_old_identity},
        "result": {"path": state.destination_relative, "sha256": hashlib.sha256(output).hexdigest(), "version": request.expected_version + 1, "atom_id": request.new_atom_id},
        "frontmatter": {"removed": sorted(request.frontmatter_removals), "updated": sorted(request.frontmatter_updates)},
        "relations": relation_changes,
        "journal": {"status": "not_performed"},
        "git": {"status": "not_performed"},
        "handoff": {"status": "ready", "next_tools": ["APPEND_CHANGE_RECORDS", "COMMIT_CHANGE_SET"]},
    }


def _relation_changes(request: Request) -> dict[str, list[dict[str, str]]]:
    rewrites = [
        {"relation": relation, "from": old, "to": new}
        for relation, mapping in request.relation_rewrite_map.items() for old, new in mapping.items()
    ]
    removals = [
        {"relation": relation, "target": target}
        for relation, targets in request.relation_removal_map.items() for target in targets
    ]
    return {"rewritten": sorted(rewrites, key=lambda item: (item["relation"], item["from"])), "removed": sorted(removals, key=lambda item: (item["relation"], item["target"]))}


if __name__ == "__main__":
    from migrate_atom_identity_workers.runtime import cli

    raise SystemExit(cli())
