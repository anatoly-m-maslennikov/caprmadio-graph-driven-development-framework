---
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 5
updated_at: 2026-09-01 02:30:00 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-812
    - CA-R-1121
---
# Commit one folder action atomically

## Test case

Given one sealed folder action with its complete ordered entry set, when `COMMIT_CHANGE_SET` applies it, then exactly one real-change commit contains all and only that folder action's entry changes with its Initiative-based message. Its Journal record is appended independently and a later Journal-only batch, if any, contains only Journal carrier changes.

## Sources

- [CA-R-805 — Serialize repository Git mutations through one logical gate](../04_requirement/CA-R-805-COMMIT_CHANGE_SET-REQUIREMENT--serialize-repository-git-mutations-through-one-logical-gate.md)
- [CA-R-812 — Append governed action records independently of real-change commits](../../APPEND_CHANGE_RECORDS/04_requirement/CA-R-812-APPEND_CHANGE_RECORDS-REQUIREMENT--append-governed-action-records-independently-of-real-change-commits.md)
