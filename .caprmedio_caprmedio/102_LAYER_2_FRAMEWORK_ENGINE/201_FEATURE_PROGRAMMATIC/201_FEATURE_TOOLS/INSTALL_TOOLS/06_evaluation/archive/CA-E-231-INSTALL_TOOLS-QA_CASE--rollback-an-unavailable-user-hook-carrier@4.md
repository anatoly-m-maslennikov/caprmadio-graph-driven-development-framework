---
subjects:
  governs:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103

---
# Roll back an unavailable user Hook carrier

## Claim checked

An apply failure at the required Codex user Hook carrier does not expose a partially selected Tool release.

## Test case

Install one verified release, change the canonical Tool source so the next apply resolves another release, and make the configured Codex user home unavailable as a directory before applying again.

## Acceptance criteria

Apply fails with `host-hook-carrier-unavailable`. The current selection manifest and canonical Codex Hook fragment remain byte-for-byte equal to their pre-apply values, the previously selected release remains active, and existing user and project Hook carriers remain unchanged.

## Failure disposition

Reject the installer if the unavailable carrier selects the new release, changes a retained Hook carrier, hides the cause behind an unstable exception, or requires a repository backup for recovery.
