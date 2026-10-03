---
subject_scopes:
  - artifact-operations
tier: core
version: 2
updated_at: 2026-08-22 03:01:35
relations:
  child_of:
    - CA-R-004
    - CA-R-861
---
# Search CAPRMEDIO Markdown Atoms

The `ATOM_SEARCH` Tool must find only CAPRMEDIO Markdown Atom carriers under `.caprmedio`. It must support deterministic search over carrier path, filename, frontmatter, and content; exact Atom selectors; lifecycle and subtree filters; singular and bulk results; and metadata-only, content-only, or combined output. It must never mutate governed project truth.

## Check

Automated tests must prove that search returns deterministic singular and bulk results, respects subtree and lifecycle filters, excludes non-Atom Markdown, exposes only the requested output view, and leaves all repository bytes unchanged.
