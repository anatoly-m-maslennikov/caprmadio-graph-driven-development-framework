#!/usr/bin/env python3
"""Plan one sealed relation rebind under CA-R-1049 and CA-M-156.

The manager makes the entire one-carrier decision from supplied facts.  Its
workers own JSON, filesystem, frontmatter, and registry I/O.  Journal and Git
actions deliberately remain outside this Doer.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path


TOOL_DIRECTORY = Path(__file__).resolve().parent
if str(TOOL_DIRECTORY) not in sys.path:
    sys.path.insert(0, str(TOOL_DIRECTORY))

from rebind_atom_relations_workers.frontmatter import (
    assert_declared_delta,
    rebind_relations,
    split_document,
    update_revision,
    validate_revision,
)
from rebind_atom_relations_workers.models import Plan, RebindError, Request, State


def plan_relation_rebinding(request: Request, state: State) -> Plan:
    """Return one fully checked relation-only update plan without filesystem I/O."""
    _validate_digest(state.source_bytes, request.expected_sha256)
    frontmatter, body = split_document(state.source_bytes)
    validate_revision(frontmatter, request)
    rewritten = rebind_relations(frontmatter, request, state.active_target_ids)
    updated = update_revision(rewritten, request)
    assert_declared_delta(frontmatter, updated, body, request)
    output = ("---\n" + updated.rstrip("\n") + "\n---\n" + body).encode("utf-8")
    return Plan(output=output, receipt=_receipt(request, state, output))


def _validate_digest(source: bytes, expected: str) -> None:
    """Fail before planning when the sealed source bytes have changed."""
    if hashlib.sha256(source).hexdigest() != expected:
        raise RebindError("source-digest-mismatch", "source SHA-256 differs from expected_source_sha256")


def _receipt(request: Request, state: State, output: bytes) -> dict[str, object]:
    """Render the deterministic no-Journal, no-Git result contract."""
    return {
        "operation": "REBIND_ATOM_RELATIONS",
        "action_type": "UPDATE",
        "source": {
            "path": state.source_relative,
            "sha256": request.expected_sha256,
            "version": request.expected_version,
        },
        "result": {
            "path": state.source_relative,
            "sha256": hashlib.sha256(output).hexdigest(),
            "version": request.expected_version + 1,
        },
        "relations": {
            "rewritten": _rewritten(request),
            "removed": _removed(request),
        },
        "frontmatter": {
            "updated": ["updated_at", "version"],
            "preserved": "all undeclared fields and relation targets",
        },
        "journal": {"status": "not_performed"},
        "git": {"status": "not_performed"},
    }


def _rewritten(request: Request) -> list[dict[str, str]]:
    """Sort requested rewrites independently from input object ordering."""
    rows = [
        {"relation": relation, "from": old, "to": new}
        for relation, targets in request.rewrite_map.items()
        for old, new in targets.items()
    ]
    return sorted(rows, key=lambda row: (row["relation"], row["from"]))


def _removed(request: Request) -> list[dict[str, str]]:
    """Sort requested removals independently from input object ordering."""
    rows = [
        {"relation": relation, "target": target}
        for relation, targets in request.removal_map.items()
        for target in targets
    ]
    return sorted(rows, key=lambda row: (row["relation"], row["target"]))


if __name__ == "__main__":
    from rebind_atom_relations_workers.runtime import cli

    raise SystemExit(cli())
