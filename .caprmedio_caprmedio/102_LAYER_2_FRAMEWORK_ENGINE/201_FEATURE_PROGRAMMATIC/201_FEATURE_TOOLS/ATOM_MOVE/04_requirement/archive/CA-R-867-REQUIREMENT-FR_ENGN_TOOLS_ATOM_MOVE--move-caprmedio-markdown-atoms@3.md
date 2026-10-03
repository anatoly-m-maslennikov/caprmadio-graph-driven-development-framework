---
subject_scopes:
  - artifact-operations
tier: core
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Move CAPRMEDIO Markdown Atoms

The `ATOM_MOVE` Tool must move one or many CAPRMEDIO Markdown Atom carriers between `.caprmedio` content-role locations while preserving their bytes, filenames, and Atom IDs. It must support exact selectors and recursive source-subtree selection, preserve the selected subtree by default, flatten only when explicitly requested, reject collisions and invalid destinations, and preflight the entire bulk operation. It must default to a mutation-free dry run and apply all validated moves as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk moves, default subtree preservation, explicit flattening, byte and identity preservation, collision and destination rejection, mutation-free dry run, and restoration of every source and destination after an apply failure.
