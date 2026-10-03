---
subject_scopes:
  - artifact-operations
version: 2
updated_at: 2026-08-23 15:25:06
relations:
  child_of:
    - CA-R-004
    - CA-R-861
---
# Migrate one sealed Atom identity

`MIGRATE_ATOM_IDENTITY` must migrate exactly one selected active CAPRMEDIO Markdown Atom carrier from one explicit source path to one explicit destination path. The Doer must default to dry run and accept an exact JSON request containing the source digest and version, approved legacy identity, new canonical Atom ID, classification, exact destination filename tokens, approved frontmatter removals and updates, and exact relation rewrite and removal maps.

The destination filename is the sole authority for canonical Atom ID and Local Tier. The request must not add or update `atom_id` or `tier`; it must remove either field exactly when that field is present in the selected legacy carrier. It must preserve their absence otherwise, while requiring `version` to advance exactly once and an explicit `updated_at` timestamp.

Before applying, the Doer must fail closed on a source digest or version mismatch, inactive or non-Atom carrier, old-identity mismatch, destination or canonical-ID collision, filename-token or content-role mismatch, undeclared frontmatter mutation, and missing or repeated named relation target. It may read other carriers only to validate identity collisions; it must mutate no carrier beyond the selected source and destination.

An applied migration must preserve the Markdown body and every frontmatter or relation element not named in the sealed request, write the resulting carrier atomically, and return a deterministic receipt. The receipt must state `journal: not_performed` and `git: not_performed`, with a ready handoff to `APPEND_CHANGE_RECORDS` and `COMMIT_CHANGE_SET`; this Tool must not append the Journal, stage files, or create a commit.
