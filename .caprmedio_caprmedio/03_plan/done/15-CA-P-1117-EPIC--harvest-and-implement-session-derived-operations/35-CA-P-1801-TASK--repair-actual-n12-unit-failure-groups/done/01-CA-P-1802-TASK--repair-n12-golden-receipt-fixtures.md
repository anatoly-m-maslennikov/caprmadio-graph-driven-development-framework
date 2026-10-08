---
atom_id: CA-P-1802
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
status: Done
version: 1
updated_at: "2026-10-06 18:31:00 +0000"
subjects:
  governs: "Repair N12 golden receipt fixtures"
  depends_on: [Implementation, Evaluation, Source Carrier]
relations:
  is_decomposition_of: [CA-P-1801]
  relates_to: [CA-C-507]
---
# Summary

Repair N12 golden receipt fixtures

## Objective

repair the source-complete golden fixture and affected tests without weakening actual receipt, currentness or Full Gate checks.

## Details

- this lane owns 17 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

the fixture now writes the exact context-derived unit-deadline.json snapshot consumed by the real reader. independent review accepts the two-line fixture change. four focused tests have retained exit-0 terminal results: two retained-fixture cases, the E2E fixed-command/bound-receipt case and the Full Gate exact-partition/unchanged-bytes case. the long combined run has no retained aggregate verdict and is not claimed passing; the fresh complete Unit and later release gates remain with the parent Plan.
