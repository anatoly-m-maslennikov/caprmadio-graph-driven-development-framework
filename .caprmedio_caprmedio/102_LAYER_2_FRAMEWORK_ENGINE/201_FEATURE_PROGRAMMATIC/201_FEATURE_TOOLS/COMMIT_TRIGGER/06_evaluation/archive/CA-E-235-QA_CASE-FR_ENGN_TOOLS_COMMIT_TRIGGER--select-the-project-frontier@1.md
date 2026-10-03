---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-21 06:34:42
relations:
  check_of:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_TRIGGER--emit-only-operational-hook-triggers
---
# Select the project frontier

Given admitted and ignored repository paths, when `COMMIT_TRIGGER` scans the project frontier, then it includes ordinary Git-eligible files and `.caprmedio` files, excludes paths rejected by current Git ignore rules, excludes every top-level dot-directory other than `.caprmedio`, and retains Work Journal files only for pipeline-correlation suppression rather than as independent subjects.
