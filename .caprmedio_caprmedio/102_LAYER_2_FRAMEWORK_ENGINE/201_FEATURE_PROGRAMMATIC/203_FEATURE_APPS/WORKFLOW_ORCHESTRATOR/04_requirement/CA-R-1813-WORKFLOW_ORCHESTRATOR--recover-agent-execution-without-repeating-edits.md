---
atom_id: CA-R-1813
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-03 20:12:24 +0400"
subjects:
  governs: "Workflow Run/recovery"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Recover Agent execution without repeating edits

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

WORKFLOW_ORCHESTRATOR **must** recover interrupted execution **without** replaying a completed Atom edit.

## Details

- use a stable dispatch identity for each selected Atom **and** phase.
- retain accepted Agent output before source effects. admit reports through the existing coordination Tool.
- before applying an accepted edit, compare the current source with the saved before **and** after hashes: apply the before case, acknowledge the after case, **and** block any other case.
- a worker loss **during** unacknowledged Agent execution leaves execution uncertain; require explicit recovery rather than silently launching another effectful session.
- transport retry does **not** grant semantic repair permission. replay recorded completed outputs rather than rerunning completed checks.
