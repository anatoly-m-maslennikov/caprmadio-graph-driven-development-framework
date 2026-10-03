---
atom_id: CA-M-193
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1096
  derived_from:
    - CA-A-058
---
# Supply the active Tool frontier to MCP

## Applicable when

Apply when MCP builds or refreshes the callable frontier supplied by TOOLS.

## Procedure

1. Enumerate the complete current set of active immediate Tool units from the
   canonical TOOLS frontier.
2. Read and validate each active Tool's machine-invocation contract without
   inferring missing meaning from its code or runtime state.
3. Project exactly one stable callable endpoint for each valid active Tool.
4. Omit inactive and explicitly disabled Tools; report every invalid active
   Tool as a diagnostic rather than silently omitting it.
5. Delegate each admitted call to the Tool without duplicating or changing its
   meaning, inputs, outcomes, or mechanics.
6. Replace the exposed frontier only after the complete candidate projection
   validates; preserve the preceding valid frontier when refresh fails.

## Outcome

MCP exposes one complete, deterministic projection of valid active Tools and
remains a replaceable interface rather than a second Tool authority.

## Failure or stop

Stop refresh and preserve the preceding valid frontier when active Tool
enumeration is incomplete, endpoint identities collide, or a machine contract
is missing or invalid. Reject a call that cannot delegate unchanged.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
