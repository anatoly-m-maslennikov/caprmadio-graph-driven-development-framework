---
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 3
updated_at: 2026-08-23 16:16:20 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094---
# Reconcile disabled and removed Tools

MCP regeneration must add every newly active valid Tool, exclude every explicitly disabled Tool, and remove every projection whose source Tool is no longer active or present. MCP must not maintain a second independent allowlist or lifecycle registry that can disagree with current project authority and Configuration.
