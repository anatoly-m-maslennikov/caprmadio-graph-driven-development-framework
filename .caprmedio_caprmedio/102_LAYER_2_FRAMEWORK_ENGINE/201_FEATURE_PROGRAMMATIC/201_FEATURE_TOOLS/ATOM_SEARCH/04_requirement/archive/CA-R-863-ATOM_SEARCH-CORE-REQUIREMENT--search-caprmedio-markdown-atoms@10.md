---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 10
updated_at: 2026-09-04 03:10:59 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Search CAPRMEDIO Markdown Atoms

The `ATOM_SEARCH` Tool is the canonical Finder for CAPRMEDIO Markdown Atom carriers under the configured Project control root. It must support deterministic search over carrier path, filename, frontmatter, and content; exact Atom selectors; lifecycle and subtree filters; singular and bulk results; and metadata-only, content-only, or combined output. It may use generic artifact-query mechanics but owns Atom eligibility, selector, and output-view semantics. It must never mutate governed project truth.

## Check

Automated tests must prove that search returns deterministic singular and bulk results, respects subtree and lifecycle filters, excludes non-Atom Markdown, exposes only the requested output view, and leaves all repository bytes unchanged.
