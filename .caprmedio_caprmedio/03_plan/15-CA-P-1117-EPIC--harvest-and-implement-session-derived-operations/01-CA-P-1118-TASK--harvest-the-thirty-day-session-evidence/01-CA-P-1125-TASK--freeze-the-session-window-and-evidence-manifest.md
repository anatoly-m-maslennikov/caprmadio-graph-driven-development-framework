---
atom_id: CA-P-1125
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
updated_at: "2026-10-04 06:36:25 +0400"
relations:
  is_decomposition_of:
    - CA-P-1118
  blocks:
    - CA-P-1151
    - CA-P-1152
    - CA-P-1153
    - CA-P-1154
    - CA-P-1126
    - CA-P-1127
    - CA-P-1128
    - CA-P-1129
---
# Summary

Freeze the session window and evidence manifest

## Objective

The assigned AI Agent must complete one bounded work packet for freeze the session window and evidence manifest, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Use the request window [2026-09-04 05:54:15 +0400, 2026-10-04 05:54:15 +0400). Read the current Operator Goal and all active Project Principles before discovery. Inspect project-linked session metadata through available local/app read interfaces; do not scan denied paths, credentials, or unrelated project content. Compare existing Harvest Epic 014 and other active Plans for overlapping ownership.

### Required output

A timestamped corpus manifest with session identifiers, relevance reasons, retrieval sources/cursors, known gaps, date partitions, current authority revisions, and reusable existing work. If enumeration exceeds fifteen minutes, create additional bounded manifest subtasks before declaring the harvest stage complete.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

## Details

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
