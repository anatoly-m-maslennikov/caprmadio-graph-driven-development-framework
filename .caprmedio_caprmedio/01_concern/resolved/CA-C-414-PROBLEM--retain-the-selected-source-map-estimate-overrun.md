---
atom_id: CA-C-414
content_role: Concern
type: Problem
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
version: 1
updated_at: "2026-10-04 16:38:53 +0000"
subjects:
  governs: "Plan execution estimate"
  depends_on: [Plan, Analysis]
relations:
  concern_about: [CA-P-1435]
---
# Summary

Retain the selected source-map estimate overrun

## Concern

P1435's completed discovery exceeded its <=15-minute leaf estimate during saving and terminal closure.

## Evidences

The unchanged first clock is 2026-10-04 16:07:03 UTC. The saved evidence gate passed at 16:21:45 (14m42), physical Done placement occurred at 16:22:30 (15m27), and the final receipt was 16:24:04 (17m01). A1141 and the Done Plan retain these different events. The final elapsed overrun is 2m01; no reset or <=15-minute completion claim is accepted.

## Blast radius

The bounded discovery result is retained as complete discovery only, not source acceptance or runtime proof. Root has replaced the broad follow-up with independently bound P1437–1444 packets. Their own actual clocks and incomplete remainders must be recorded. This resolved record preserves the overrun; it does not retroactively make the estimate satisfied.
