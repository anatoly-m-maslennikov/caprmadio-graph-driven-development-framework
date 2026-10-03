---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-1041
    - CA-R-1093
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject unadmitted replacement application

## Test case

Given two distinct active Atom IDs and a sealed Initiative action, `REPLACE_ATOM` dry run returns the explicit replacement action without mutation. Direct `--apply` without authorized project-local MCP delegation returns a stable rejection and leaves every carrier, Journal, index, Git history, and runtime file unchanged.

Given the same sealed action through authorized MCP delegation, the Tool invokes only the canonical lifecycle operation and MCP receives durable `COMMIT_TRIGGER` intake acknowledgement before success. The Tool itself does not append the Journal, stage files, or create a Git commit.

## Sources

- [CA-R-1041 — Coordinate Atom replacement intent](../04_requirement/CA-R-1041-REPLACE_ATOM-CORE-REQUIREMENT--coordinate-atom-replacement-intent.md)
