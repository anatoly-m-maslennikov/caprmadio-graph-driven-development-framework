---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 8
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1041
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate and describe one Atom replacement

For one replacement request, resolve the predecessor **and** successor by exact active Atom ID **and** reject an unresolved, inactive, duplicated, **or** self-referential pair. Preserve the sealed Initiative action context. Return a structured replacement action naming the successor **and** predecessor archive transition **without** inferring a relation **or** generic carrier behavior.

Dry run is mutation-free. `--apply` is accepted **only** through the authorized project-local MCP delegation carried by that sealed Initiative envelope. The authorized effect invokes the canonical Atom lifecycle operation, preserves the declared action boundary, **and** obtains durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success. `REPLACE_ATOM` never appends the Journal, stages files, **or** creates a Git commit.
