---
atom_id: CA-P-1118
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
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
version: 1
updated_at: "2026-10-04 06:19:35 +0400"
relations:
  is_decomposition_of:
    - CA-P-1117
  blocks:
    - CA-P-1155
    - CA-P-1119
    - CA-P-1130
---
# Summary

Harvest the thirty-day session evidence

## Objective

Analyze project-relevant session evidence in the fixed thirty-day request window and retain traceable workflow, Step, Action, tool, and prompt candidates without treating assistant proposals as Operator decisions.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Definition of Done

This Plan is not Done if any accessible in-window project session is unprocessed, any unavailable session is hidden instead of linked to a C/Problem, any extracted decision lacks its source and timestamp, or any superseded decision is represented as the current decision. Any required child, remainder, repair or re-review task that is not Done also falsifies completion.
