---
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-1049
    - CA-R-1093
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate one sealed Atom relation rebinding

## Test case

Given temporary active Markdown Atom carriers, perform dry runs of sealed requests that rewrite one exact relation target to a verified canonical active ID or remove one exact target. Repeated requests must return byte-identical receipts, preserve filename, body, and undeclared frontmatter, advance version once only in the planned result, and report no Journal or Git effect.

Verify direct `--apply` is rejected without authorized project-local MCP delegation. Verify an authorized MCP delegation replaces only the sealed source carrier, returns the deterministic receipt, and receives durable `COMMIT_TRIGGER` intake acknowledgement without a Journal append, staged file, or Git commit. Rejections for inactive source, changed digest, wrong version, unavailable relation, missing old target, repeated old target, and invalid new target leave source bytes unchanged.

## Sources

- [CA-R-1049 — Rebind one active Atom relation set](../../04_requirement/CA-R-1049-TOOLS-CORE-REQUIREMENT--rebind-one-active-atom-relation-set.md)
