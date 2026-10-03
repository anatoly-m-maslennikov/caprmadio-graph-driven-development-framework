---
subjects:
  governs:
    continuant:
      - installed-plugin-validation
version: 7
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1075
  derived_from:
    - CA-A-057
---
# Verify the installed Codex plugin

Verify the installed Codex plugin through this procedure:

1. Validate each packaged skill, MCP tool, UI resource, and hook independently before testing the complete plugin; when an MCP server is present, exercise representative inputs, edge cases, invalid inputs, empty results, authorization behavior, schemas, and model-readable results.
2. Add the repository marketplace as a local source, install the packaged plugin from that source, restart the host when required to refresh local package files, and begin a fresh Codex conversation with the plugin enabled.
3. Run a versioned evaluation set containing direct requests, indirect requests with the same goal, follow-ups that depend on earlier results, unsupported requests, and declared boundary cases.
4. For every request, record whether the expected skill or tool activated, whether arguments and results were correct, whether bundled resources resolved from the installed package, whether required steps completed, and whether authorization or confirmation behavior matched the requested action.
5. When MCP or UI is present, also verify tool discovery, skill-to-tool routing, authentication after installation, model-readable fallback behavior, UI rendering, and completion of the combined workflow from start to finish.
6. Treat source-package validity, marketplace availability, successful installation, and proved runtime invocation as separate outcomes; accept the plugin only when the fresh installed path supplies replayable evidence for each claimed outcome.
