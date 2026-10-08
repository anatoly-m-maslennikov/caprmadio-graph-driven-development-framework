---
atom_id: CA-P-1789
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 1
updated_at: "2026-10-06 12:08:00 +0000"
subjects:
  governs: "orchestrator and Implementation typed report fixtures"
  depends_on: [Implementation, Evaluation, Source Carrier, Journal]
relations:
  is_decomposition_of: [CA-P-1782]
  relates_to: [CA-C-498]
---
# Summary

Repair the typed prompt report contract fixtures

## Objective

repair orchestrator and Implementation typed report fixtures without relaxing the accepted release or source-currentness boundaries.

## Details

- this bounded lane feeds a fresh source-bound N10; retain failed N9 without replay.
- root owns Git, integration, source pins, canonical refresh and actual dispatch. workers preserve other lanes' changes.
- local fixture/source acceptance is not full Release acceptance; installed N remains unchanged.

## Definition of Done

2c16f633a; thirty-eight cases pass, retaining baseline failure, source gates and candidate mutation assertions.
