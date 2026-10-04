---
atom_id: CA-P-1135
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
version: 2
updated_at: "2026-10-04 18:48:47 +0000"
relations:
  is_decomposition_of:
    - CA-P-1121
  blocks:
    - CA-P-1161
    - CA-P-1136
---
# Summary

Author one PROMPTS RMED slice

## Objective

The assigned AI Agent must complete one bounded work packet for author one prompts rmed slice, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Bind one adopted prompt family to exact ACTION_PROMPTS or OPERATOR_PROMPTS carriers. Preserve Integrated/Isolated boundaries under current authority. An interactive Step returns prompt plus context to the main session, which decides or delegates and submits the decision/result in a subsequent MCP call; prompt delivery alone is not completion.

### Required output

Current prompt RMED and source Operation linkage, input/result/context contracts, confidence/HITL behavior, and exact implementation ownership. Keep prompts out of a ballooning main system prompt; add leaves for remaining prompt families.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

## Details

### Saved authoring completion

P1490 supplied fifteen current PROMPTS R/M/E/D carriers with complete source pins and seven-Step delivery boundaries. Both authoring leaves P1160/P1490 are saved Done. P1500 independently reviews that exact packet before prompt delivery. Its recorded 17 stale delivered source bindings remain an implementation gate, not a runtime pass.

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
