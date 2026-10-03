---
subject_scopes:
  - artifact-operations
version: 2
updated_at: 2026-08-23 16:45:00 +0400
relations:
  method_for:
    - CA-R-1049
---
# Plan one sealed Atom relation rebinding

For one sealed request, resolve the exact active source carrier, verify its digest and version, validate only the explicitly named direct relation rewrites or removals, and pass the observed bytes and sealed request to a pure planner. The planner preserves filename, body, and undeclared frontmatter, advances version once, sets the supplied timestamp, derives the result digest, and returns one `UPDATE` receipt.

Dry run is mutation-free. `--apply` is accepted only through authorized project-local MCP delegation with the sealed Initiative action envelope. The authorized effect atomically replaces only the source carrier and obtains durable `COMMIT_TRIGGER` intake acknowledgement before MCP reports success. It never infers a relation meaning, target mapping, backup, Journal event, staging change, or Git action.
