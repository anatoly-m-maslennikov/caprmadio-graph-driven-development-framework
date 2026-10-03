---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Form one folder action during reconciliation

## Test case

Given multiple Git-admitted changes below one non-root folder **and** an explicitly declared grouping policy, **when** COMMIT_AUTOMATION reconciles the current repository frontier, **then** its pure manager forms one folder-subject action with one frozen ordered entry set **and** preserves **every** contributing event identity. COMMIT_TRIGGER does **not** scan **or** group the repository.

## Sources

- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-project-path-action.md)
