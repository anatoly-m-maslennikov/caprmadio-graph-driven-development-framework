---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "artifact-query"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 17
updated_at: 2026-09-23 04:20:00 +0400
---
# Serve live graph sources read-only

the headless `GRAPH_SERVER` unit **must** give Tools, MCP clients, **and** optional interfaces strictly read-only access **to** registered current Atoms, Journals, Projections, **and** derived graph data, including persisted `GENERATE_ENTITY_GRAPH` Projection carriers; return source kind, non-authoritative status, source-frontier lineage, raw content, canonical path, **and** current digest **where** applicable; operate without `GRAPH_UI`; **and** reject inactive **or** unregistered targets, path traversal, symlink escape, authority substitution, **and** **every** mutation.
