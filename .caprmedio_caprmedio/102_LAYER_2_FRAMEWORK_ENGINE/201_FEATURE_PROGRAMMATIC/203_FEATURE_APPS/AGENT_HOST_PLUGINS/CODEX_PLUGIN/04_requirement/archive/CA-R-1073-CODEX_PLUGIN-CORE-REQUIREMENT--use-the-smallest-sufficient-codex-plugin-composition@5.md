---
subjects:
  declared:
    continuant:
      - plugin-architecture
version: 5
updated_at: 2026-08-23 16:16:20 +0400
---
# Use the smallest sufficient Codex plugin composition

`CODEX_PLUGIN` must contain only the Codex-host capabilities necessary to expose the current `GRAPH_APP` and route governed CAPRMEDIO work: skills for repeatable workflow guidance, a connection to the provider-neutral `MCP` unit only when Tool invocation is required, UI only when graph inspection or navigation materially benefits from it, and hooks only for Codex-specific lifecycle behavior. Every MCP-backed capability must remain usable without UI, and the plugin must reference rather than duplicate provider-neutral Skill, Tool, MCP, GRAPH_APP, or Methodology behavior.
