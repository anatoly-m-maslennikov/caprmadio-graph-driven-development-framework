---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-M-087
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Commit each folder lifecycle action

## Test case

Given a non-empty Git-trackable folder, when it is added, structurally moved, updated across multiple contained files, and removed in successive operations, then every operation produces exactly one folder-subject commit and one completed Journal event, uses `ADD`, `MOVE`, `UPDATE`, and `REMOVE` respectively, and advances the logger-owned folder revision only while a present result exists.

## Sources

- [CA-R-805 — Serialize repository Git mutations through one logical gate](../04_requirement/CA-R-805-COMMIT_CHANGE_SET-REQUIREMENT--serialize-admitted-local-commits-through-one-logical-gate.md)
- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-project-path-action.md)
