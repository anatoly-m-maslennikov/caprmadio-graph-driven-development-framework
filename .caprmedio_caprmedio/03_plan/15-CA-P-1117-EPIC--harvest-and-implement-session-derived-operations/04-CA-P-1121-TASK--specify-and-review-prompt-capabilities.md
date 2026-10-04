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
    - CA-P-1162
    - CA-P-1163
    - CA-P-1122
    - CA-P-1137
    - CA-P-1138
---
# Summary

Specify and review PROMPTS capabilities

## Objective

Add or update current RMED for the adopted Action Prompts and Operator Prompts, including interactive workflow Steps and the main session's decision/result handoff, and obtain independent subagent review.

### Work decomposition

This is a composite task, not a fifteen-minute executable leaf. Its initial child files partition the work; add more <=15-minute one-file subtasks for remaining evidence, capability slices, reviews or failures. Roll-up effort depends on the frozen inventory. Inherit CA-P-1117 execution controls and its autonomous-confidence threshold; do not copy or override inherited values.

Before marking this task Done, verify full-stage coverage and update the next dependent task(s) from actual results. A blocked child remains unfinished, has a C/Problem, and does not authorize bypassing this parent's gate.

## Details

### Definition of Done

This Plan is not Done if any adopted prompt capability lacks current governing RMED, interactive result submission is confused with prompt delivery or Step completion, or any prompt lacks independent subagent review and findings dispositions. Any required child, remainder, repair or re-review task that is not Done also falsifies completion.
