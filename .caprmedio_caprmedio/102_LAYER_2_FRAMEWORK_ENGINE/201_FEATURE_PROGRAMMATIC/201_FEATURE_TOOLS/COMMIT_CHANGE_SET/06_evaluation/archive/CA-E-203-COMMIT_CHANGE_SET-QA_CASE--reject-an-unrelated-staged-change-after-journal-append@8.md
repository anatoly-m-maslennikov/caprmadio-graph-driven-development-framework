---
subjects:
  governs: "Git Index"
  depends_on: []
version: 8
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject an unrelated staged change after Journal append

## Claim checked

The commit Doer revalidates the index after Journal append and does not absorb a newly staged unrelated change.

## Test case

Run `APPEND_CHANGE_RECORDS` for one valid `UPDATE`, stage a separate repository file after receipts are returned, and pass the receipts and live lease to the commit boundary.

## Acceptance criteria

`COMMIT_CHANGE_SET` returns a deterministic unrelated-staged-change diagnostic before staging its own files, preserves the complete index, creates no commit, and preserves the receipt-bound Journal records plus one observable blocked action and lease state for retry or explicit operator resolution.

## Failure disposition

Reject the Doer if it commits, unstages, overwrites, or absorbs the unrelated change; deletes or duplicates an accepted Journal record; or allows a later action to bypass the blockage.
