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
# Classify content change as UPDATE

## Claim checked

A content change to one governed file identity without Structural relocation is classified only as `UPDATE`.

## Test case

Supply a trigger for one identity whose governed content and resulting version change while its filename and Structural location remain unchanged.

## Acceptance criteria

The sealed context reports `UPDATE`, names the resulting version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report any added `MOVE` flag, preserved old version, or incorrect relation source.
