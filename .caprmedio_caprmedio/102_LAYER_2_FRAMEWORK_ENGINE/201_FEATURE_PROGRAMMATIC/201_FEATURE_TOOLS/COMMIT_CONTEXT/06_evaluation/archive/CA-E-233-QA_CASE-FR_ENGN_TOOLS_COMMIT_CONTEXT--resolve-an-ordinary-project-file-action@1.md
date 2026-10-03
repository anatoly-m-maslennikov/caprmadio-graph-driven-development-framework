---
subject_scopes:
  - feature-boundary
version: 1
updated_at: 2026-08-21 06:34:42
relations:
  check_of:
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
---
# Resolve an ordinary project file action

Given a Git-eligible non-Atom project file, when `COMMIT_CONTEXT` resolves an add, update, move, move-and-update, or removal trigger, then it returns one valid file-subject context with an empty graph-source set and a deterministic logger-owned revision without requiring Markdown, frontmatter, or Atom relations.
