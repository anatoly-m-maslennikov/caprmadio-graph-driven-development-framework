#!/usr/bin/env python3
"""Describe one deferred Concern-closure intent without mutation.

Governing authority: CA-R-1042 and CA-M-129. Relation realization is deferred.
"""

from __future__ import annotations

from pathlib import Path
import sys

SCRIPT = Path(__file__).resolve()
TOOLS = SCRIPT.parents[1]
for parent in SCRIPT.parents:
    if parent.name in {".caprmedio_install", ".caprmedio_runtime"}:
        sys.pycache_prefix = str(parent.parent / ".caprmedio_tmp/cache/python")
        break
sys.path.insert(0, str(TOOLS))

from lifecycle_intents import (  # noqa: E402
    IntentError,
    active_atom,
    active_atoms,
    carrier,
    deferred_handoff,
    optional_active_ids,
    required_atom_id,
    required_context,
    run_cli,
)

TOOL_ID = "CLOSE_ATOM"
INPUT_SCHEMA = {
    "concern_atom_id": "exact active Concern Atom ID",
    "terminal_disposition": "nonempty operator-supplied closure disposition",
    "resolver_atom_ids": "optional exact active Atom-ID array",
    "subject_atom_ids": "optional exact active Atom-ID array",
    "action_context": "operator-supplied JSON object, preserved unchanged",
}


def terminal_disposition(payload: dict[str, object]) -> str:
    """Require a supplied closure meaning without interpreting its content."""
    value = payload.get("terminal_disposition")
    if not isinstance(value, str) or not value.strip():
        raise IntentError("terminal-disposition-required", "terminal_disposition must be a nonempty string")
    return value


def build_intent(root: Path, payload: dict[str, object]) -> dict[str, object]:
    """Validate supplied closure participants without inferring their relations."""
    atoms = active_atoms(root)
    concern_id = required_atom_id(payload, "concern_atom_id")
    concern = active_atom(concern_id, atoms)
    if concern.role_directory != "01_concern":
        raise IntentError("concern-atom-required", f"concern_atom_id is not a Concern: {concern_id}")
    resolver_ids = optional_active_ids(payload, "resolver_atom_ids", atoms)
    subject_ids = optional_active_ids(payload, "subject_atom_ids", atoms)
    context = required_context(payload)
    intent = {
        "concern": carrier(concern),
        "target_lifecycle": "solved",
        "terminal_disposition": terminal_disposition(payload),
        "resolver_atom_ids": resolver_ids,
        "subject_atom_ids": subject_ids,
    }
    return {
        "closure_intent": intent,
        "commit_pipeline_handoff": deferred_handoff(TOOL_ID, "close_atom", {
            "concern_atom_id": concern_id,
            "resolver_atom_ids": resolver_ids,
            "subject_atom_ids": subject_ids,
        }, context),
    }


if __name__ == "__main__":
    raise SystemExit(run_cli(TOOL_ID, INPUT_SCHEMA, build_intent))
