---
subjects:
  governs: "graph-app-access"
  depends_on: []
version: 10
updated_at: "2026-09-23 04:27:00 +0400"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Expose the current GRAPH_UI through Codex

`CODEX_PLUGIN` **must** let a Codex operator open **and** navigate the current `GRAPH_UI`, apply its governed filters, select graph nodes, **and** inspect their current source content, paths, digests, **and** provenance **without** copying the graph read model into plugin authority. The plugin **must** consume the GRAPH_UI's read-only interface, preserve stale **or** unavailable-source states, **and** **must not** mutate an Atom, Journal, Projection, graph source, **or** derived GRAPH_UI state through the viewing path.
