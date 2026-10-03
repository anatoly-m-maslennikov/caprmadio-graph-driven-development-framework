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
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Commit each folder lifecycle action

## Test case

Given a non-empty Git-trackable folder, when it is added, structurally moved, updated across multiple contained files, and removed in successive operations, then every operation produces exactly one folder-subject commit and one completed Journal event, uses `ADD`, `MOVE`, `UPDATE`, and `REMOVE` respectively, and advances the logger-owned folder revision only while a present result exists.

## Sources

- [CA-R-805 — Serialize repository Git mutations through one logical gate](../04_requirement/CA-R-805-COMMIT_CHANGE_SET-REQUIREMENT--serialize-repository-git-mutations-through-one-logical-gate.md)
- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
