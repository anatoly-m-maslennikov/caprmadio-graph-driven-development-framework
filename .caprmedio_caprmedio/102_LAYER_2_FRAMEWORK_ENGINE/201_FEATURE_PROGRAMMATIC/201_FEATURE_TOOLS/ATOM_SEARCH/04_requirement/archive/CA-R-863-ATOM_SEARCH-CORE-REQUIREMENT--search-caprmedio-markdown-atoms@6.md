---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Search CAPRMEDIO Markdown Atoms

The `ATOM_SEARCH` Tool is the canonical Finder for CAPRMEDIO Markdown Atom carriers under `.caprmedio`. It must support deterministic search over carrier path, filename, frontmatter, and content; exact Atom selectors; lifecycle and subtree filters; singular and bulk results; and metadata-only, content-only, or combined output. It may use generic artifact-query mechanics but owns Atom eligibility, selector, and output-view semantics. It must never mutate governed project truth.

## Check

Automated tests must prove that search returns deterministic singular and bulk results, respects subtree and lifecycle filters, excludes non-Atom Markdown, exposes only the requested output view, and leaves all repository bytes unchanged.
