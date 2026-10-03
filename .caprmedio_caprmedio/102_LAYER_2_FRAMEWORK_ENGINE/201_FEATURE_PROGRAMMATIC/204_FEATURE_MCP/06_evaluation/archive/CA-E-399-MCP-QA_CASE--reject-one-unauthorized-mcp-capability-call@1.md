---
atom_id: CA-E-399
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
    - CA-M-180
  derived_from:
    - CA-A-057
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
