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
# Reconcile disabled and removed Tools

MCP regeneration must add every newly active valid Tool, exclude every explicitly disabled Tool, and remove every projection whose source Tool is no longer active or present. MCP must not maintain a second independent allowlist or lifecycle registry that can disagree with current project authority and Configuration.
