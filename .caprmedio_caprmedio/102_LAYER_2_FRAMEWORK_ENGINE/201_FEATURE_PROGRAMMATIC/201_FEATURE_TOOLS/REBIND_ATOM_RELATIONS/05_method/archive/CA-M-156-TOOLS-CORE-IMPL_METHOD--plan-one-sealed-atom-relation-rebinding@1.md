---
subject_scopes:
  - artifact-operations
version: 1
updated_at: 2026-08-23 13:20:00
relations:
  method_for:
    - CA-R-1049
---
# Plan one sealed Atom relation rebinding

For one supplied request, resolve the exact active source carrier. When the request contains rewrites, load the canonical relation-type dictionary and collect canonical filename-derived IDs that have exactly one active Markdown Atom carrier; reject a rewrite relation unavailable for direct storage in an Atom carrier. A removal needs no relation admission because it only deletes one exact stored target and never introduces or translates a relation meaning. Pass only the observed source bytes, rewrite-admitted target IDs, and sealed request to a pure planner.

The planner verifies the source digest and version, verifies that every named old target occurs exactly once under its named relation, verifies every rewrite target ID, applies only the requested rewrites and removals in memory, advances `version` once, sets the supplied `updated_at`, and derives the exact result digest. It returns one `UPDATE` receipt.

On `--apply`, recheck the source digest and atomically replace that source. Do not infer relation meanings or target mappings, rename either carrier, modify the body or unspecified frontmatter, write backups, append the Journal, stage files, or create a Git commit.
