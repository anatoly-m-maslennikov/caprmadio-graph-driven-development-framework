---
subject_scopes:
  - artifact-operations
tier: core
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Archive active Atoms

The `ATOM_ARCHIVE` Tool must archive one or many active CAPRMEDIO Markdown Atoms by moving each carrier into the `archive` location of its content-role directory. It must preserve carrier bytes, filename, and stable Atom ID; reject drafts, already archived Atoms, collisions, and non-Atom Markdown; and preflight the complete bulk operation. It must default to a mutation-free dry run and apply all validated archives as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk archiving, exact byte and stable-identity preservation, correct content-role archive placement, mutation-free dry run, lifecycle and collision rejection, and restoration of every source and destination after an apply failure.
