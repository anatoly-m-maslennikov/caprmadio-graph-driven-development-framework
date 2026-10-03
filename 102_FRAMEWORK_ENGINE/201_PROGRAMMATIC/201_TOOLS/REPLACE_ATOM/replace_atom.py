#!/usr/bin/env python3
"""Describe one deferred Atom-replacement intent without mutation.

Governing authority: CA-R-1041 and CA-M-128. Relation realization is deferred.
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
    required_atom_id,
    required_context,
    run_cli,
)

TOOL_ID = "REPLACE_ATOM"


INPUT_SCHEMA = {
    "predecessor_atom_id": "exact active Atom ID",
    "successor_atom_id": "exact distinct active Atom ID",
    "action_context": "operator-supplied JSON object, preserved unchanged",
}


def build_intent(root: Path, payload: dict[str, object]) -> dict[str, object]:
    """Validate one explicit replacement and produce no relation or mutation."""
    atoms = active_atoms(root)
    predecessor_id = required_atom_id(payload, "predecessor_atom_id")
    successor_id = required_atom_id(payload, "successor_atom_id")
    if predecessor_id == successor_id:
        raise IntentError("replacement-self-reference", "predecessor and successor must be distinct Atom IDs")
    predecessor = active_atom(predecessor_id, atoms)
    successor = active_atom(successor_id, atoms)
    context = required_context(payload)
    intent = {
        "predecessor": carrier(predecessor),
        "successor": carrier(successor),
        "predecessor_transition": "archive",
    }
    return {
        "replacement_intent": intent,
        "commit_pipeline_handoff": deferred_handoff(TOOL_ID, "replace_atom", {
            "predecessor_atom_id": predecessor_id,
            "successor_atom_id": successor_id,
        }, context),
    }


if __name__ == "__main__":
    raise SystemExit(run_cli(TOOL_ID, INPUT_SCHEMA, build_intent))
