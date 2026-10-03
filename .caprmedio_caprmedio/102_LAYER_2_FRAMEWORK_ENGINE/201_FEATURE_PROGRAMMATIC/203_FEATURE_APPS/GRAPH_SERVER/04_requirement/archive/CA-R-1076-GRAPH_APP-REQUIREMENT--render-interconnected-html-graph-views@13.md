---
atom_id: CA-R-1076
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 13
updated_at: 2026-09-04 03:10:59 +0400
---
# Render interconnected HTML graph views

The `GRAPH_APP` unit must render interconnected HTML graph views from its current derived read model and the governed source frontier behind that model. It may also consume a persisted `GENERATE_ENTITY_GRAPH` Projection for declared Terms, their direct-parent tree, direct dependency graph, and complete dependency-Term closure. The views must provide short and detailed node presentation, tier, current Structural-unit, Content-role, and Type filters, orphan and cycle visibility controls, source lineage, unknown-region diagnostics, and access to current Atom content without treating any Projection as governed authority or modifying authority.
