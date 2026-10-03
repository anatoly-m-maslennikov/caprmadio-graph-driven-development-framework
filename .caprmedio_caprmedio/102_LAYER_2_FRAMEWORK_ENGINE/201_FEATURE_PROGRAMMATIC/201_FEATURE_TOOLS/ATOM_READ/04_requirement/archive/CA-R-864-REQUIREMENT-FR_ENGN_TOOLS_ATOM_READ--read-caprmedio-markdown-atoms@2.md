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
# Read CAPRMEDIO Markdown Atoms

The `ATOM_READ` Tool must resolve one or many CAPRMEDIO Markdown Atoms from an exact repository-relative path, full filename, filename stem, or Atom ID. For every resolved Atom, it must return content only, metadata only, or both. Metadata must include the raw frontmatter and identity, placement, and lifecycle facts derived from the carrier filename and location. Missing or ambiguous selectors must fail explicitly, and the Tool must never mutate governed project truth.

## Check

Automated tests must prove equivalent resolution by path, filename, filename stem, and Atom ID; correct singular and bulk results; exact output-view selection; explicit missing and ambiguous failures; and no repository-byte mutation.
