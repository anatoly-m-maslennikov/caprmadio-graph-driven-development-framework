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
# Emit one folder action

Given one observed operation that changes multiple Git-trackable files below one non-root folder, when `COMMIT_TRIGGER` compares the before and after frontiers, then it emits one folder-subject trigger whose boundary covers the common folder rather than one trigger per contained file.
