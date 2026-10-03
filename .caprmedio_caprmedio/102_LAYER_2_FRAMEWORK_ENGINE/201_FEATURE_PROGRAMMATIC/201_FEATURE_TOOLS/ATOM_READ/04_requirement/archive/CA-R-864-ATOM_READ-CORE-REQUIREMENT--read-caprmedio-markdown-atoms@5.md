---
subjects:
  declared:
    continuant:
      - artifact-operations
version: 5
updated_at: 2026-08-23 16:16:20 +0400
---
# Read CAPRMEDIO Markdown Atoms

The `ATOM_READ` Tool is the canonical Finder for resolving one or many CAPRMEDIO Markdown Atoms from an exact repository-relative path, full filename, filename stem, or Atom ID. For every resolved Atom, it must return content only, metadata only, or both. Metadata must include the raw frontmatter and identity, placement, and lifecycle facts derived from the carrier filename and location. It may use generic metadata retrieval but owns Atom resolution and output-view semantics. Missing or ambiguous selectors must fail explicitly, and the Tool must never mutate governed project truth.

## Check

Automated tests must prove equivalent resolution by path, filename, filename stem, and Atom ID; correct singular and bulk results; exact output-view selection; explicit missing and ambiguous failures; and no repository-byte mutation.
