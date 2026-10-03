---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - commit-automation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-182
---
# Resume one queued plan after Scheduler restart

## Claim checked

A durable manager-defined plan survives Scheduler and service termination.

## Test case

Persist one plan with a completed step and one newly ready step, terminate the Scheduler and manager, restart from the selected installed release, and dispatch once.

## Acceptance criteria

The completed step is not replayed, exactly the persisted ready step is claimed, its identities and digests are preserved, and no new transition is inferred.

## Failure disposition

Reject recovery if work is lost, duplicated, reordered, or reconstructed from process memory.
