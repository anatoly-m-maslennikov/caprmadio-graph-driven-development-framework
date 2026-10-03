---
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 5
updated_at: 2026-09-01 02:30:00 +0400
relations:
  evaluation_for:
    - CA-R-804
    - CA-M-087
  derived_from:
    - CA-A-057
---
# Resolve an ordinary project file action

## Test case

Given a Git-eligible non-Atom project file, when `COMMIT_CONTEXT` resolves an add, update, move, move-and-update, or removal trigger, then it returns one valid file-subject context with an empty graph-source set and a deterministic logger-owned revision without requiring Markdown, frontmatter, or Atom relations.

## Sources

- [CA-R-804 — Gather provisional programmatic action context concurrently](../04_requirement/CA-R-804-COMMIT_CONTEXT-REQUIREMENT--gather-provisional-programmatic-action-context-concurrently.md)
- [CA-M-087 — Process one project-path action](../../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
