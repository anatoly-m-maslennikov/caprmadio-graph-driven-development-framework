---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 23:40:00
relations:
  evaluation_for:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
---
# Commit all and only related Journal sidecars

## Claim checked

One governed commit contains one governed subject change plus every and only Journal sidecar record related to that action.

## Test case

Prepare one action with related records in two Journal carriers, one unrelated record in an affected carrier, and one unrelated unstaged file; apply the commit flow and inspect the committed line-level changes.

## Acceptance criteria

The commit contains the one governed subject change and every receipt-bound line sharing the action identity, contains no unrelated Journal line or file change, and leaves all unrelated work untouched.

## Failure disposition

Reject the commit at the first missing related sidecar, included unrelated line, second governed subject identity, or changed unrelated file.
