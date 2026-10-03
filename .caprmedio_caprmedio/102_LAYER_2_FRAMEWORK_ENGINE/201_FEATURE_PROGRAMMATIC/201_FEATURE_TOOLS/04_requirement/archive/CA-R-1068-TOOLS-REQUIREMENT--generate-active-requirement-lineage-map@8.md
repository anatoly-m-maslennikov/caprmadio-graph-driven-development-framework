---
subjects:
  governs: "projection-pipeline"
  depends_on: []
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
---
# Generate active Requirement Lineage Map

The framework must provide one deterministic `project` Tool that writes the active-only Requirement lineage-section Projection as `<selected-structural-unit-root>/stg_requirements_lineage_sections.md`, assigns each non-orphan Requirement exactly once to the section named by its complete sorted set of reachable Principle Requirement numbers, orders section names as numeric vectors with a prefix before its extensions, orders each section by Principle, Core, and Standard tier and then numeric Requirement ID, places one Orphans section last, and renders exactly the linked `TYPE + ID`, exact first-H1 `Summary`, and direct authored `Child of` columns while resolving ancestry against the complete active project graph.
