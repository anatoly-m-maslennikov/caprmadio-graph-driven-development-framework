---
atom_id: CA-E-287
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  evaluation_for:
    - CA-M-181
  derived_from:
    - CA-A-057
---
# Distinguish one protocol failure from one Tool failure

## Claim checked

MCP returns stable model-readable responses that distinguish a protocol failure from a canonical Tool failure.

## Test case

Produce one invalid protocol message and one valid message whose canonical Tool returns a structured failure.

## Acceptance criteria

The two responses are distinct, retain applicable provenance, and expose no internal implementation detail.

## Failure disposition

Reject the result adapter until it preserves the required distinction.
