---
subjects:
  declared:
    continuant:
      - artifact-operations
version: 5
updated_at: 2026-08-23 16:16:20 +0400
---
# Promote drafts to active Atoms

The `ATOM_PROMOTE` Tool is the canonical Doer for promoting CAPRMEDIO Markdown Atom drafts into active authority. Promotion is not archiving or upgrading: every promoted draft receives an operator-supplied stable Atom ID matching the draft's content role; the Tool derives the accepted filename from that ID and the mutable draft filename, removes the `drafts` location segment, and preserves carrier bytes. It must reject non-drafts, missing, invalid, mismatched, or colliding Atom IDs, destination collisions, and partial operations. An atomic action promotes exactly one draft; a bulk action freezes two or more draft targets and their assigned IDs and is all-or-nothing. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk promotion, stable-ID assignment and filename derivation, correct active placement, byte preservation, mutation-free dry run, MCP-gated apply, invalid identity and collision rejection, and restoration of every draft and destination after an apply failure.
