---
atom_id: CAPRMEDIO-REQU-621
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032-CORE-REQUIREMENT--let-parents-own-immediate-child-goals
---
# Place framework settings in the root REALIZATION

The CAPRMEDIO framework repository must own `caprmedio_framework_settings.toml` in its root REALIZATION and expose that same carrier through a relative symlink under `.caprmedio/000_caprmedio_framework` rather than through a copied mirror.
