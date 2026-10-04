---
atom_id: CA-P-1131
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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
version: 3
updated_at: "2026-10-04 14:39:01 +0000"
relations:
  is_decomposition_of:
    - CA-P-1119
  blocks:
    - CA-P-1157
    - CA-P-1132
---
# Summary

Author one methodology operation slice

## Objective

The assigned AI Agent must complete one bounded work packet for author one methodology operation slice, using the stated inputs and ownership restrictions, and record the required output without extending this leaf's scope.

### Inputs and bounded ownership

Bind one reconciled Action or Workflow and at most three directly associated Step/Action source Atoms with exact target carriers and governing revisions. An accepted Action-only contribution does not require inventing a duplicate Workflow. Use the reconciled destination: CORE_META_MODEL for reusable, project-independent Operations; PROJECT_CONFIGURATION for caprmedio-specific Operations. Reuse existing Operations where equivalent; preserve governed archives and required Journal provenance under the Epic's Operator-approved save policy. Write only authoritative methodology sources, not generated projections.

For the separately retained Carrier repairs, bind layout-only packets of at most four existing Operations, plus the directly identified CA-M-301 supporting-heading repair in one packet. These packets preserve Summary, meaning and Version; refresh Updated At and apply CA-D-479's registered body boundaries and CA-D-482's explicit resolved target. This is repair of the reconciled source frontier, not semantic reauthoring of reused Operations. Keep the independent review limit of four changed Operations per leaf.

### Current admitted authoring frontier

CA-A-1064 independently accepts the optional completed-work handoff assessment. CA-A-1085 accepts evaluator calibration and legacy-evidence/provisional-RMED preparation. CA-A-1086 accepts read-only scoped-choice applicability assessment. Completed CA-P-1372 / CA-A-1087 v2 independently accepts the single coalesced F07/F08/F10 prepared-result conformance assessment. All five reusable accepted contributions target CORE_META_MODEL. No automatic repair, rollout, refactoring, approval or Workflow invocation follows from these definitions.

The CA-P-1130 family and independent-review gates remain binding. This update adapts packet granularity to actual results, not permission to start while an incoming required blocker is Active. CA-P-1156 must bind the exact accepted carriers and any explicitly retained source-layout repair remainder from those results before execution. Current Operation reuse is not a requirement to reauthor every existing Operation.

### Required output

Current source Operations with explicit inputs, outcomes, actor/handoff and failure behavior as required by current authority, exact changed Atom IDs, and a functional acceptance outline. Add leaves for every remaining adopted slice before the parent can finish.

### Composite packet and execution gate

This packet Plan is composite. Its initial preflight child has an estimate of <=15 minutes; actual execution children are created only after their inputs, ownership, output and verification are bound. Composite roll-up effort depends on the resulting decomposition. Before execution, the parent/preceding-task review must bind the exact evidence packet or capability IDs, live governing revisions, target file paths, output and verification command/scenario in this file. If they cannot be bound safely or exceed the estimate, create narrower subtasks before execution rather than starting an underspecified leaf. A remainder is represented by new Plan files and explicit dependency edges, not an untracked promise.

Inherit CA-P-1117 controls and the 90% confidence threshold through IS_DECOMPOSITION_OF. Every issue requires a typed C atom: blocker/failure -> Problem; unresolved choice -> Question; incompatible authority -> Conflict. Postpone a blocked task and work on another independent ready task. After completion, reassess and update affected dependent tasks before they start. Retain durable source/result/provenance evidence; do not mark the parent Done merely because this first packet is Done.

## Details

### Definition of Done

This Plan is not Done if the bound packet's required output or verification evidence is missing; any encountered issue lacks its typed Concern and disposition; any remaining work lacks explicit child/remainder tasks and appropriate BLOCKS edges; governing sources or authority boundaries were bypassed; or the affected dependent task(s) were not reviewed and updated from the completed result. A blocked or timed-out packet is not Done.
