---
subject_scopes:
  - projection-pipeline
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 7
updated_at: "2026-08-23 11:37:28"
relations:
  child_of:
    - CAPRMEDIO-METHODOLOGY-REQU-630--govern-current-non-authoritative-projections
---
# Generate active Requirement Subject Catalog

The framework must provide one deterministic `project` Tool that writes the active-only Subject Requirement Projection as `<selected-structural-unit-root>/stg_requirements_subjects.md`, groups non-orphan Requirements by their single authored Subject, orders each Subject by Principle, Core, and Standard tier and then numeric Requirement ID, places one Orphans section last, and renders exactly the linked `TYPE + ID`, exact first-H1 `Summary`, and direct authored `Child of` columns without filename fallback or inferred ancestry.
