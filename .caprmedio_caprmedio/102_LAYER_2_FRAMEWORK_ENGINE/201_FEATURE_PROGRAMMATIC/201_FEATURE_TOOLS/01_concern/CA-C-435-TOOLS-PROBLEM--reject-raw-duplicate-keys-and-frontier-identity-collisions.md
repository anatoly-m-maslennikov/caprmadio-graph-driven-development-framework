---
atom_id: CA-C-435
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: "Journal raw identity validation"
  depends_on: [Journal, Event, QUERY_FILTER]
relations:
  relates_to: [CA-R-1861, CA-R-1865, CA-M-334, CA-E-577]
---
# Summary

Reject raw duplicate keys and frontier identity collisions

## Disposition

Resolved in the Journal source contract: raw JSON duplicate object keys are
rejected before parse, and Event IDs must be unique across the captured frontier.
CA-E-577 preserves expected-failure evidence; no implementation claim is made.
