---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - background-services
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-104
---
# Preserve queued work through service lifecycle controls

## Claim checked

status, pause, resume, stop, start, and reload preserve accepted work and safe mutation boundaries.

## Test case

Prepare queued, active pre-mutation, and active mutation-critical actions; invoke every lifecycle command, including repeated commands and reload to a new selected release.

## Acceptance criteria

Status is read-only. Pause stops dispatch. Stop and reload wait for declared recoverable boundaries. Start and resume drain preserved work without duplicates. No command deletes inbox, queue, action, receipt, circuit, or dead-letter state or force-terminates the mutation-critical action.

## Failure disposition

Reject lifecycle control on lost work, duplicate process or action, unsafe termination, stale release selection, or hidden state.
