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
    - CA-R-1107
  derived_from:
    - CA-A-057
---
# Validate one complete Tool invocation contract

## Applicable when

Apply before MCP exposes one active Tool.

## Procedure

1. Read the Tool's canonical identity, capability kind, input schema, result envelope, diagnostic and failure contract, and executable binding.
2. Validate that each field is present, coherent, and bound to the same current Tool identity.
3. Return the validated contract or explicit field-level diagnostics without repairing or reinterpreting it.

## Outcome

Only one complete canonical Tool contract is eligible for MCP projection.

## Failure or stop

Stop when any contract field is missing, conflicting, ambiguous, or unresolved.
