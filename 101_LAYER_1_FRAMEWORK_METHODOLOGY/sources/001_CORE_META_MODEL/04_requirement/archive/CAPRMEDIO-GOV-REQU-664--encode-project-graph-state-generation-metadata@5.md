---
subject_scopes:
  - settings
version: 5
updated_at: 2026-08-21 03:26:58
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
---
# Encode Project Graph State generation metadata

Each Project Graph State Projection carrier must encode `updated_at`, generator identity and digest, the exact Project Configuration Atom identity and Revision, and only the source bindings needed to explain emitted Graph State values. It must not encode a blanket source frontier, a source-frontier digest, a governed-file inventory, or an unrelated Journal carrier, and it must not expose projected values as editable settings.
