---
subjects:
  governs: "concern-resolution"
  depends_on: []
version: 9
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-R-1042
    - CA-R-1093
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject unadmitted Concern closure application

## Test case

Given one active Concern ID, terminal disposition, optional active resolver or subject IDs, and a sealed Initiative action, `CLOSE_ATOM` dry run returns the closure action without mutation. Direct `--apply` without authorized project-local MCP delegation returns a stable rejection and leaves every carrier, Journal, index, Git history, and runtime file unchanged.

Given the same sealed action through authorized MCP delegation, the Tool invokes only the canonical lifecycle operation and MCP receives durable `COMMIT_TRIGGER` intake acknowledgement before success. The Tool itself does not append the Journal, stage files, or create a Git commit.

## Sources

- [CA-R-1042 — Coordinate Concern closure intent](../04_requirement/CA-R-1042-CLOSE_ATOM-CORE-REQUIREMENT--coordinate-concern-closure-intent.md)
