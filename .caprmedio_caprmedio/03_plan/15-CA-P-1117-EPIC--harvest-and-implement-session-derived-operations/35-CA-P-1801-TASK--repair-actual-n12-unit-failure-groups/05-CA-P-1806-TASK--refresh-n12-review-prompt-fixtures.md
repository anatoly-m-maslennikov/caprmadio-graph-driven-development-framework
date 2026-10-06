---
atom_id: CA-P-1806
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 17:46:21 +0000"
subjects:
  governs: "Refresh N12 review prompt fixtures"
  depends_on: [Implementation, Evaluation, Source Carrier]
relations:
  is_decomposition_of: [CA-P-1801]
  relates_to: [CA-C-511]
---
# Summary

Refresh N12 review prompt fixtures

## Objective

refresh the exact prompt settings pin and correct the sealed authority fixture, retaining all substantive authorization and no-forcing checks.

## Details

- this lane owns 2 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

