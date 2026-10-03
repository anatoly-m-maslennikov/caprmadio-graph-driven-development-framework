---
subjects:
  governs: "Git Index"
  depends_on: []
version: 11
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
