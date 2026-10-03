---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-180
  derived_from:
    - CA-A-057
---
# Redact one secret from an MCP result

## Claim checked

MCP does not expose a secret through a projected capability result or diagnostic.

## Test case

Inject one secret-bearing diagnostic value into a Tool result fixture.

## Acceptance criteria

The public MCP representation excludes that value while retaining the classified failure meaning.

## Failure disposition

Stop the affected capability and treat the representation as a secret-boundary defect.
