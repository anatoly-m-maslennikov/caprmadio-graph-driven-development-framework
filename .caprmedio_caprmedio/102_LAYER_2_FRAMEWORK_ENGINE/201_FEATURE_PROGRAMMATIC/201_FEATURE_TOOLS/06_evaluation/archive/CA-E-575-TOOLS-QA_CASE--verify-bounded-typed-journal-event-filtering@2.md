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
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
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

Query a fixed snapshot containing scalar, null, array, object, nested,
escaped-key, and array-index values through shared valid/invalid fixtures, plus
unknown, bad-pointer, and dot-qualified Event selectors.

## Acceptance criteria

Shared valid and invalid cases preserve CA-R-1850 results for every Event value
type; local invalid selectors return invalid-filter diagnostics and no fallback.
Request-byte, depth, token, IN-member, page-size, selected-field, timeout, and
retained-finding maxima each reject at maximum plus one (or time out) and expose
configured and consumed budget evidence.

## Failure disposition

Reject a divergent local grammar, selector fallback, or filename-based value.
