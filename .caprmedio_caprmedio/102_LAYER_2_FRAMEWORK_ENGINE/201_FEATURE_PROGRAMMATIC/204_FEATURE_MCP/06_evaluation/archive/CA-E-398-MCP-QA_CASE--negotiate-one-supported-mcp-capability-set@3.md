---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 3
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-178
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Negotiate one supported MCP capability set

## Claim checked

Supported MCP peers reach operation with exactly the declared negotiated
revision and capability set.

## Test case

Initialize the adapter once with a supported revision and capability set and
once with one unsupported required capability.

## Acceptance criteria

Pass only when the supported peer reaches operation with exactly the negotiated
set and the unsupported peer receives a stable incompatibility response before
any capability executes.

## Failure disposition

Stop the affected session before registry use or Tool dispatch.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [CA-M-178 — Negotiate declared MCP protocol capabilities](../05_method/CA-M-178-MCP-CORE-METHOD--negotiate-declared-mcp-protocol-capabilities.md)
