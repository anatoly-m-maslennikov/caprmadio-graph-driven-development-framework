---
subject_scopes:
  - plugin-packaging
version: 5
updated_at: 2026-08-23 17:40:00 +0400
relations:
  method_for:
    - CA-R-1074
  derived_from:
    - CA-A-057
---
# Package the Codex plugin

Package the Codex plugin through this procedure:

1. Create one plugin root with a stable kebab-case identity and a required `.codex-plugin/plugin.json` manifest containing the current plugin version, description, and relative paths to its packaged capabilities.
2. Place reusable workflows under `skills/`; add `.app.json` only for a registered MCP server connection, `.mcp.json` only for an MCP server distributed with the plugin, and assets or lifecycle hooks only when selected by the plugin-shape decision.
3. Keep manifest references relative to and contained by the plugin root, keep credentials and mutable runtime state outside the package, and ensure every declared file or directory exists.
4. Add or update one repository marketplace entry at `.agents/plugins/marketplace.json`, point its `source.path` to the plugin root with a `./`-prefixed path relative to the marketplace root, and declare installation policy, authentication policy, and category.
5. Verify that the marketplace plugin name matches the manifest identity, the advertised version and description match the packaged content, and optional MCP, UI, asset, and hook references match the selected plugin shape.
6. Produce a distributable package without redefining the provider-neutral CAPRMEDIO authority referenced by its skills or tools.
