---
atom_id: CA-P-1793
content_role: Plan
type: Plan
label: Task
work_sequence_number: 33
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 14:40:22 +0000"
subjects:
  governs: "Release source delivery predecessor repair"
  depends_on: [Implementation, Evaluation, Source Carrier, Journal, Workflow Run]
relations:
  is_decomposition_of: [CA-P-1117]
  relates_to: [CA-C-500, CA-P-1792]
---
# Summary

Repair source delivery predecessor admission

## Objective

restore safe source-delivery admission for a fresh Release using exact independently accepted predecessor ownership evidence, without weakening unknown-file, currentness or recording guards.

## Details

- N11 is terminally interrupted before delivery with release-copy-predecessor-mismatch. retain its 14 Journal rows and do not replay it.
- code diagnosis, actual-tree comparison, source-authority review and test-first fixture work are separate bounded lanes. root owns source pins, integration, Git and fresh MCP dispatch.
- the finite Unit budget repair is independently accepted: 147 focused tests passed; guarded binding revision 6 is recorded. no complete fresh Unit gate has yet used that budget.
- choose the smallest safe correction and preserve any actual predecessor tree. arbitrary or unproven files remain protected; installed N and historical records remain unchanged.
- use a fresh source-bound N12 only after source/code/evidence acceptance. all Unit, image/canary, Candidate E2E, Full Gate and promotion criteria remain required.

## Definition of Done

the exact mismatch is explained; source and any code correction are independently accepted; ownership, tamper and no-effect regressions pass; a fresh Release completes source delivery with actual recorded evidence.
