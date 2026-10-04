---
atom_id: CA-M-336
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/result selection"
  depends_on: [Event, Tool]
relations:
  method_for: [CA-R-1863, CA-R-1865, CA-R-1871]
---
# Summary

Select and page Event query results

## Scope

Result construction.

## Claim

To construct results, the Tool **must** order snapshot matches deterministically, apply the bounded page, and expose IDs, selected fields, or full Events only in the requested mode with truthful coverage metadata.

## Details

The next-page token remains bound to the source snapshot and result selection; a request cannot use it against a new frontier.
