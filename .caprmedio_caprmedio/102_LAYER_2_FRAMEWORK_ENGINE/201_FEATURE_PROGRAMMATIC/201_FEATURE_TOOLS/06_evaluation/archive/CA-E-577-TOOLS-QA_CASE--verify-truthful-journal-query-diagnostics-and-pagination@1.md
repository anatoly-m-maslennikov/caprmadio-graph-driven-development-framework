---
atom_id: CA-E-577
content_role: Evaluation
type: QA Case
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
  depends_on: [Tool, Journal, Evaluation]
relations:
  evaluation_for: [CA-R-1865, CA-R-1871]
---
# Summary

Verify truthful Journal query diagnostics and pagination

## Claim

The Tool reports malformed Events, missing IDs, duplicate fields, incomplete reads, source changes, coverage, and page limits without silently skipping them.

## Test case

Introduce one fixture for each diagnostic plus a bounded multi-page snapshot.

## Acceptance criteria

Every outcome identifies its exact diagnostic, returned/scanned counts, and snapshot-bound continuation state; no affected fixture is reported complete.

## Failure disposition

Reject silent omission, invented completeness, or pagination across an unbound frontier.

