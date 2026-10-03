---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "commit-automation"
  depends_on: []
version: 5
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-182
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
