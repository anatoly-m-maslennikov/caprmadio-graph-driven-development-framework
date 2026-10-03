---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 1
updated_at: 2026-08-23 17:40:00 +0400
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

1. Validate the message and assign its declared time and resource bounds.
2. Expose progress only for an admitted long-running operation.
3. On cancellation, expiry, invalid input, or resource exhaustion, stop with a structured outcome and preserve Tool and project state.

## Outcome

Every MCP request has an explicit admission and completion boundary.

## Failure or stop

Stop before dispatch on an invalid or expired request and never leave an ungoverned background operation.
