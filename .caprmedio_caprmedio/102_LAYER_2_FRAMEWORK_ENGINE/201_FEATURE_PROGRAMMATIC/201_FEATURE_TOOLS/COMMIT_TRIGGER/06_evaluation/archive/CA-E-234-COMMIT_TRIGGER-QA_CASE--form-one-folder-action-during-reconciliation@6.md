---
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 6
updated_at: 2026-09-01 02:30:00 +0400
relations:
  evaluation_for:
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Form one folder action during reconciliation

## Test case

Given multiple Git-admitted changes below one non-root folder and an explicitly declared grouping policy, when COMMIT_AUTOMATION reconciles the current repository frontier, then its pure manager forms one folder-subject action with one frozen ordered entry set and preserves every contributing event identity. COMMIT_TRIGGER does not scan or group the repository.

## Sources

- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
