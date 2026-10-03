---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile disabled and removed Tools

MCP regeneration must add every newly active valid Tool, exclude every explicitly disabled Tool, and remove every projection whose source Tool is no longer active or present. MCP must not maintain a second independent allowlist or lifecycle registry that can disagree with current project authority and Configuration.
