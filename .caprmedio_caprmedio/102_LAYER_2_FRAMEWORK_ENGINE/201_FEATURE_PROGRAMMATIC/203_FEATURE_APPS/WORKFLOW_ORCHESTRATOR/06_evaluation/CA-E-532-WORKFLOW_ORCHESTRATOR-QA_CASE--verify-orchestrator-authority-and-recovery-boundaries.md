---
atom_id: CA-E-532
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 02:57:00 +0400"
subjects:
  governs: "Workflow Run/permissions"
  depends_on: [Workflow, Action, Atom, Operator, Journal, Implementation, Tool]
relations:
  relates_to: [CA-R-1522, CA-R-1523, CA-R-1524, CA-O-104]
---
# Summary

Verify orchestrator authority and recovery boundaries

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

the Evaluation **must** verify rejection of orchestration requests **or** Agent output outside declared authority.

## Details

- reject unsupported Workflows, traversal, symlinks, protected paths, unknown fields, stale input **and** conflicting duplicate Run requests.
- check phases cannot modify source Atoms; allow_fixes=false preserves source bytes.
- reject Agent-assigned successor IDs, undelegated Summary changes, low confidence, incomplete checks **and** invalid report fields.
- **with** allow_replacements=true **and** fix permission, verify the new unreused ID, successor Version **`=1`**, archived predecessor, confirmed lifecycle receipts **and** full report bindings.
- verify recovery **after** partial publication reuses the reserved ID **without** a new Agent dispatch; stale source, changed Scope Unit **or** conflicting destination bytes interrupt rather than overwrite.
- record uncertainty **after** dispatch intent with no accepted output, **without** silently rerunning the Agent.
- verify failure **and** interruption remain observable through status, shared Journal **and** full reports.
