---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1114
  derived_from:
    - CA-A-057
---
# Regenerate one MCP registry deterministically

## Applicable when

Apply before publishing the MCP registry for a resolved project frontier.

## Procedure

1. Seal the complete current Tool-contract source frontier.
2. Order equivalent inputs stably and generate the registry from those inputs only.
3. Repeat generation against an unchanged frontier and compare semantic registry content while excluding volatile execution metadata.

## Outcome

The same current Tool contracts and project state produce the same MCP capability registry.

## Failure or stop

Stop when source sealing, ordering, identity, or repeated semantic output is not deterministic.
