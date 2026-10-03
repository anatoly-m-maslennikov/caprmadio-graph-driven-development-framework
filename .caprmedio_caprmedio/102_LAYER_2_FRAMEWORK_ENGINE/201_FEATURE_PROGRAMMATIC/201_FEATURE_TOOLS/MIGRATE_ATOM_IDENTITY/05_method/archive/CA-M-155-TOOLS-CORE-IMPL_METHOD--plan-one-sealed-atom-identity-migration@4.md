---
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1048
---
# Plan one sealed Atom identity migration

For one sealed migration request, resolve the exact active source and destination carriers, collect filesystem facts and canonical-ID collision candidates, and pass only those facts to a pure planner. The planner validates every sealed precondition, applies only the named frontmatter and relation changes in memory, derives the exact result digest, and returns one `UPDATE` or `MOVE+UPDATE` receipt.

Dry run is mutation-free. `--apply` is accepted only through authorized project-local MCP delegation with the sealed Initiative action envelope. The authorized effect atomically writes the planned destination, removes the source only when paths differ, and obtains durable `COMMIT_TRIGGER` intake acknowledgement before MCP reports success. It never infers identity mappings, relation meanings, timestamps, Journal events, or Git actions beyond the sealed request.
