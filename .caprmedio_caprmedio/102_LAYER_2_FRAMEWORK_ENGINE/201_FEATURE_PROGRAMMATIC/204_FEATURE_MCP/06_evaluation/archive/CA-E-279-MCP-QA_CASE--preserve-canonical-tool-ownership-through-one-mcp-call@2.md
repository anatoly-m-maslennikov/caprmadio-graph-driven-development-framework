---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-173
  derived_from:
    - CA-A-057
---
# Preserve canonical Tool ownership through one MCP call

## Claim checked

MCP delegates a call without reimplementing the canonical Tool's decisions or lifecycle behavior.

## Test case

Invoke one exposed Tool with a fixture that would reveal an MCP-side target or lifecycle decision.

## Acceptance criteria

Only the canonical Tool performs that decision and MCP returns its resulting structured outcome unchanged.

## Failure disposition

Reject the transport implementation as an unauthorized second operation owner.
