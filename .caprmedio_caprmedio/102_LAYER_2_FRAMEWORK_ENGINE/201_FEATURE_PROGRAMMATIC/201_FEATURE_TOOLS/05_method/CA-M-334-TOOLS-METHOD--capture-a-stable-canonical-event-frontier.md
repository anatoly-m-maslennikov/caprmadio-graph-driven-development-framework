---
atom_id: CA-M-334
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source snapshot"
  depends_on: [Journal, Event, Tool]
relations:
  method_for: [CA-R-1861, CA-R-1866]
---
# Summary

Capture a stable canonical Event frontier

## Scope

Source snapshot construction.

## Claim

To capture the query source, the Tool **must** enumerate canonical Event carriers once, seal their ordered references and digests into one opaque snapshot token, then read only that frontier.

## Details

The method detects changed, unreadable, duplicate, or malformed frontier members and returns their exact condition; it never retries by silently extending the frontier.
