---
atom_id: CA-E-578
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source snapshot"
  depends_on: [Tool, Journal, Workflow Run, Action Run, Evaluation]
relations:
  evaluation_for: [CA-R-1866]
---
# Summary

Verify query snapshot excludes its own execution Events

## Claim

The Tool's result frontier remains unchanged when shared Run evidence appends during its actual invocation.

## Test case

Capture the Journal byte-prefix before workflow/action-start recording, start an
admitted execute invocation that records actual Run evidence, and append an
unrelated later Event before result pagination.

## Acceptance criteria

Returned IDs and continuation remain exactly the pre-dispatch snapshot; own and
later Events are absent, the result exposes the initial token and prefix hash,
and a standalone Action performs the same capture before its Run evidence.

## Failure disposition

Reject self-inclusion, frontier growth, or an unreported source change.
