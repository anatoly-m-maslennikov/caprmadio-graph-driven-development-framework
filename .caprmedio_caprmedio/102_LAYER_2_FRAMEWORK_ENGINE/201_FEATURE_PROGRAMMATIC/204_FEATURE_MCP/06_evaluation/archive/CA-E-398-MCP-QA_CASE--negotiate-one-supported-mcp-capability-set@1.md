---
atom_id: CA-E-398
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-178
  derived_from:
    - CA-A-057
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
