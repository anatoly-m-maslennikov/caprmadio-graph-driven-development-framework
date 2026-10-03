---
subjects:
  governs: "Governed Change/Git Commit Message"
  depends_on: []
version: 9
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-805
    - CA-D-417

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
