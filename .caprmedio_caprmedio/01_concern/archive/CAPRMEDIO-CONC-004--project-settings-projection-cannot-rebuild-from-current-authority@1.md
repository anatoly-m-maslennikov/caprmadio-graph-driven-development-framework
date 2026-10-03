---
artifact_subtype: problem
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-22 03:19:24
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  concern_about:
    - CAPRMEDIO-REQU-622--establish-project-configuration-through-rmed
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-GOV-REQU-626--encode-project-settings-as-a-generated-toml-projection
    - CAPRMEDIO-GOV-REQU-669--register-project-settings-source-map-projection
---
# Project Settings Projection cannot rebuild from current authority

The current Project Settings generator requires one active RMED contribution for `schema_version`, but current authority supplies no such contribution. The same generator still emits legacy Journal records without the governed Actor type. Until both defects are repaired, Project Settings and its Source Map cannot be regenerated faithfully and remain stale generated Projections; P-020 Action 14 owns their repair and rebuild.
