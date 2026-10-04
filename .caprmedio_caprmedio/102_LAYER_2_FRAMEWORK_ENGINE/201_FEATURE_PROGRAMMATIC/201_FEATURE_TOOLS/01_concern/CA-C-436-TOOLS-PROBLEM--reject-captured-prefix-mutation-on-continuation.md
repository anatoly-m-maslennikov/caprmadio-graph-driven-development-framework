---
atom_id: CA-C-436
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
  governs: "Journal snapshot continuation integrity"
  depends_on: [Journal, Event, Pagination]
relations:
  relates_to: [CA-R-1866, CA-M-334, CA-M-336, CA-E-577]
---
# Summary

Reject captured-prefix mutation on continuation

## Disposition

Resolved in the Journal source contract: continuation revalidates source and
captured-member hashes, rejects changed/deleted/unreadable/truncated captured
data, and permits bytes appended after the sealed prefix.
