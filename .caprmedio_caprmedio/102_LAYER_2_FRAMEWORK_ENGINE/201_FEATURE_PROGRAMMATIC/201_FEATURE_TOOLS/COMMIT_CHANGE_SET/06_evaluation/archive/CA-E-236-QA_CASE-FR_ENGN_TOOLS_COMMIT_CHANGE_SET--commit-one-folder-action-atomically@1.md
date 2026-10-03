---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-21 06:34:42
relations:
  check_of:
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
---
# Commit one folder action atomically

Given one sealed folder-subject context and its complete Journal receipt set, when `COMMIT_CHANGE_SET` applies it, then exactly one commit contains all and only the folder entry changes plus the related Journal sidecars and the Journal contains exactly one completed project-change event for the folder.
