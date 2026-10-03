---
subjects:
  governs: "Atom/Revision"
  depends_on: []
version: 11
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-R-805
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject non-current upstream version

## Claim checked

the commit flow cannot seal **or** apply a typed upstream relation whose target version is **not** current immediately **before** the file change.

## Test case

Prepare one `UPDATE` fixture whose direct upstream target is at version 3, **then** supply a candidate context that names version 2 for that same target.

## Acceptance criteria

the flow returns a deterministic non-current-upstream-version diagnostic, names both versions, **and** creates no governed **or** Git state change.

## Failure disposition

Reject the flow **if** it accepts, silently rewrites, **or** omits the stale target reference.
