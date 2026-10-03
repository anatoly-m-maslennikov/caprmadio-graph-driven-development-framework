---
subjects:
  governs: "Governed Change/File Identity"
  depends_on: []
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
