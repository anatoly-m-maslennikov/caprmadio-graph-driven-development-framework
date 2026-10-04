---
atom_id: CA-R-1866
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source snapshot"
  depends_on: [Journal, Event, Workflow Run, Action Run, Tool]
relations:
  relates_to: [CA-O-163, CA-M-334, CA-E-578]
---
# Summary

Seal a stable Event source snapshot before query execution

## Scope

The query-source snapshot.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** bind an immutable source snapshot before execution evidence can append and must not enlarge that snapshot with its own execution Events.

## Details

The opaque snapshot token binds ordered canonical Event carrier references and their digests plus the configured source root. An unavailable, changed, or incompletely read frontier reports that condition and cannot claim complete coverage.

