---
atom_id: CA-P-1816
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 20:24:00 +0000"
subjects:
  governs: "Retain per-route candidate Run evidence"
  depends_on: [Implementation, Evaluation, Source Carrier, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1124]
  relates_to: [CA-C-515]
---
# Summary

Retain per-route candidate Run evidence

## Objective

preserve already-completed disposable-fixture Run and Journal evidence needed by the final coverage matrix.

## Details

- the existing sealed harnesses assert native per-route evidence, then remove disposable fixtures; their retained JUnit reports alone do not contain exact per-route Run IDs.
- use a bounded read-only observer under .caprmedio_tmp to preserve completed graph/Run results and exact supporting Journal prefixes before cleanup. bind every copy to its original path, bytes/mode/digest, candidate and fixture-local definitions.
- this is report collection, not a product Tool or permission expansion. it dispatches no Workflow, creates no Event, changes no source/runtime and never claims a fixture-local fifteen-route manifest is the live sixteen-route binding.
- after actual harness passage, attach captured identities and receipts to the existing matrix. absent captures remain explicit gaps, never inferred success.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.
