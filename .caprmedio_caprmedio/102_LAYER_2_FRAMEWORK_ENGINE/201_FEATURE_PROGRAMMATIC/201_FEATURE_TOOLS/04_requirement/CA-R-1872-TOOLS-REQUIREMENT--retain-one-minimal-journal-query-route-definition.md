---
atom_id: CA-R-1872
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/route"
  depends_on: [Workflow, Step, Action, Tool]
relations:
  relates_to: [CA-O-161, CA-O-162, CA-O-163, CA-D-557]
---
# Summary

Retain one minimal Journal query route definition

## Scope

The source-to-implementation route.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** retain exactly one Workflow, one query Action, and one query Step as its source route.

## Details

Shared Run support remains shared infrastructure and does not become an additional Workflow or query Action.
