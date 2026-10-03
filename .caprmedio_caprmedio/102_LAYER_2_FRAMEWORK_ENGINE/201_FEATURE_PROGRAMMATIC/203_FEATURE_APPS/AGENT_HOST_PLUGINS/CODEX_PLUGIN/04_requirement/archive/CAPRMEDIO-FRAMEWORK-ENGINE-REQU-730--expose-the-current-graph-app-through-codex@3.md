---
subject_scopes:
  - graph-app-access
tier: core
version: 3
updated_at: 2026-08-23 11:39:04
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-712--define-codex-plugin-unit
---
# Expose the current GRAPH_APP through Codex

`CODEX_PLUGIN` must let a Codex operator open and navigate the current `GRAPH_APP`, apply its governed filters, select graph nodes, and inspect their current source content, paths, digests, and provenance without copying the graph read model into plugin authority. The plugin must consume the GRAPH_APP's read-only interface, preserve stale or unavailable-source states, and must not mutate an Atom, Journal, Projection, graph source, or derived GRAPH_APP state through the viewing path.
