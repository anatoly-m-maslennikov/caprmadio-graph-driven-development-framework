---
subjects:
  - settings
version: 10
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-666--register-project-settings-source-map-atom
    - CAPRMEDIO-GOV-REQU-667--bind-project-settings-source-map-revisions-in-the-work-journal
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
    - CA-R-1054
---
# Register the Project Scope Unit Graph Sources Projection

GOVERNANCE must register the versionless internal Project Scope Unit Graph Sources Projection at `.caprmedio/project_scope_unit_graph_sources.projection.toml` with Content role `implementation` and Type `map`. It maps every emitted Project Scope Unit Graph value to the exact Project Configuration Atom revision and any Atom revisions or Journal records that directly contribute that value, records `updated_at`, omits a blanket source frontier, and is never read as authority for values or source selection.

This Projection uses TOML. Its required representation is a compact mapping from emitted Project Scope Unit Graph paths to exact source references. The Projection remains generated, read-only, and non-authoritative; it does not create a parallel writable configuration source.
