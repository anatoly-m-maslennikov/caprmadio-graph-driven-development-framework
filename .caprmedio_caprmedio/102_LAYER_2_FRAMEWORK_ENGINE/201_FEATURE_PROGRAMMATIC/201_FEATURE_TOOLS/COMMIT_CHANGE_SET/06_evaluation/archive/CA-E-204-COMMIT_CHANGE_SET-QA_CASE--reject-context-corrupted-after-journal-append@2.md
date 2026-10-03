---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_APPEND_CHANGE_RECORDS--append-governed-file-change-journal-records
---
# Reject context corrupted after Journal append

## Claim checked

The commit Doer rejects a sealed context whose canonical fields no longer match the receipt-bound event.

## Test case

Run `APPEND_CHANGE_RECORDS` for one valid `UPDATE`, remove the singular canonical `result` from the context after receipts are returned, and pass the corrupted context with those receipts and the live lease to the commit boundary.

## Acceptance criteria

`COMMIT_CHANGE_SET` returns a deterministic context-receipt mismatch diagnostic before staging, creates no commit, and preserves the accepted Journal records plus one observable blocked action and lease state for retry with the original context or explicit operator resolution.

## Failure disposition

Reject the Doer if it reconstructs the missing field, stages or commits, deletes or duplicates a Journal record, silently rewrites a receipt, or permits a later action to bypass the blockage.
