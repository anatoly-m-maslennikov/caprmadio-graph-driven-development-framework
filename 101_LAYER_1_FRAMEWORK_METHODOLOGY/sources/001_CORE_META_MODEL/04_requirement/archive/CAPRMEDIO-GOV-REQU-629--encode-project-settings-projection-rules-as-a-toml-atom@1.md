---
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-18 03:25:18
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-619--classify-framework-settings-as-an-implementation-atom
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
    - CAPRMEDIO-REQU-628--place-project-settings-projection-rules-in-the-root-realization
---
# Encode Project Settings Projection rules as a TOML Atom

`caprmedio_project_settings_projection_rules.toml` must define setting keys, project-authority source selectors, cardinality, composition, precedence, and validation without containing current-project Atom identities; the generated Project Settings Projection must record the exact source Atom revisions and rules-Atom revision used for every emitted value.
