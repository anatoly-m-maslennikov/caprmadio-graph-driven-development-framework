---
atom_id: CA-P-1778
content_role: Plan
type: Plan
label: Task
work_sequence_number: 27
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 05:20:14 +0000"
subjects:
  governs: "Source-bound semantic Update assessment admission"
  depends_on: [Implementation, Analysis, Atom, Evaluation, Permission]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1775, CA-P-1655, CA-P-1721]
---
# Summary

Admit source-bound semantic Update assessments

## Objective

Support substantive Update only through exact source-bound assessment evidence, preserving separate mutation authorization.

## Details

1. Add Tool-specific R/M/E/D for the optional completed Analysis Report reference before implementation. Reuse the existing generic O067/O145/O129 evidence contract; do not put Tool serialization into the Core Meta-Model.
2. Bind the report to the current target, exact proposal, current change authority, same-primary-Claim finding and completed lineage-impact evidence.
3. Read and seal verified evidence at O145, then reopen and revalidate it before O129 persists the change.
4. Cover a valid semantic Revision and missing, stale, mismatched, altered or incomplete evidence. A report creates no permission; uncertain input remains unresolved.

One lifecycle worker owns this bounded interface and its tests. Source IDs R1892/M348/E591/D585 are reserved; D584 belongs to the separate Implementation packet lane. Estimated source/schema and implementation slices are each <=15 minutes. Root owns integration and actual release dispatch.

## Definition of Done

Source-first authority, source-bound valid semantic Update and fail-closed regression evidence are independently accepted. Real Docker/queue acceptance remains required separately.

## Pre-execution review

The existing unresolved outcome is safe, but cannot by itself establish the requested semantic Update capability. The Operator authorized best-option decisions with a retained Question. CA-C-494 records the chosen saved-report interface; assessment evidence is not approval.
