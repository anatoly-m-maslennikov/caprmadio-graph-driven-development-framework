---
atom_id: CA-R-1865
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/diagnostics"
  depends_on: [Journal, Event, Tool]
relations:
  relates_to: [CA-O-162, CA-E-577]
---
# Summary

Report complete query diagnostics and bounded coverage

## Scope

Query failure and coverage reporting.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** report malformed Events, missing IDs, duplicate Event fields, incomplete reads, invalid filters, source change, coverage, and pagination truthfully without silent skipping.

## Details

Each result identifies scanned snapshot coverage, matched count when determinable, returned count, next-page availability, and every blocking or partial-read diagnostic.

