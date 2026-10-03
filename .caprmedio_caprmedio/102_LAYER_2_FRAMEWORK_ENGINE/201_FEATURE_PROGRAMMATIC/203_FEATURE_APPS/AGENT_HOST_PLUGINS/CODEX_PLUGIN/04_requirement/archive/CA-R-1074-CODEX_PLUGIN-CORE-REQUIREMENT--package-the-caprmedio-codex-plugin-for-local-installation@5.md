---
subjects:
  declared:
    continuant:
      - plugin-packaging
version: 5
updated_at: 2026-08-23 16:16:20 +0400
---
# Package the CAPRMEDIO Codex plugin for local installation

`CODEX_PLUGIN` must be one versioned installable package with a stable kebab-case identity, a required `.codex-plugin/plugin.json` manifest, contained relative references to every bundled skill and optional MCP, UI, asset, or hook resource, and one repository-local marketplace entry through which Codex can discover and install the package. Credentials and mutable runtime state must remain outside the package, every declared resource must resolve after installation, and the advertised identity, version, description, and capabilities must match the packaged content.
