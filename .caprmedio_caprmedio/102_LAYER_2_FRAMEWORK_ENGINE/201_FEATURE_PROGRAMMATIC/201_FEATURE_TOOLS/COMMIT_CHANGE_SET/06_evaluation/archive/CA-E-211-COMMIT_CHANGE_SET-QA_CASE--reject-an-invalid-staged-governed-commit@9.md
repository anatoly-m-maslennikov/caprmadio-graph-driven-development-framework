---
subjects:
  governs: "Governed Change/Git Commit Creation"
  depends_on: []
version: 9
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-805
    - CA-D-417

llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject an invalid staged governed commit

## Claim checked

The Git gate accepts a real-change boundary only when its staged target set exactly matches one sealed action and its Initiative message projection.

## Test case

Present the gate with an unresolved target, stale expected revision, a Journal carrier mixed with a real-change target, two atomic targets, an incomplete bulk target set, and one valid sealed target set.

## Acceptance criteria

Each invalid state returns one stable diagnostic before commit creation. The valid state creates only the sealed real-change target commit and does not require a Journal record or Journal carrier in the index.

## Failure disposition

Reject the delivery if an invalid boundary passes, a valid boundary fails, or preflight mutates repository state.
