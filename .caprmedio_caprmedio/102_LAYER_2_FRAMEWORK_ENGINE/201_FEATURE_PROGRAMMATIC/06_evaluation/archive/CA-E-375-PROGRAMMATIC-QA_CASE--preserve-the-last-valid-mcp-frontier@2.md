---
atom_id: CA-E-375
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp-frontier
  depends_on:
    continuant:
      - programmatic software
version: 2
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-193
  derived_from:
    - CA-A-058
---
# Preserve the last valid MCP frontier

## Claim checked

One invalid MCP frontier refresh leaves the preceding complete valid frontier
available and reports the invalid active Tool.

## Test case

Start with one valid exposed Tool frontier, then refresh from a candidate set
containing one active Tool with a colliding endpoint identity.

## Acceptance criteria

Pass only when the candidate frontier is rejected, the collision is reported,
and the preceding frontier remains unchanged and callable.

## Failure disposition

Reject the refresh path until replacement is atomic at the validated frontier
boundary.

## Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md)
