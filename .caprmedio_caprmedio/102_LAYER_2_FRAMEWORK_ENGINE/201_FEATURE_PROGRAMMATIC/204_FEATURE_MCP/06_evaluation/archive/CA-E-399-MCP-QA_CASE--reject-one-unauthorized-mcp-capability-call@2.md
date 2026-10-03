---
atom_id: CA-E-399
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 2
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-180
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject one unauthorized MCP capability call

## Claim checked

An MCP request without the required capability authority is rejected before
project access and does not expose or reuse credentials.

## Test case

Submit one structurally valid request whose authorization context lacks the
required permission and carries credentials for another resource.

## Acceptance criteria

Pass only when the request is rejected before access, the protocol error is
stable, logs contain no token material, and the unrelated credential is not
used.

## Failure disposition

Stop the capability and treat any access or disclosure as an authority-boundary
defect.

## Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [CA-M-180 — Preserve least authority and secret boundaries](../05_method/CA-M-180-MCP-CORE-METHOD--preserve-least-authority-and-secret-boundaries.md)
