---
subject_scopes:
  - artifact-operations
tier: core
version: 4
updated_at: 2026-08-23 15:59:05 +0400
---
# Move CAPRMEDIO Markdown Atoms

The `ATOM_MOVE` Tool is the canonical Doer for moving CAPRMEDIO Markdown Atom carriers between `.caprmedio` content-role locations while preserving their bytes, filenames, and Atom IDs. It must support exact selectors and recursive source-subtree selection, preserve the selected subtree by default, flatten only when explicitly requested, reject collisions and invalid destinations, and preflight the complete operation. An atomic action moves exactly one Atom; a bulk action freezes two or more Atom targets with their expected revisions or digests and is all-or-nothing. It may use generic rename mechanics but owns Atom placement, identity-preservation, transaction, and effect semantics. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk moves, default subtree preservation, explicit flattening, byte and identity preservation, collision and destination rejection, mutation-free dry run, MCP-gated apply, and restoration of every source and destination after an apply failure.
