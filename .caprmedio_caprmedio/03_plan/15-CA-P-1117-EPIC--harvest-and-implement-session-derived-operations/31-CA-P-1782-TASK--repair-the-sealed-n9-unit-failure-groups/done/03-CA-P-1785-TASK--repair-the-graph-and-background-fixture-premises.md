---
atom_id: CA-P-1785
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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
  governs: "graph disposable Git fixture and exact background-services private-reader fixture"
  depends_on: [Implementation, Evaluation, Source Carrier, Journal]
relations:
  is_decomposition_of: [CA-P-1782]
  relates_to: [CA-C-498]
---
# Summary

Repair the graph and background fixture premises

## Objective

repair graph disposable Git fixture and exact background-services private-reader fixture without relaxing the accepted release or source-currentness boundaries.

## Details

- this bounded lane feeds a fresh source-bound N10; retain failed N9 without replay.
- root owns Git, integration, source pins, canonical refresh and actual dispatch. workers preserve other lanes' changes.
- local fixture/source acceptance is not full Release acceptance; installed N remains unchanged.

## Definition of Done

d1be603f6; fourteen graph and three background cases pass; production guards unchanged.
