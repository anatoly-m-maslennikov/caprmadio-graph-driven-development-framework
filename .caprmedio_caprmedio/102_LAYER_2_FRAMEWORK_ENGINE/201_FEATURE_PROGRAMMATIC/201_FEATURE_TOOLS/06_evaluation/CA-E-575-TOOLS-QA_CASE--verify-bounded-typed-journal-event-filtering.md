---
atom_id: CA-E-575
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/filter"
  depends_on: [Tool, Event, Evaluation]
relations:
  evaluation_for: [CA-R-1850, CA-R-1862, CA-R-1868, CA-R-1869]
---
# Summary

Verify bounded typed Journal Event filtering

## Claim

The Tool applies CA-R-1850 unchanged to every valid canonical Event selector and rejects only unknown or ambiguous Event selectors at its local boundary.

## Test case

Query a fixed snapshot containing canonical Event fields through the shared
filter's valid and invalid fixtures, plus unknown and ambiguous Event selectors.

## Acceptance criteria

Shared valid and invalid cases preserve CA-R-1850 results; local unknown or
ambiguous selectors return invalid-filter diagnostics and no fallback.

## Failure disposition

Reject a divergent local grammar, selector fallback, or filename-based value.
