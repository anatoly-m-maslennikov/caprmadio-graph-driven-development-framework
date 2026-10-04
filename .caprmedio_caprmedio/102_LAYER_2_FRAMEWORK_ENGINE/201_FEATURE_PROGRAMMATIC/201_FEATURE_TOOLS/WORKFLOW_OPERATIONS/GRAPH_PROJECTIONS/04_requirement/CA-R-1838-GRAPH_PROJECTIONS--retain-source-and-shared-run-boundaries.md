---
atom_id: CA-R-1838
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:45 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Boundary"
  depends_on: [Tool, Workflow, Action, Projection, Artifact, Journal, Workflow Run, Step Run]
relations:
  relates_to: [CA-R-1835, CA-R-1836, CA-R-1837, CA-O-133, CA-O-136, CA-R-1720, CA-R-1728]
---
# Summary

Retain source and shared Run boundaries

## Scope

The boundary between graph projection construction, source authority, and accepted shared Run/Journal support.

## Claim

The builders **must** consume the selected Workflow/Step/Action bindings and shared Run/Journal receipts by reference, without creating a second Journal schema or treating a Projection as source authority.

## Details

Each attempt preserves requested graph kind, source frontier, source Atom/Claim/Project Structure identities and revisions, Workflow/Step/Action definition revisions, actual parent/Run references, output destination, and exact effects. A start/terminal recording failure returns a recording blocker/pending receipt reference rather than a completed Run claim; a recording-only recovery reconciles the same event identity/payload and never replays construction. Source correction, vocabulary admission, Relation-kind admission, scope declaration, retry, or regeneration is not authorized by an incomplete or failed build.

Projection consumers, including GRAPH_SERVER and optional UI, are read-only consumers of derived output. No builder, consumer, or output may modify source authority to make a graph pass, use a Projection to establish missing source completeness, or silently substitute current files for the admitted frontier.

### Sources

- CA-O-133 v2, CA-O-134 v2, CA-O-136 v2, CA-O-137 v2.
- CA-R-1387 v8; shared Run/Journal authority is referenced, not redefined.
