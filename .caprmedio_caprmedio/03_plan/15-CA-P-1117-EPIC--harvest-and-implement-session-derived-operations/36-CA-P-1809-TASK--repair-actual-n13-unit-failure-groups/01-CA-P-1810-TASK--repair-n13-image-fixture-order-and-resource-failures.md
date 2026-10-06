---
atom_id: CA-P-1810
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
  governs: "Repair N13 image fixture order and resource failures"
  depends_on: [Implementation, Evaluation, Source Carrier, Workflow, Action, Journal]
relations:
  is_decomposition_of: [CA-P-1809]
  relates_to: [CA-C-514]
---
# Summary

Repair N13 image fixture order and resource failures

## Objective

repair the confirmed cause of the twenty-two image-fixture failures in the sealed Unit context without weakening image or retention predicates.

## Details

test_release_image.py and its necessary isolated fixture helper; reproduce the actual later-case failure, retain precise reason diagnostics, and verify a bounded order-equivalent regression.

## Definition of Done

the confirmed defect is explained and repaired against current authority; source-equivalent focused regressions have a captured terminal result and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.
