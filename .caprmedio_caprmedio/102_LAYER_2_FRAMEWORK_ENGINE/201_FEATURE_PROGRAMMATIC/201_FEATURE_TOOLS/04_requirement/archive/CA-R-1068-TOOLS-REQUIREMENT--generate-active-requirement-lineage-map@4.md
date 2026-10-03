---
subject_scopes:
  - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: "2026-08-23 11:37:28"
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-630--govern-current-non-authoritative-projections
---
# Generate active Requirement Lineage Map

The framework must provide one deterministic `project` Tool that writes the active-only Requirement lineage-section Projection as `<selected-structural-unit-root>/stg_requirements_lineage_sections.md`, assigns each non-orphan Requirement exactly once to the section named by its complete sorted set of reachable Principle Requirement numbers, orders section names as numeric vectors with a prefix before its extensions, orders each section by Principle, Core, and Standard tier and then numeric Requirement ID, places one Orphans section last, and renders exactly the linked `TYPE + ID`, exact first-H1 `Summary`, and direct authored `Child of` columns while resolving ancestry against the complete active project graph.
