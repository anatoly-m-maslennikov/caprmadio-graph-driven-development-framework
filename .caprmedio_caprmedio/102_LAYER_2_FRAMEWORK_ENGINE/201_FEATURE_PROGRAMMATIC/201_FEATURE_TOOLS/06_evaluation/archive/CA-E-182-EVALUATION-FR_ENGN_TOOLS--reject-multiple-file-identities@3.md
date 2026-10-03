---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 23:40:00
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
---
# Reject multiple file identities

## Claim checked

One commit-flow invocation cannot gather or apply changes for more than one repository file identity.

## Test case

Supply one trigger whose candidates resolve to two independently governed file identities with valid changes.

## Acceptance criteria

The flow returns a deterministic multiple-identities diagnostic before staging or committing either change.

## Failure disposition

Reject the flow if it chooses one identity implicitly, combines both identities, or mutates Git state.
