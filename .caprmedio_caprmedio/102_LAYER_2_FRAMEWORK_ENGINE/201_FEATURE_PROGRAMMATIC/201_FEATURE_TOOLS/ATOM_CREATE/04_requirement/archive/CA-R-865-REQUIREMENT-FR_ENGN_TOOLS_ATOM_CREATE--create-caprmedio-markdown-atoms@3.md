---
subject_scopes:
  - artifact-operations
tier: core
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Create CAPRMEDIO Markdown Atoms

The `ATOM_CREATE` Tool must create one or many CAPRMEDIO Markdown Atom carriers only under `.caprmedio` content-role locations. It must accept a complete path or a directory and filename with frontmatter and content, enforce the current filename grammar, reject carrier and stable Atom-ID collisions, establish revision metadata, and preflight the entire bulk operation. It must default to a mutation-free dry run and apply all validated creations as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk creation, current filename validation, Atom-ID and path collision rejection, automatic initial revision metadata, mutation-free dry run, and no partial creation after a failed bulk preflight or apply.
