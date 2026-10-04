---
atom_id: CA-P-1121
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: PROMPTS
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

Specify and review PROMPTS capabilities

## Objective

Add or update and independently review RMED only for Action/Operator Prompts needed by the thirteen selected Workflows in CA-P-1117 v3, particularly the Implementation Workflow and genuinely agentic or approval-dependent Steps. Reuse existing prompts. Purely programmatic Actions do not require invented agent prompts.

Specify concise input/result handoffs, decision and permission boundaries, Update-to-Replace routing, and Run/Action identifiers needed for Journal linkage. Workflow execution order belongs to reviewed O definitions, not duplicate independent prompt procedures.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Completion result

P1135 authoring and P1136 independent review are Done: current Implementation Workflow and required agentic/approval handoffs have reviewed R1843–46/M326–29/E563–66/D544–46. P1516 owns actual prompt/action delivery and stale binding fixes; programmatic Actions have no invented extra prompt requirement.

### Definition of Done

This Plan is not Done if a prompt actually required by a selected Workflow lacks reviewed RMED and findings disposition, result submission is confused with prompt delivery or Step completion, or identity/permission/Journal handoff boundaries are missing. Required leaves must be Done; unrelated prompts and gratuitous prompts for programmatic Actions are excluded.
