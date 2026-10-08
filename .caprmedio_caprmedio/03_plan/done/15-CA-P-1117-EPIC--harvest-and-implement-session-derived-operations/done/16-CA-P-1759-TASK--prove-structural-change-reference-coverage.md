---
atom_id: CA-P-1759
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 2
updated_at: "2026-10-06 04:12:31 +0000"
subjects:
  governs: "Prove structural change reference coverage"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  blocks: [CA-P-1655]
---
# Summary

Prove structural change reference coverage

## Objective

Derive authoritative affected-reference coverage before Scope Unit changes rather than trusting empty caller frontiers or asserted Goal state.

## Details

WORKFLOW_OPERATIONS/PROJECT_STRUCTURE implementation/tests; structural_admission_repair. O012/O014 govern; units may legitimately have no active Goal; project_structure.toml remains authoritative.

Estimated bounded slice: <=15 minutes. Workers share the checkout, preserve other edits and do not stage or commit. Root owns integration and Git. Preparation does not prove runtime execution.

## Definition of Done

An unlisted affected declared reference blocks mutation; complete covered proposals succeed; actual Goals/descendants/carriers are accounted without forcing a Goal.

## Pre-execution review

Root accepts this bounded repair/restoration against Operator authority, DRY, preservation of valuable information and the latest continuation. Keep installed N intact and distinguish local tests from required actual runtime gates.

## Recorded verification

06396a228 retains authoritative scope-field coverage, exact frontmatter-only rename repair, lowercase active selection and Remove refusal with active references. Fifteen tests pass; the independent review's Remove blocker was repaired. No semantic body rewriting or inferred rehome is allowed.
