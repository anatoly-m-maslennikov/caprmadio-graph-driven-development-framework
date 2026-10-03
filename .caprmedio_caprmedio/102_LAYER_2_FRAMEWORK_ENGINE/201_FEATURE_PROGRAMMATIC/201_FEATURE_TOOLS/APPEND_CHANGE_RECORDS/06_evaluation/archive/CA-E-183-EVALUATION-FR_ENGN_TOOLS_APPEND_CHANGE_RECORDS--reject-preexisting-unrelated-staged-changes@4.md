---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-20 23:43:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
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
