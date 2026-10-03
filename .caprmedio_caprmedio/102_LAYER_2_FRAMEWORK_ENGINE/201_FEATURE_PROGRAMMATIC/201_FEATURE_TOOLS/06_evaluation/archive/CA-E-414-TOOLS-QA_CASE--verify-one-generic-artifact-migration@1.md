---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-migration
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-248
---
# Verify one generic Artifact migration

## Claim checked

CA-M-248 read-only replays an applied generic migration plan and reports every residual, unexpected, and unmapped state.

## Applicable when

Apply whenever generic migration postcondition comparison, evidence attribution, or discrepancy classification changes.

## Test case

Use one applied migration plan whose current evidence contains one residual old identity, one unexpected carrier mutation, and one unmapped reference. Replay postconditions and compare every carrier, typed reference, Projection, and Work Journal carrier before and after the replay.

## Acceptance criteria

The result separately reports all three discrepancies with their attributable evidence. No carrier, reference, Projection, or Work Journal evidence changes during verification.

## Failure disposition

Reject the realization and preserve plan postconditions, observed evidence, discrepancy classifications, digests or revisions before and after replay, and no-mutation proof.
