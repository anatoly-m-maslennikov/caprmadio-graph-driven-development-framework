---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 9
updated_at: 2026-08-23 16:45:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
    - CA-R-1121
---
# Commit one governed change independently from a Journal batch

## Claim checked

One sealed real-change action creates exactly one Initiative-named Git commit for its governed target, while its canonical Journal record and any Journal-only batch commit remain independent evidence.

## Test case

Prepare one valid `UPDATE` action with a sealed Initiative, an unrelated unstaged change, and an independently prepared Journal record. Run the real-change gate, then run a later Journal batch and reconciliation. Inspect the two commit trees, Journal record, outbox state, and returned envelopes.

## Acceptance criteria

The real-change commit contains all and only the resolved action target changes, no Journal carrier change, and the exact Initiative-based message. The unrelated change remains untouched. The Journal-only batch contains only selected Journal carrier changes and has the distinct batch message. Reconciliation binds the same action to both evidence streams without duplicate record or commit.

## Failure disposition

Reject the flow at the first extra commit, mixed commit class, missing action binding, message difference, duplicate Journal record, or unintended working-tree effect.
