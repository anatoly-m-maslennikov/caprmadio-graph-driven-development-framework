---
subjects:
  governs: "Commit Context"
  depends_on: []
version: 8
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-R-805
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject context corrupted after Journal append

## Claim checked

the commit Doer rejects a sealed context whose canonical fields no longer match the receipt-bound event.

## Test case

Run `APPEND_CHANGE_RECORDS` for one valid `UPDATE`, remove the singular canonical `result` from the context **after** receipts are returned, **and** pass the corrupted context with those receipts **and** the live lease **to** the commit boundary.

## Acceptance criteria

`COMMIT_CHANGE_SET` returns a deterministic context-receipt mismatch diagnostic **before** staging, creates no commit, **and** preserves the accepted Journal records plus one observable blocked action **and** lease state for retry with the original context **or** explicit operator resolution.

## Failure disposition

Reject the Doer **if** it reconstructs the missing field, stages **or** commits, deletes **or** duplicates a Journal record, silently rewrites a receipt, **or** permits a later action **to** bypass the blockage.
