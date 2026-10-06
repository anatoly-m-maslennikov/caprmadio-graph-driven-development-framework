---
atom_id: CA-P-1817
content_role: Plan
type: Plan
label: Task
work_sequence_number: 37
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
version: 1
updated_at: "2026-10-06 23:31:31 +0000"
subjects:
  governs: "bound Unit execution after Release host loss"
  depends_on: [Implementation, Evaluation, Workflow Run, Journal]
relations:
  is_decomposition_of: [CA-P-1117]
  relates_to: [CA-M-343, CA-E-586, CA-D-579]
---
# Summary

bound Unit execution after Release host loss

## Objective

implement the accepted host-independent Unit deadline and fixed temporary-mount contract, preserving sealed commands and non-passing timeout evidence.

## Details

source-first authority and independent review precede implementation. preserve the installed runtime, historical Release evidence and unrelated changes. root owns source publication and actual runtime dispatch.

## Definition of Done

the 18 bounded regression tests pass; independent code review accepts the guard; an installed-image diagnostic confirms daemon-owned timeout without a live host observer. full Release acceptance remains separately gated.
