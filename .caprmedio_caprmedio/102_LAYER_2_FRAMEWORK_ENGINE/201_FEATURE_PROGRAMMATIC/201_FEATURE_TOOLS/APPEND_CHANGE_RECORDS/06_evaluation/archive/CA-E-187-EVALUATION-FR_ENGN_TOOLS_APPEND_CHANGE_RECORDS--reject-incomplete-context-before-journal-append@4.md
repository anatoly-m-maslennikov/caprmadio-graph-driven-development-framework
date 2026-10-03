---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-20 23:45:00
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
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
