---
atom_id: CA-C-437
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
  governs: "Journal query resource bounds"
  depends_on: [Journal, QUERY_FILTER, Pagination]
relations:
  relates_to: [CA-R-1865, CA-D-556, CA-E-575, CA-E-577]
---
# Summary

Make Journal query resource bounds enforceable

## Disposition

Resolved with configurable maxima and exhaustion evidence for expression depth,
tokens, IN members, page size, selected fields, frontier members, and frontier
bytes. QA requires each maximum-plus-one failure; no runtime implementation is
claimed.
