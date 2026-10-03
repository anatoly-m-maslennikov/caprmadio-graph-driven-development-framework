---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 3
updated_at: 2026-09-01 01:55:00 +0400
relations:
  method_for:
    - CA-R-1117
  derived_from:
    - CA-A-057
---
# Bound one admitted MCP request

## Applicable when

Apply when MCP receives one protocol message before Tool dispatch.

## Procedure

1. Validate the message against the admitted schema and assign its declared
   time and resource bounds.
2. Expose progress only for an admitted long-running operation.
3. On cancellation, expiry, invalid input, or resource exhaustion, stop with a structured outcome and preserve Tool and project state.

## Outcome

Every MCP request has an explicit admission and completion boundary.

## Failure or stop

Stop before dispatch on an invalid or expired request and never leave an ungoverned background operation.

## Sources

- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
- [CA-A-057 — Reconcile PROGRAMMATIC specialization authority](../../02_analysis/CA-A-057-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-programmatic-specialization-authority.md)
