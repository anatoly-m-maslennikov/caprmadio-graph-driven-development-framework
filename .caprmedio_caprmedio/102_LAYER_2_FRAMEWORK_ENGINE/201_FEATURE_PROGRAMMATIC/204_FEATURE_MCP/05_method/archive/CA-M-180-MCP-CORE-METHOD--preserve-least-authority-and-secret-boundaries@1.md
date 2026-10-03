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
    - CA-R-1118
  derived_from:
    - CA-A-057
---
# Preserve least-authority and secret boundaries

## Applicable when

Apply when MCP projects a capability, forwards an invocation, or forms a result.

## Procedure

1. Grant no more authority than the source Tool requires and preserve its authorization checks.
2. Bind credentials only to their admitted transport and resource boundary.
3. Exclude secrets from discovery, results, diagnostics, logs, progress, and generated registries.

## Outcome

MCP exposes only the Tool's admitted authority without leaking credentials.

## Failure or stop

Stop the affected projection or invocation when authority is broadened or a secret-bearing representation would be emitted.
