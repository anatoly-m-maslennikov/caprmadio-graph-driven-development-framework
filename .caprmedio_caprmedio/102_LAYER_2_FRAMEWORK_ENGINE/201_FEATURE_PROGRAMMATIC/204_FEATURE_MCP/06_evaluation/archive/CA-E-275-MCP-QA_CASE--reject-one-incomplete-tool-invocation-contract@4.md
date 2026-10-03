---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 4
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-169
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
