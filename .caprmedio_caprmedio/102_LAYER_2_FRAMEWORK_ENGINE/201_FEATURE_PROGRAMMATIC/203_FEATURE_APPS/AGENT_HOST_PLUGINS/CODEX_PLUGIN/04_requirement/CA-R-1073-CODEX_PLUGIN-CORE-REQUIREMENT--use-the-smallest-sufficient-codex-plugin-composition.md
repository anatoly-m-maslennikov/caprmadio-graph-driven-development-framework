---
subjects:
  governs: "plugin-architecture"
  depends_on: []
version: 10
updated_at: "2026-09-23 04:27:00 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Use the smallest sufficient Codex plugin composition

`CODEX_PLUGIN` **must** contain **only** the Codex-host capabilities necessary **to** expose the current `GRAPH_UI` **and** route governed CAPRMEDIO work: skills for repeatable workflow guidance, a connection **to** the provider-neutral `MCP` unit **only** **when** Tool invocation is required, UI **only** **when** graph inspection **or** navigation materially benefits from it, **and** hooks **only** for Codex-specific lifecycle behavior. Every MCP-backed capability **must** remain usable **without** UI, **and** the plugin **must** reference rather than duplicate provider-neutral Skill, Tool, MCP, GRAPH_UI, **or** Methodology behavior.
