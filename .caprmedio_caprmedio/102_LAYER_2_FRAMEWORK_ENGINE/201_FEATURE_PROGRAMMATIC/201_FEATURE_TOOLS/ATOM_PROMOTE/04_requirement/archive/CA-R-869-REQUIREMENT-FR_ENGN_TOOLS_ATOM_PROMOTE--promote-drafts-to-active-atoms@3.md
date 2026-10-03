---
subject_scopes:
  - artifact-operations
tier: core
version: 3
updated_at: 2026-08-23 15:33:04 +0400
---
# Promote drafts to active Atoms

The `ATOM_PROMOTE` Tool must promote one or many CAPRMEDIO Markdown Atom drafts into active authority. Every promotion must receive an operator-supplied stable Atom ID matching the draft's content role; the Tool derives the accepted filename from that ID and the mutable draft filename, removes the `drafts` location segment, and preserves carrier bytes. It must reject non-drafts, missing, invalid, mismatched, or colliding Atom IDs, destination collisions, and partial bulk operations. It must default to a mutation-free dry run and apply all validated promotions as one recoverable operation only when explicitly requested.

## Check

Automated tests must prove singular and bulk promotion, stable-ID assignment and filename derivation, correct active placement, byte preservation, mutation-free dry run, invalid identity and collision rejection, and restoration of every draft and destination after an apply failure.
