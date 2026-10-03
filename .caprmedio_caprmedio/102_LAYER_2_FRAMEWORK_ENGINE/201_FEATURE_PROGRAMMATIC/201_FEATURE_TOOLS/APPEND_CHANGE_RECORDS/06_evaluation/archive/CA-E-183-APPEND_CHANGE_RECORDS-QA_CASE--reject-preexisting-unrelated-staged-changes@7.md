---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-812
---
# Reject pre-existing unrelated staged changes

## Claim checked

The Journal-appending Doer fails before append when the index already contains a staged change outside the resolved file identity.

## Test case

Prepare one valid sealed `UPDATE` context, stage a separate repository file, and invoke `APPEND_CHANGE_RECORDS` apply.

## Acceptance criteria

The Doer returns a deterministic unrelated-staged-change diagnostic before the first Journal append, releases any provisional unconsumed lease, preserves the complete index, and creates no Journal record, runtime blockage, or commit.

## Failure disposition

Reject the Doer if it appends, unstages, overwrites, or absorbs any staged change.
