---
subject_scopes:
  - artifact-query
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 9
updated_at: 2026-08-23 15:33:04 +0400
---
# Serve live graph sources read-only

The `GRAPH_APP` unit's local server must give its web pages strictly read-only access to registered current Atoms, Journals, Projections, and derived graph data; return source kind, raw content, canonical path, and current digest where applicable; and reject inactive or unregistered targets, path traversal, symlink escape, and every mutation.
