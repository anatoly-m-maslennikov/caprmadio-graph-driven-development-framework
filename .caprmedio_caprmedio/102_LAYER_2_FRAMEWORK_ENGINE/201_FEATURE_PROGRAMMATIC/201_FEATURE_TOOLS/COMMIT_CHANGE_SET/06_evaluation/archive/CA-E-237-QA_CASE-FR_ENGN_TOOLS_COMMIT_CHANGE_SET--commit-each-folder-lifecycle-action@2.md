---
subject_scopes:
  - feature-boundary
version: 2
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Commit each folder lifecycle action

Given a non-empty Git-trackable folder, when it is added, structurally moved, updated across multiple contained files, and removed in successive operations, then every operation produces exactly one folder-subject commit and one completed Journal event, uses `ADD`, `MOVE`, `UPDATE`, and `REMOVE` respectively, and advances the logger-owned folder revision only while a present result exists.
