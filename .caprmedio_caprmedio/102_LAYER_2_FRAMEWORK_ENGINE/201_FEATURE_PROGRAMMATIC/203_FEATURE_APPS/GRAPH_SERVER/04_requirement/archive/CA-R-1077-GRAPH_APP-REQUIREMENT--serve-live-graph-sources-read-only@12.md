---
atom_id: CA-R-1077
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - artifact-query
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 12
updated_at: 2026-09-04 03:10:59 +0400
---
# Serve live graph sources read-only

The `GRAPH_APP` unit's local server must give its web pages strictly read-only access to registered current Atoms, Journals, Projections, and derived graph data, including persisted `GENERATE_ENTITY_GRAPH` Projection carriers; return source kind, non-authoritative status, source-frontier lineage, raw content, canonical path, and current digest where applicable; and reject inactive or unregistered targets, path traversal, symlink escape, authority substitution, and every mutation.
