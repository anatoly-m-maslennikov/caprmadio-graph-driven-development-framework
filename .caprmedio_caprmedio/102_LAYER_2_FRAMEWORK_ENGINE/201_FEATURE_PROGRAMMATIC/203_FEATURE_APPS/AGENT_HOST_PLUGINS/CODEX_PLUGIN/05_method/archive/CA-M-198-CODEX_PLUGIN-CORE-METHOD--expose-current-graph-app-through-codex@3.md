---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - graph-app-access
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1103
  derived_from:
    - CA-A-058
---
# Expose the current GRAPH_APP through Codex

## Applicable when

Use this Method when a Codex operator needs to inspect the current Project Graph through the installed plugin.

## Procedure

1. Connect the plugin to the read-only GRAPH_APP interface and obtain its current source frontier and rebuild status.
2. Expose graph navigation, filtering, node selection, and node inspection without copying graph authority into the plugin.
3. For every selected node, show its source path, current digest, source content, and available provenance.
4. Preserve explicit stale, unavailable, missing-source, and rebuild-in-progress states in the Codex-facing response.
5. Reject all graph mutations through this interface and route any requested change to separately governed Skills or Tools.

## Outcome

Codex presents an attributable read-only view of the current GRAPH_APP state and its source carriers.

## Failure or stop

Return the precise stale or unavailable state when GRAPH_APP cannot prove currentness; never synthesize current graph content or mutate sources.
