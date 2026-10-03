---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Update CAPRMEDIO Markdown Atoms

The `ATOM_UPDATE` Tool is the canonical Doer for updating the frontmatter, content, or both for exactly selected CAPRMEDIO Markdown Atoms. It must preserve each carrier path, filename, and Atom ID, advance revision metadata, reject duplicate, missing, ambiguous, or stale targets, and preflight the complete operation. An atomic action updates exactly one Atom; a bulk action freezes two or more Atom targets with their expected revisions or digests and is all-or-nothing. It may use generic metadata or relation-patch mechanics but owns Atom authority validation, revision, transaction, and effect semantics. It must default to a mutation-free dry run and accept `--apply` only through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Check

Automated tests must prove singular and bulk frontmatter and content updates, preservation of carrier identity and location, automatic revision advancement, mutation-free dry run, MCP-gated apply, selector failure handling, and restoration of every original carrier after an apply failure.
