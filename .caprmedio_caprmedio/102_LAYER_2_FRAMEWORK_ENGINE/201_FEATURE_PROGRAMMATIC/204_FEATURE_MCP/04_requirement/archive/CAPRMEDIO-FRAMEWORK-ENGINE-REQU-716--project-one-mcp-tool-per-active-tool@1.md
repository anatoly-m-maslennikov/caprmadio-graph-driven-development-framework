---
subject_scopes:
  - framework-engine-mcp
version: 1
updated_at: 2026-08-22 02:06:02
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-713--define-mcp-unit
    - CAPRMEDIO-FRAMEWORK-ENGINE-CNTR-001--supply-active-tools-to-mcp
---
# Project one MCP tool per active Tool

MCP must project exactly one callable MCP tool for every valid active immediate Tool unit and no callable MCP tool without one such source Tool. The MCP tool identity must derive stably from the canonical Tool identity; aliases, accidental duplicates, implicit aggregation, and splitting one Tool into multiple public MCP identities are prohibited unless separately governed by new Tool authority.
