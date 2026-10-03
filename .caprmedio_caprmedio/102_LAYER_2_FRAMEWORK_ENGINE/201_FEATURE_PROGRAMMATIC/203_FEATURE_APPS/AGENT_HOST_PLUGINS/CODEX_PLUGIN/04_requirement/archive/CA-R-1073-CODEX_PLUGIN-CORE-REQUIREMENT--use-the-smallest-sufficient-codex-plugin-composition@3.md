---
subject_scopes:
  - plugin-architecture
version: 3
updated_at: "2026-08-23 11:37:28"
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-712--define-codex-plugin-unit
---
# Use the smallest sufficient Codex plugin composition

`CODEX_PLUGIN` must contain only the Codex-host capabilities necessary to expose the current `GRAPH_APP` and route governed CAPRMEDIO work: skills for repeatable workflow guidance, a connection to the provider-neutral `MCP` unit only when Tool invocation is required, UI only when graph inspection or navigation materially benefits from it, and hooks only for Codex-specific lifecycle behavior. Every MCP-backed capability must remain usable without UI, and the plugin must reference rather than duplicate provider-neutral Skill, Tool, MCP, GRAPH_APP, or Methodology behavior.
