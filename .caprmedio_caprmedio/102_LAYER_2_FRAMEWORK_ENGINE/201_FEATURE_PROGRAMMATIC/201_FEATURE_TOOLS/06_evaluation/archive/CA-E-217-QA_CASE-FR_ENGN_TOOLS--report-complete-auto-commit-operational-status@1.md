---
atom_id: CA-E-217
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-21 02:12:00
relations:
  evaluation_for:
    - CA-D-006
  check_of:
    - CA-D-006
---
# Report complete auto-commit operational status

## Claim checked

An operator can inspect the complete current auto-commit operational state through one read-only interface.

## Test case

Prepare an enabled Codex adapter, registered Git Hooks, one live repository lease, one blocked action with receipts and a recovery instruction, and one prior completed action; invoke the integrated status interface once.

## Acceptance criteria

One schema-versioned result reports the adapter and Hook registration, resolved application and session UUID when available, live lease, blocked action, last completed action, related receipt identities, and deterministic recovery instruction without requiring direct runtime-file inspection. The invocation changes no file, index entry, ref, Journal record, lease, or adapter state.

## Failure disposition

Reject the delivery if any required state is absent, stale, ambiguous, available only through specialist inspection, or changed by the status call.
