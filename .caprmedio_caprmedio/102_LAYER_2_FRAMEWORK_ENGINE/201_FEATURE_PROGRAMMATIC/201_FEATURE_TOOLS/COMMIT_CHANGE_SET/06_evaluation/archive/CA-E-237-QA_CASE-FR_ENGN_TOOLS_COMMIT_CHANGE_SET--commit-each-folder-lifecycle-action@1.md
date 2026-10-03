---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-21 06:34:42
relations:
  check_of:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
---
# Commit each folder lifecycle action

Given a non-empty Git-trackable folder, when it is added, structurally moved, updated across multiple contained files, and removed in successive operations, then every operation produces exactly one folder-subject commit and one completed Journal event, uses `ADD`, `MOVE`, `UPDATE`, and `REMOVE` respectively, and advances the logger-owned folder revision only while a present result exists.
