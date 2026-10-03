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
    - CA-M-169
  derived_from:
    - CA-A-057
---
# Reject one incomplete Tool invocation contract

## Claim checked

MCP exposes only a complete coherent canonical Tool invocation contract.

## Test case

Validate one Tool contract missing its structured result envelope.

## Acceptance criteria

Validation returns a field-level failure and produces no eligible projection.

## Failure disposition

Stop exposure until the contract is complete and unambiguous.
