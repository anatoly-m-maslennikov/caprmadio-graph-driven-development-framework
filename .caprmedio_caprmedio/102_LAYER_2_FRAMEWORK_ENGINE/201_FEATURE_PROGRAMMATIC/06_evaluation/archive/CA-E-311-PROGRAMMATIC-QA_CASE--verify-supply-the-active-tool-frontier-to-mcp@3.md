---
atom_id: CA-E-311
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-193
---
# Verify supply the active tool frontier to mcp

## Claim checked

One MCP frontier refresh deterministically distinguishes a valid active Tool,
a disabled Tool, and an invalid active Tool without changing Tool meaning.

## Applicable conditions

Apply when MCP builds or refreshes its callable frontier from TOOLS.

## Test case

Provide one valid active Tool with a machine contract, one explicitly disabled
Tool, and one active Tool with an invalid machine contract, then request one
frontier refresh.

## Acceptance criteria

Pass only when exactly one unchanged endpoint is projected for the valid active
Tool, the disabled Tool is omitted, the invalid active Tool is reported
explicitly, and no call semantics or mechanics are duplicated in MCP.

## Failure disposition

Reject the candidate frontier and preserve the preceding valid frontier when
the complete projection cannot validate.

## Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md)
