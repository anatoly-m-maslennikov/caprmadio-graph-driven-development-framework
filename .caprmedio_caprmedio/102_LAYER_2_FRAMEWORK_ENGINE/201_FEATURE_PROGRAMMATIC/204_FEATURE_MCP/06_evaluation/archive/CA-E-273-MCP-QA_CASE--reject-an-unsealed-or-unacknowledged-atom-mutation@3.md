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
    - CA-M-167
  derived_from:
    - CA-A-057
---
# Reject an unsealed or unacknowledged Atom mutation

## Claim checked

MCP delegates an Atom mutation only with one authorized Initiative and returns success only from the canonical Tool's acknowledged outcome.

## Test case

Submit one mutation request with a missing Initiative, then a request whose canonical Tool returns an unacknowledged result.

## Acceptance criteria

Both requests fail explicitly; MCP neither resolves a target nor reports success.

## Failure disposition

Reject the MCP mutation boundary and retain the canonical Tool as the operation owner.
