---
subjects:
  governs: "graph-app-access"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Expose the current GRAPH_APP through Codex

`CODEX_PLUGIN` must let a Codex operator open and navigate the current `GRAPH_APP`, apply its governed filters, select graph nodes, and inspect their current source content, paths, digests, and provenance without copying the graph read model into plugin authority. The plugin must consume the GRAPH_APP's read-only interface, preserve stale or unavailable-source states, and must not mutate an Atom, Journal, Projection, graph source, or derived GRAPH_APP state through the viewing path.
