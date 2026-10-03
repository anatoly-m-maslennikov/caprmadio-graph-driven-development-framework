---
subjects:
  governs: "Commit Context"
  depends_on: []
version: 9
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-804
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject incomplete context before Journal append

## Claim checked

The Journal-appending Doer fails closed when a required sealed-context field is absent.

## Test case

Remove the singular canonical `result` field from one otherwise valid sealed `UPDATE` context and invoke `APPEND_CHANGE_RECORDS` apply.

## Acceptance criteria

The Doer returns a deterministic missing-`result` diagnostic before the first Journal append, releases any provisional unconsumed lease, and creates no Journal record, runtime blockage, or Git state change.

## Failure disposition

Reject the Doer if it reconstructs the omitted canonical field from the working tree, appends, leaves an unconsumed lease, partially applies the context, or emits a generic diagnostic.
