---
subjects:
  governs: "concern-resolution"
  depends_on: []
version: 7
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1042
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate and describe one Concern closure

For one closure request, resolve the Concern and every supplied resolver or solution by exact active Atom ID, reject unresolved or inactive carriers, require a nonempty terminal disposition, and preserve the sealed Initiative action context. Return one closure action targeting `solved` without inferring relation kinds, role meanings, or participants.

Dry run is mutation-free. `--apply` is accepted only through the authorized project-local MCP delegation carried by that sealed Initiative envelope. The authorized effect invokes the canonical Atom lifecycle operation and obtains durable `COMMIT_TRIGGER` intake acknowledgement before MCP reports success. `CLOSE_ATOM` never appends the Journal, stages files, or creates a Git commit.
