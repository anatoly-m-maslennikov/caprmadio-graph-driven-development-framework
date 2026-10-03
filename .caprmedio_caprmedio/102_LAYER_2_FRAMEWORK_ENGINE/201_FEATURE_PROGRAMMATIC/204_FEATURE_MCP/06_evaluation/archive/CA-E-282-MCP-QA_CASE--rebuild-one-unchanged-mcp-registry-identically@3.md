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
    - CA-M-176
  derived_from:
    - CA-A-057
---
# Rebuild one unchanged MCP registry identically

## Claim checked

Repeated MCP registry generation over one unchanged sealed frontier is semantically idempotent.

## Test case

Generate the registry twice from the same Tool-contract and project frontier.

## Acceptance criteria

The two registries have the same capability identities and schemas; volatile execution metadata does not change that result.

## Failure disposition

Stop publication and report the first nondeterministic source or ordering defect.
