---
subject_scopes:
  - framework-boundary
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
---
# Declare repository Work Areas

An adopting repository owner must declare either repository-level scope or one or more existing repository-relative folders as Work Areas before scope-dependent CAPRMEDIO consumers operate on them. Every scope-dependent consumer must resolve the current accepted declaration; absolute paths, paths outside the repository, missing folders, and stale declarations are invalid.
