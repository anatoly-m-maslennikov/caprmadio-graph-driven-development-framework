---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 23:40:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
---
# Classify rename as UPDATE

## Claim checked

A filename-only rename of one governed file identity without Structural relocation is classified only as `UPDATE`.

## Test case

Supply a trigger for one identity whose filename changes while content, Structural location, governed meaning, and version remain unchanged.

## Acceptance criteria

The sealed context reports `UPDATE`, records both filenames, preserves the version, and does not report `MOVE`.

## Failure disposition

Reject classification and report any identity split, version change, or competing change set.
