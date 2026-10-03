---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "background-services"
  depends_on: []
version: 6
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-104
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Open one service circuit at a declared failure budget

## Claim checked

Automatic recovery is bounded **and** integrity-sensitive failures require Operator action.

## Test case

Exhaust one measured transient restart budget, **then** separately inject governance, Journal, staging, ambiguous Git, **and** lease-integrity failures.

## Acceptance criteria

Transient recovery stops at the declared budget **and** opens a visible circuit. Every integrity-sensitive failure pauses autonomous dispatch immediately, preserves accepted state, **and** reports deterministic Operator recovery instructions. No unconditional auto-resume occurs.

## Failure disposition

Reject the service **if** it loops, hides budget use, drops work, **or** retries an integrity-sensitive failure autonomously.
