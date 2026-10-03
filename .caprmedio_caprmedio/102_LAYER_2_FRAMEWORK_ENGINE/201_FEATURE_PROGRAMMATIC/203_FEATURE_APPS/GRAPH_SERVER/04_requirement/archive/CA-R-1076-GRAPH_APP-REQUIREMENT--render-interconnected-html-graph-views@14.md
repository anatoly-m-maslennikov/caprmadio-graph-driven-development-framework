---
atom_id: CA-R-1076
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "projection-pipeline"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 14
updated_at: "2026-09-16 23:48:40 +0000"
---
# Render interconnected HTML graph views

The `GRAPH_APP` unit must render interconnected HTML graph views from its current derived read model and the governed source frontier behind that model. It may also consume a persisted `GENERATE_ENTITY_GRAPH` Projection for declared Terms, their direct-parent tree, direct dependency graph, and complete dependency-Term closure. The views must provide short and detailed node presentation, tier, current Structural-unit, Content-role, and Type filters, orphan and cycle visibility controls, source lineage, unknown-region diagnostics, and access to current Atom content without treating any Projection as governed authority or modifying authority.
