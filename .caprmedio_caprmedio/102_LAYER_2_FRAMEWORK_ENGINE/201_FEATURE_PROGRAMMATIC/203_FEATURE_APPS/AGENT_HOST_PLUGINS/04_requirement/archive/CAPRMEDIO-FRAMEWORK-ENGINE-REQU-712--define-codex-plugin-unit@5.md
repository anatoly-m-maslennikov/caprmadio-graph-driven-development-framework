---
subject_scopes:
  - feature-boundary
tier: core
version: 5
updated_at: 2026-08-23 15:33:04 +0400
---
# Define the CODEX_PLUGIN unit

`CODEX_PLUGIN` with prefix `CODEX_PLUGIN` must be one `unordered_unit` owned immediately by `AGENT_HOST_PLUGINS` at Structural level `5`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN`, and realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/`; it owns the installable Codex-specific plugin package and Codex host wiring while referencing rather than redefining provider-neutral CAPRMEDIO behavior.
