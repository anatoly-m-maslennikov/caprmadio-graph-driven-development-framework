---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 6
updated_at: 2026-08-30 16:44:07 +0400
---
# Migrate one sealed Atom identity

`MIGRATE_ATOM_IDENTITY` is the canonical CAPRMEDIO Markdown Atom Doer for migrating exactly one selected active Atom carrier from one explicit source path to one explicit destination path. It must default to dry run and accept an exact JSON request containing the source digest and version, approved legacy identity, new canonical Atom ID, classification, exact destination filename tokens, approved frontmatter removals and updates, and exact relation rewrite and removal maps. A set of two or more migrations belongs to an explicitly governed bulk coordinator that freezes all single-migration requests and is all-or-nothing; this Tool must not silently widen its one-Atom operation.

The destination filename is the sole authority for canonical Atom ID and Local Tier. The request must not add or update `atom_id` or `tier`; it must remove either field exactly when that field is present in the selected legacy carrier. It must preserve their absence otherwise, while requiring `version` to advance exactly once and an explicit `updated_at` timestamp.

Before applying, the Doer must fail closed on a source digest or version mismatch, inactive or non-Atom carrier, old-identity mismatch, destination or canonical-ID collision, filename-token or content-role mismatch, undeclared frontmatter mutation, and missing or repeated named relation target. It may read other carriers only to validate identity collisions; it must mutate no carrier beyond the selected source and destination.

An apply is accepted only through an authorized project-local MCP delegation with a sealed Initiative action envelope. It must preserve the Markdown body and every frontmatter or relation element not named in the sealed request, write the resulting carrier atomically, and return a deterministic receipt. The receipt must state `journal: not_performed`, `git: not_performed`, and `trigger: acknowledged`; the Tool must cause durable `COMMIT_TRIGGER` intake before MCP reports success, but it must not append the Journal, stage files, or create a Git commit.
