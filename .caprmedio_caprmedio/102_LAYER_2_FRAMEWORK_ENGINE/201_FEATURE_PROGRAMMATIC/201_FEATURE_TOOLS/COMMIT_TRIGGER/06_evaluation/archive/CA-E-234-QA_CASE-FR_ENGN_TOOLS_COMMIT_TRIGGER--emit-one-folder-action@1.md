---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-21 06:34:42
relations:
  check_of:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
---
# Emit one folder action

Given one observed operation that changes multiple Git-trackable files below one non-root folder, when `COMMIT_TRIGGER` compares the before and after frontiers, then it emits one folder-subject trigger whose boundary covers the common folder rather than one trigger per contained file.
