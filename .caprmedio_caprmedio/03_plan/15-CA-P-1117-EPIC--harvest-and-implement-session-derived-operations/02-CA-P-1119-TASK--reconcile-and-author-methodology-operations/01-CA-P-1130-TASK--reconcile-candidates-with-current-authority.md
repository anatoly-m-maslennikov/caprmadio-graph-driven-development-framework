---
atom_id: CA-P-1130
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: METHODOLOGY_SOURCES
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
updated_at: "2026-10-04 06:29:05 +0400"
relations:
  is_decomposition_of:
    - CA-P-1119
  blocks:
    - CA-P-1156
    - CA-P-1131
---
# Summary

Reconcile candidates with current authority

## Objective

The assigned AI Agent must complete one bounded work packet for reconcile candidates with current authority, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Select at most five harvest candidates. Read their active Project and methodology sources, including current terminology for Processes, Actions, and workflow Steps. Latest explicit Operator input wins over older input; higher Principles remain governing. Cross-map older active harvest/migration Plans instead of duplicating their work.

### Required output

A decision-to-existing/new-Operation mapping with source revisions, semantic deduplication, required RMED ownership, accepted disposition, and linked Concerns. Assign reusable, project-independent Operations to CORE_META_MODEL and caprmedio-specific Operations to PROJECT_CONFIGURATION, with exact source carriers and a destination rationale. Split the remainder into additional leaves which block authoring of their corresponding operations.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

## Details

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
