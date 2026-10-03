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
    - CA-M-181
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Distinguish one protocol failure from one Tool failure

## Claim checked

MCP returns stable model-readable responses that distinguish a protocol failure from a canonical Tool failure.

## Test case

Produce one invalid protocol message **and** one valid message whose canonical Tool returns a structured failure.

## Acceptance criteria

the two responses are distinct, retain applicable provenance, **and** expose no internal implementation detail.

## Failure disposition

Reject the result adapter **until** it preserves the required distinction.
