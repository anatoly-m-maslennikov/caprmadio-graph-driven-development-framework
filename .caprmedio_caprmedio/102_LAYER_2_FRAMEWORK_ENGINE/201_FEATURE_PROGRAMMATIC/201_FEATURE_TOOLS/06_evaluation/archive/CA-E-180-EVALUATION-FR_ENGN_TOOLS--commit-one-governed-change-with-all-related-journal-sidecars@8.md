---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 8
updated_at: 2026-08-20 23:40:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
---
# Commit one governed change with all related Journal sidecars

## Claim checked

Applying one valid sealed context creates exactly one commit containing one governed subject identity and every and only receipt-bound Journal sidecar record related to the same action.

## Test case

Prepare one valid `UPDATE` context that requires multiple related Journal records across two carrier partitions and has one unrelated unstaged change, run the Journal Doer and Git Doer, and inspect the repository lease lifetime, new commit, Journal records, index, remaining working tree, projected commit message, and returned result envelope.

## Acceptance criteria

Exactly one repository-scoped lease is acquired before the first append and released only after verification; exactly one new commit exists; its tree changes only the resolved governed identity and every receipt-bound related Journal line, even across multiple carriers; it contains no unrelated Journal line; its one-line message equals the deterministic Projection of the structured file-change event; the unrelated unstaged change remains untouched; and the returned commit identifier resolves to that commit with no blocked action remaining.

## Failure disposition

Reject the flow and report the first extra commit, governed identity, missing or unrelated Journal record, message difference, or unintended working-tree effect.
