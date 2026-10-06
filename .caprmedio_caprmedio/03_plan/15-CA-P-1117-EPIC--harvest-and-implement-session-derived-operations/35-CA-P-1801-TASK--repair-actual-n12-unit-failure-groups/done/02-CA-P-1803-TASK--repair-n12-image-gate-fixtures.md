---
atom_id: CA-P-1803
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 1
updated_at: "2026-10-06 19:02:03 +0000"
subjects:
  governs: "Repair N12 image gate fixtures"
  depends_on: [Implementation, Evaluation, Source Carrier]
relations:
  is_decomposition_of: [CA-P-1801]
  relates_to: [CA-C-508]
---
# Summary

Repair N12 image gate fixtures

## Objective

repair confirmed image-gate fixture or implementation defects against current RMED, preserving real image/canary acceptance.

## Details

- this lane owns 24 failing cases from the frozen N12 Unit report, not a new scope expansion.
- use disposable fixtures; preserve actual Run, runtime, Journal and source snapshot evidence.
- coordinate shared production dependencies instead of overlapping another worker. root integrates accepted changes and current pins.

## Definition of Done

the observed failures are explained and fixed against current authority; focused regression suites pass and independent review accepts the bounded change. actual full Release acceptance remains with the parent Plan.

## Result

- the fixture now reflects the sealed rollback retention condition: `retain_prior` yields a retained prior image and the exact settings condition reference.
- exact immutable-image identity, all-container inspection, rollback selector and command/receipt assertions remain intact.
- the two final regression cases passed in 77.339 seconds with exit 0; independent read-only review accepts the bounded patch.
- the complete N13 Unit gate and later actual Release gates remain required under the parent Plan; the uncaptured long local module run is not claimed passing.
