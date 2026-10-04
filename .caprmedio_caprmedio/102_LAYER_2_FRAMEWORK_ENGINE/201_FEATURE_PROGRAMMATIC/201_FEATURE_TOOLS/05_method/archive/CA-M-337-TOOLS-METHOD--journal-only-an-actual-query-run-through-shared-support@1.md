---
atom_id: CA-M-337
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:30:00 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/Run evidence"
  depends_on: [Workflow Run, Action Run, Journal, Tool]
relations:
  method_for: [CA-R-1867]
---
# Summary

Journal only an actual query Run through shared support

## Scope

Actual query invocation evidence.

## Claim

To record an actual Journal query invocation, the Tool **must** delegate preview/execute admission and Run evidence to the shared selected-Run support after snapshot binding.

## Details

Preview has no Run/Event; execute records only actual Run outcomes and cannot change the already captured result frontier.

