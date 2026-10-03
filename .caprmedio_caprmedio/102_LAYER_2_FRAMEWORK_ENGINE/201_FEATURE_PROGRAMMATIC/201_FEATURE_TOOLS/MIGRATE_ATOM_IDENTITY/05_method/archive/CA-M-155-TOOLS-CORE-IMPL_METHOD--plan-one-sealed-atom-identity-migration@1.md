---
subject_scopes:
  - artifact-operations
version: 1
updated_at: 2026-08-23 12:00:00
relations:
  method_for:
    - CA-R-1048
---
# Plan one sealed Atom identity migration

For one supplied migration request, resolve the exact active source and destination carriers, collect only their filesystem facts and canonical-ID collision candidates, and pass those facts to a pure planner. The planner checks every sealed precondition, removes any source `atom_id` or `tier` only when explicitly declared and present, applies only the remaining named frontmatter and relation changes in memory, derives the exact result digest, and returns one `UPDATE` or `MOVE+UPDATE` receipt.

On `--apply`, atomically write the planned resulting bytes to the selected destination and remove the source only when the paths differ. If source removal fails, remove the new destination and report failure. Do not derive identity mappings, relation meanings, timestamps, frontmatter changes, Journal events, or Git actions that the request did not explicitly supply.
