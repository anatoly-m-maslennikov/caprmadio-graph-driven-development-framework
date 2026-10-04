---
atom_id: CA-P-1120
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Session-derived operational capability delivery"
  depends_on:
    - "Operations"
    - "Implementation"
version: 3
updated_at: "2026-10-04 19:29:30 +0000"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1162
    - CA-P-1163
    - CA-P-1122
    - CA-P-1137
    - CA-P-1138
---
# Summary

Specify and review PROGRAMMATIC capabilities

## Objective

Add or update RMED only for the PROGRAMMATIC capabilities required by CA-P-1117 v3's thirteen Workflows, at their narrowest owning Scope Units. Cover Create/Update/Replace/Change Status Atom; Create/Rename/Move/Remove Scope Unit; Implementation Workflow; Revert Changes; and the Entities Graph, Terms Graph and Applicable Methodology builders. Archive is a Change Status shortcut.

Specify every Workflow Run and Action Run's durable Journal evidence, including standalone, nested, failed, canceled and no-op paths. Reuse one authoritative Events Journal and derived log views. Specify source traceability, source conflict reporting, Operator-approved corrections, rebuild behavior, and incomplete-result handling for the three Projections. Preserve identity/history and Operator control at mutation boundaries. Obtain independent RMED review; do not expand this task into unrelated Tool delivery.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Completion result

P1133 authoring and P1134 independent review are Done: selected shared support, lifecycle, Project Structure, reversal, two graph builders, compiler, MCP and D521v3 queue contract have exact functional RMED. Findings P1501–1506 are corrected/accepted. P1510–1515/P1517–1519 carry implementation; no code or Docker pass is claimed here.

### Definition of Done

This Plan is not Done if any required PROGRAMMATIC path for the thirteen selected Workflows lacks current RMED, functional acceptance criteria and independent review, including complete Workflow/Action Run journaling and all three Projection builders. R/M/E/D responsibilities and local tiers must be correct, findings disposed and required leaves Done; unrelated implementations are excluded.
