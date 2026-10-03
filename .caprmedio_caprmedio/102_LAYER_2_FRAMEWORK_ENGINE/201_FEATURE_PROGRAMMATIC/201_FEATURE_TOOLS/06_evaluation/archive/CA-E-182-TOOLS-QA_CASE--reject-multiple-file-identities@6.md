---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
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
