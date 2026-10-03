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
    - CA-R-1116
  derived_from:
    - CA-A-057
---
# Negotiate declared MCP protocol capabilities

## Applicable when

Apply during MCP service initialization.

## Procedure

1. Declare the supported protocol revision and capability set.
2. Compare the peer's required revision and capabilities with that declaration.
3. Accept only a defined compatible mode and return machine-readable diagnostics for unsupported or invalid lifecycle states.

## Outcome

MCP initialization selects one explicit compatible protocol boundary.

## Failure or stop

Stop on an unsupported revision, incompatible required capability, or invalid lifecycle transition.
