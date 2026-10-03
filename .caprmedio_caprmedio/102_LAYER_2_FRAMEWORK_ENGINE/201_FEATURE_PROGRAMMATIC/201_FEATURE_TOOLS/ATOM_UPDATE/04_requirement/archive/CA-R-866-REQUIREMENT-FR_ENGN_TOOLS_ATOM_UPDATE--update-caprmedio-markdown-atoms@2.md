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
# Update CAPRMEDIO Markdown Atoms

The `ATOM_UPDATE` Tool must update the frontmatter, content, or both for one or many exactly selected CAPRMEDIO Markdown Atoms. It must preserve each carrier path, filename, and Atom ID, advance revision metadata, reject duplicate, missing, or ambiguous targets, and preflight the entire bulk operation. It must default to a mutation-free dry run and apply all validated updates as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk frontmatter and content updates, preservation of carrier identity and location, automatic revision advancement, mutation-free dry run, selector failure handling, and restoration of every original carrier after an apply failure.
