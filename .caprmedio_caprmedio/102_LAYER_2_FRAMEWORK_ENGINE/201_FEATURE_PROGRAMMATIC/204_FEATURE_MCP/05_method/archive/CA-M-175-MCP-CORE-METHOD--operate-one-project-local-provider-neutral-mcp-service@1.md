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
    - CA-R-1113
  derived_from:
    - CA-A-057
---
# Operate one project-local provider-neutral MCP service

## Applicable when

Apply when a project exposes its generated Tool surface through MCP.

## Procedure

1. Bind one provider-neutral project-local service to the current registry.
2. Expose each eligible Tool through that service without requiring a user interface or agent-host plugin.
3. Permit a plugin to package or connect to the service without moving provider-neutral MCP or Tool ownership into the plugin.

## Outcome

The complete MCP Tool surface remains headless, project-local, and provider-neutral.

## Failure or stop

Stop when an additional service becomes a competing authority or a capability depends on App presentation.
