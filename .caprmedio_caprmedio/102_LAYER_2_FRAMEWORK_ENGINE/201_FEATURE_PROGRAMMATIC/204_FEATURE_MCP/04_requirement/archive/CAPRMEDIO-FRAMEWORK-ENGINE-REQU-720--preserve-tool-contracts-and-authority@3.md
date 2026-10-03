---
subject_scopes:
  - framework-engine-mcp
version: 3
updated_at: 2026-08-23 15:59:05 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Preserve Tool contracts and authority

MCP must preserve each Tool's accepted inputs, structured outputs, diagnostics, failures, target-set identity, and side-effect controls without changing their meaning. MCP must preserve Finder read-only behavior, Checker evidence and verdict behavior, Doer dry-run and explicit-apply behavior, and every Tool permission boundary; it must never broaden mutation authority, infer approval, or convert a failed or partial Tool result into success.

For CAPRMEDIO Markdown Atom Doers, MCP must pass through the canonical Tool's sealed target set, expected revision or digest, Initiative action envelope, and resulting receipt. It must not replace a Tool's atomic or bulk cardinality, preflight, conflict, recovery, or lifecycle decision with transport behavior of its own.
