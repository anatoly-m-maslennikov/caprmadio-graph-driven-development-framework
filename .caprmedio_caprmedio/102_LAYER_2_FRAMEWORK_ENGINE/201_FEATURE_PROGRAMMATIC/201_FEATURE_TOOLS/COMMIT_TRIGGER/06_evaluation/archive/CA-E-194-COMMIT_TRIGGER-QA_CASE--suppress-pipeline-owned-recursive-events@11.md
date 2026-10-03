---
subjects:
  governs: "Commit Trigger"
  depends_on: []
version: 11
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-803
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Suppress pipeline-owned recursive events

## Claim checked

Writes owned by one commit-automation action do not create an independently admitted recursive action.

## Test case

Run one subject change through Journal append, real-change commit, and later Journal-only commit while observing every asynchronous PostToolUse event produced by pipeline-owned writes; repeat after service restart.

## Acceptance criteria

Transport may preserve correlated observations, but the intake and reconciliation identities associate them with the existing action and admit no second governed action. The original subject action and independent commit classes complete once. Suppression depends on stable action correlation rather than timing or process-local memory.

## Failure disposition

Reject the flow if a pipeline-owned write creates a recursive action, if the original event is suppressed, if independent commit classes are collapsed, or if restart loses correlation.
