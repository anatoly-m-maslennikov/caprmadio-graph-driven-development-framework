---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 2
updated_at: 2026-08-23 16:45:00 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-1121
  check_of:
    - CA-D-010
---
# Reject a noncanonical governed commit message

## Claim checked

The Git gate accepts a real-change message only when it is the Initiative-based Projection for its sealed action.

## Test case

For one valid atomic action, present the exact `<initiative-summary> | <CHANGE_CLASS> | <affected-subject>` message and variants with a technical parent, changed class, changed subject, extra body line, or trailer. Separately present the Journal-batch form for a real-change action.

## Acceptance criteria

Only the exact real-change Projection succeeds. Every altered or Journal-batch form fails before the Git effect without changing the message carrier, index, working tree, governed source, Journal, refs, or runtime state.

## Failure disposition

Reject the delivery if a noncanonical message passes, the canonical message fails, or message validation mutates project state.
