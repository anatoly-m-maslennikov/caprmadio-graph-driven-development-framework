---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Archive active Atoms

The `ATOM_ARCHIVE` Tool is the canonical Doer for archiving active CAPRMEDIO Markdown Atoms by moving each carrier into the `archive` location of its content-role directory. Archive preserves carrier bytes, filename, stable Atom ID, revision history, and historical dependents without retaining current authority. It is neither promotion nor upgrade. The Tool must reject drafts, already archived Atoms, collisions, and non-Atom Markdown, and preflight the complete operation. An atomic action archives exactly one Atom; a bulk action freezes two or more Atom targets with their expected revisions or digests and is all-or-nothing. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk archiving, exact byte and stable-identity preservation, correct content-role archive placement, mutation-free dry run, MCP-gated apply, lifecycle and collision rejection, and restoration of every source and destination after an apply failure.
