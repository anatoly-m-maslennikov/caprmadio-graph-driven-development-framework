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
    - CA-M-087
    - CA-M-103
    - CA-M-104
---
# Complete one installed automatic commit end to end

## Claim checked

The exact installed release completes one automatic provenance action without blocking Codex command dispatch.

## Test case

Install and activate a fresh release, start COMMIT_AUTOMATION, invoke one Codex Tool that changes one admitted subject, and observe Hook latency, inbox acceptance, persisted phases, Journal evidence, Git evidence, status, and restart recovery.

## Acceptance criteria

The Codex Tool result is not delayed by provenance completion; one event is durably accepted; the service executes only the fixed pipeline; the independent Journal and real-change Git outcomes match the sealed action; status is complete and read-only; and restart produces no duplicate effect.

## Failure disposition

Reject release readiness if static validation, installation status, or dry-run is the only evidence, or if the fresh installed operation blocks, loses, duplicates, misattributes, or cannot recover the action.
