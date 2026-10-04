---
atom_id: CA-R-1861
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:30:00 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source"
  depends_on: [Journal, Event, Tool]
relations:
  relates_to: [CA-O-162, CA-D-555]
---
# Summary

Read only the canonical Events Journal

## Scope

The FIND_AND_FETCH_JOURNAL_EVENTS Tool source boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** query only canonical Event carriers under the selected Project's `.caprmedio_<project name>/_journal/` root.

## Details

Historical sealed Event references resolve only as immutable references; no alternate log, derived projection, filename identity, or source rewrite may substitute for canonical Events.

