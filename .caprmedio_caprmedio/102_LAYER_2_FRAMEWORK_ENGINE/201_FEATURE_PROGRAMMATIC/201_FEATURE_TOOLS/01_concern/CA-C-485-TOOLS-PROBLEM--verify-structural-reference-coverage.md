---
atom_id: CA-C-485
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Verify structural reference coverage"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1759]
---
# Summary

Verify structural reference coverage

## Concern

Structural change accepts an arbitrary empty reference frontier and caller Goal/preservation assertions without complete affected-carrier coverage.

## Evidences

At commit `c011b68fa`, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/project_structure.py:327-409` accepts empty reference frontiers and asserted Goal state; apply accounts only those supplied references. CA-O-012 and CA-O-014 require complete prepared/current affected coverage.

Source/mock results do not establish actual release completion.

## Blast radius

The restored audit additionally found resulting-tree validation delayed until apply, caller-asserted Goal/Carrier coverage, absent Move reparenting coverage and secret-content recovery serialization. CA-P-1776 owns these bounded repairs against O012/O005/O014. Existing narrower reference-repair evidence does not close those new findings.

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Resolve actual declared references and Goal state before mutation; do not force Goal existence. Block incomplete coverage rather than silently leaving broken references.

CA-P-1759 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
