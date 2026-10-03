---
subjects:
  declared:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-812
    - CA-R-1121
---
# Commit one folder action atomically

Given one sealed folder action with its complete ordered entry set, when `COMMIT_CHANGE_SET` applies it, then exactly one real-change commit contains all and only that folder action's entry changes with its Initiative-based message. Its Journal record is appended independently and a later Journal-only batch, if any, contains only Journal carrier changes.
