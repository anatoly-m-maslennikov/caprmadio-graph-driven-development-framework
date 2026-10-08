---
atom_id: CA-P-1122
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 4
updated_at: "2026-10-08 15:33:32 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1655
    - CA-P-1166
    - CA-P-1123
    - CA-P-1141
---
# Summary

Implement and verify adopted capabilities

## Objective

Implement and verify the first usable cut: Create Atom, Update Atom, Replace Atom, Change Atom Status, the Implementation Workflow, and Build Applicable Methodology. Deliver these through the existing orchestrator and stdio MCP with shared Workflow/Action Journal evidence. Reuse reviewed current Operations, Methods and implementations; do not claim a new source of authority.

Use the reviewed Implementation Workflow: compile applicable active Methods, bind Requirements/Delivery and Evaluations, build E2E/golden mock tests first, implement, then run the selected tests and diagnose failures. Preserve permissions, secrets, currentness, identity, status-model and Journal-evidence checks, including failure and no-op cases.

Scope Unit mutations, Revert, graph builders, standalone advanced Artifact/Journal query delivery, and automatic Release Version or prior-image retirement are deferred from this FIRST CUT. Their existing code, history and status remain preserved; this Plan does not delete them or represent them as done. Existing formal RMED Release gates also remain unchanged: this is neither an N+1 promotion nor a full-release claim.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its child files partition the six workflow paths, orchestrator/stdio MCP compatibility, shared journaling, and the actual loopback Docker HTTP MCP proof owned by CA-P-1757. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Definition of Done

This Plan is not Done unless all six named Workflow paths have current governing sources and passing functional coverage; stdio MCP/orchestrator compatibility and shared Workflow/Action Journal lineage and terminal evidence are preserved; and CA-P-1757 supplies actual authenticated loopback Docker HTTP MCP proof. Required failure/no-op, permission, secret, currentness, identity and status-model checks must remain fail-closed. Deferred capabilities and unchanged formal Release gates are not FIRST CUT completion criteria.
