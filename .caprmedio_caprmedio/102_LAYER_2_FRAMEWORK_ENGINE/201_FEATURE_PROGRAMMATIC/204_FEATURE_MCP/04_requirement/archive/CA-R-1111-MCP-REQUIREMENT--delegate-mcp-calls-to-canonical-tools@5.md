---
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 5
updated_at: 2026-08-23 16:24:28 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
---
# Delegate MCP calls to canonical Tools

Every MCP invocation must delegate to the selected canonical Tool executable and must not reimplement Tool decisions, project meaning, target resolution, validation, mutation, recovery behavior, or lifecycle semantics inside the MCP carrier. MCP owns only transport admission, canonical Tool selection, delegation, and result transport.

Every Finder and every Doer dry run must remain independently executable without MCP. A direct executable invocation of a CAPRMEDIO Markdown Atom Doer with `--apply` must reject the request unless it carries the authorized project-local MCP delegation and its sealed Initiative action envelope. Introducing MCP must not create a Tool dependency on MCP or another APPS unit.
