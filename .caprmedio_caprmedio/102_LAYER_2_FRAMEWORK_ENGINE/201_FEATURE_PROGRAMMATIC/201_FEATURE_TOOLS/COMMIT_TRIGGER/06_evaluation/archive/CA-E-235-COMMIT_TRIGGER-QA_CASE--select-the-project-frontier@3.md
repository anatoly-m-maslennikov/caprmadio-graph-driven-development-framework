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
    - CA-R-803
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Select the project frontier

Given admitted and ignored repository paths, when `COMMIT_TRIGGER` scans the project frontier, then it includes ordinary Git-eligible files and `.caprmedio` files, excludes paths rejected by current Git ignore rules, excludes every top-level dot-directory other than `.caprmedio`, and retains Work Journal files only for pipeline-correlation suppression rather than as independent subjects.
