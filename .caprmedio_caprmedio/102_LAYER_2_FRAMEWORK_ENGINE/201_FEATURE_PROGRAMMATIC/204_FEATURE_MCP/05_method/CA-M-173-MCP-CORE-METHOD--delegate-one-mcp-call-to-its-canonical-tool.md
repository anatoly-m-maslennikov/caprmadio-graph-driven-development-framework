---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 5
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1111
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Delegate one MCP call to its canonical Tool

## Applicable when

Apply **when** MCP receives one validated request for an exposed Tool.

## Procedure

1. Select the canonical Tool executable from the current registry.
2. Forward the admitted request **without** reimplementing target resolution, project meaning, validation, mutation, recovery, **or** lifecycle semantics.
3. Transport the Tool result as a Tool result, retaining **every** failure **and** side-effect boundary.

## Outcome

MCP is a transport boundary **and** the canonical Tool remains the sole operation owner.

## Failure or stop

Stop **when** canonical selection, request validation, **or** delegated execution fails; do **not** substitute MCP behavior.
