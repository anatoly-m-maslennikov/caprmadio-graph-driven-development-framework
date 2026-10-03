---
cce_version: cce_1
cce_form: obligation
subjects:
  - settings
version: 8
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-META-REQU-627--bind-every-project-scope-unit-graph-value-to-exact-sources
---
# Encode Project Scope Unit Graph generation metadata

Each Project Scope Unit Graph Projection carrier MUST encode `updated_at`, generator identity and digest, the exact Project Configuration Atom identity and Revision, and only the source bindings needed to explain emitted Project Scope Unit Graph values. It MUST NOT encode a blanket source frontier, a source-frontier digest, a governed-file inventory, or an unrelated Journal carrier, and it MUST NOT expose projected values as editable settings.
