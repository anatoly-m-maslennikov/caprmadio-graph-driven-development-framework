---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: "2026-09-17 02:10:33 +0000"
relations:
  evaluation_for:
    - CA-M-180
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Redact one secret from an MCP result

## Claim checked

MCP does **not** expose a secret through a projected capability result **or** diagnostic.

## Test case

Inject one secret-bearing diagnostic value into a Tool result fixture.

## Acceptance criteria

the public MCP representation excludes that value while retaining the classified failure meaning.

## Failure disposition

Stop the affected capability **and** treat the representation as a secret-boundary defect.
