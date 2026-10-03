---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  method_for:
    - CA-R-1107
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
