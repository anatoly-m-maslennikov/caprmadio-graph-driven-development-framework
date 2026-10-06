---
subject_scopes:
  - lifecycle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 1
updated_at: 2026-08-17 07:52:10
relations:
  child_of:
    - CAPRMEDIO-META-REQU-170--govern-ops-factual-admission-lifecycle
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Place Ops records by factual admission

Within each `09_ops/` directory, the optional `drafts/` directory holds governed Ops Atoms whose asserted facts are not yet admitted, the role root holds admitted factual records, and `archive/` holds invalidated, duplicated, or replaced records. This placement model is exhaustive; handling is represented separately and does not create a `handled/` lifecycle directory.
