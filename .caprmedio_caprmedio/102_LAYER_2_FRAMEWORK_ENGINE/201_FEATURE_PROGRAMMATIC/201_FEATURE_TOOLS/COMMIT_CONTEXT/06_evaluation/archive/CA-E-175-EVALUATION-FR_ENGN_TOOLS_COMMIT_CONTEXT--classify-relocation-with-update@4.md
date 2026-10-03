---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-20 23:40:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
---
# Classify relocation with update

## Claim checked

One file identity that changes Structural location and also changes content, filename, or other governed carrier state is classified as one `MOVE+UPDATE` change set.

## Test case

Supply a trigger for one identity whose directory and governed content both change in the same working-tree transition.

## Acceptance criteria

The sealed context reports exactly `MOVE+UPDATE`, records both paths and the resulting version, and resolves upstream relations from the resulting staged graph.

## Failure disposition

Reject classification and report any split into two actions, missing flag, identity split, or incorrect relation source.
