---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on:
    - "Projection"
    - "programmatic software"
version: 8
updated_at: "2026-09-17 19:19:53 +0000"
relations:
  evaluation_for:
    - CA-M-193
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify supply the active tool frontier to mcp

## Claim checked

One MCP frontier refresh deterministically distinguishes a valid active Tool,
a disabled Tool, **and** an invalid active Tool **without** changing Tool meaning.

## Applicable conditions

Apply **when** MCP builds **or** refreshes its callable frontier from TOOLS.

## Test case

Provide one valid active Tool with a machine contract, one explicitly disabled
Tool, **and** one active Tool with an invalid machine contract, **then** request one
frontier refresh.

## Acceptance criteria

pass **only** **when** exactly one unchanged endpoint is projected for the valid active
Tool **in** the candidate, the disabled Tool is omitted, the invalid active Tool is reported
explicitly, **and** no call semantics **or** mechanics are duplicated **in** MCP.
because the candidate includes an invalid active Tool, the refresh **must not**
publish a new current registry **or** present a previous registry as current,
under CA-R-1110.

## Failure disposition

Reject the candidate frontier **and** preserve the preceding valid frontier bytes
for recovery **when** the complete projection cannot validate; retaining those
bytes does **not** establish currentness.

## Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-METHOD--supply-the-active-tool-frontier-to-mcp.md)
