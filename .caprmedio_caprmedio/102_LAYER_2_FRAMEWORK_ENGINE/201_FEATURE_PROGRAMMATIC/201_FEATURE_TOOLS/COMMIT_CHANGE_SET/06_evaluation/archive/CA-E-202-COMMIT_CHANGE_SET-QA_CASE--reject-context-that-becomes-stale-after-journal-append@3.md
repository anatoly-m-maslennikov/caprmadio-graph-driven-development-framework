---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-805
    - CA-R-812
---
# Reject context that becomes stale after Journal append

## Claim checked

The commit Doer revalidates sealed context after Journal append and fails recoverably if the source frontier changes before Git mutation.

## Test case

Run `APPEND_CHANGE_RECORDS` for one valid `UPDATE`, then change its Git base or a sealed frontier digest before passing the receipts and live lease to the commit boundary.

## Acceptance criteria

`COMMIT_CHANGE_SET` returns a deterministic stale-context diagnostic before staging, creates no commit, and preserves the receipt-bound Journal records plus one observable blocked action and lease state for idempotent retry or explicit operator resolution.

## Failure disposition

Reject the Doer if it stages or commits stale state, deletes or duplicates an accepted Journal record, silently refreshes the context, releases the blocked action as successful, or permits a later action to bypass it.
