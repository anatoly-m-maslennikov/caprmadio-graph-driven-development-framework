---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-20 23:41:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
---
# Reject stale context before Journal append

## Claim checked

The Journal-appending Doer fails closed when the repository state no longer matches the sealed context.

## Test case

Gather one valid `UPDATE` context, advance its Git base or alter one sealed frontier digest, then invoke `APPEND_CHANGE_RECORDS` apply with the stale envelope.

## Acceptance criteria

The Doer releases any provisional unconsumed lease, returns a deterministic stale-context diagnostic before the first Journal append, and creates no Journal record, runtime blockage, index, ref, object-reachability, or governed-file change.

## Failure disposition

Reject the Doer if it appends, silently refreshes, or partially applies the stale context.
