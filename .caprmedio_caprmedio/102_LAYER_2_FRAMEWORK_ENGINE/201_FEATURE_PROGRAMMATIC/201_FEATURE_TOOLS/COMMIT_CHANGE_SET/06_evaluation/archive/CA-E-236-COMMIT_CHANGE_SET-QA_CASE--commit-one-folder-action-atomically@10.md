---
subjects:
  governs: "Governed Change/Git Commit Creation"
  depends_on: []
version: 10
updated_at: "2026-09-12 04:12:43 +0400"
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-812
    - CA-D-417
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Commit one folder action atomically

## Test case

Given one sealed folder action with its complete ordered entry set, when `COMMIT_CHANGE_SET` applies it, then exactly one real-change commit contains all and only that folder action's entry changes with its Initiative-based message. Its Journal record is appended independently and a later Journal-only batch, if any, contains only Journal carrier changes.

## Sources

- [CA-R-805 — Serialize repository Git mutations through one logical gate](../04_requirement/CA-R-805-COMMIT_CHANGE_SET-REQUIREMENT--serialize-admitted-local-commits-through-one-logical-gate.md)
- [CA-R-812 — Append governed action records independently of real-change commits](../../APPEND_CHANGE_RECORDS/04_requirement/CA-R-812-APPEND_CHANGE_RECORDS-REQUIREMENT--append-governed-action-records-independently-of-real-change-commits.md)
