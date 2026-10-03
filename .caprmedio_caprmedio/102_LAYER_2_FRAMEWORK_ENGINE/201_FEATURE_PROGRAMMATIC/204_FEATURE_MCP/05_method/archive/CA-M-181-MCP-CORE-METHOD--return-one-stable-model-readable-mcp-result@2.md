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
    - CA-R-1119
  derived_from:
    - CA-A-057
---
# Return one stable model-readable MCP result

## Applicable when

Apply after one canonical Tool returns an admitted outcome.

## Procedure

1. Map the Tool result, diagnostic, empty result, partial result, or failure to the declared protocol result form.
2. Preserve the original governed meaning and provenance.
3. Distinguish a protocol failure from a Tool failure and omit internal implementation details from the public response.

## Outcome

The model receives a stable, headless-readable result that retains the Tool outcome's meaning.

## Failure or stop

Stop and return an explicit protocol failure when the result cannot be represented without semantic loss or boundary leakage.
