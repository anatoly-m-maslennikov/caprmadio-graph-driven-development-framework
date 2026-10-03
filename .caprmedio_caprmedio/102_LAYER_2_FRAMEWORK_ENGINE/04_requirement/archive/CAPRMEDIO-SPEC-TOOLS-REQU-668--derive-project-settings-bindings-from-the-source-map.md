---
subject_scopes:
  - project-settings
version: 2
updated_at: 2026-08-18 07:53:29
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-SPEC-REQU-499--define-tools-feature-scope
---
# Derive Project Settings bindings from the source map

The Project Settings generator must derive every emitted leaf setting's source bindings from `CAPRMEDIO-MAPS-001--project-settings-source-map`, flatten its branching YAML keys into canonical dotted TOML binding keys, refresh its exact source frontier, and reject missing, extra, duplicate, malformed, unresolved, or ambiguous entries before emitting the Project Settings Projection.
