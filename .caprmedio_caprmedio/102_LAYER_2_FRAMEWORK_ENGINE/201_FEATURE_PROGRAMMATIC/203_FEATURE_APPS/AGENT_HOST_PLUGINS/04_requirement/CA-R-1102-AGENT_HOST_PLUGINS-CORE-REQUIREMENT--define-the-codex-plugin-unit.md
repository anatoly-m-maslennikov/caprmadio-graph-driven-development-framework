---
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 11
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define the CODEX_PLUGIN unit

`CODEX_PLUGIN` with prefix `CODEX_PLUGIN` **must** be one `unordered_unit` owned immediately by `AGENT_HOST_PLUGINS` at Structural level `5`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN`, **and** realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/`; it owns the installable Codex-specific plugin package **and** Codex host wiring while referencing rather than redefining provider-neutral CAPRMEDIO behavior.
