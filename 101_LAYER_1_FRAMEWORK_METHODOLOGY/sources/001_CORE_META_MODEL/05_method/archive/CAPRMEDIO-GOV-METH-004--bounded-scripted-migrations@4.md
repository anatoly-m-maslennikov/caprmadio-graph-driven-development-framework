---
subject_scopes:
  - methodology
tier: core
version: 4
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  relates_to:
    - CAPRMEDIO-GOV-REQU-731--place-immutable-atom-id-before-mutable-scope-path
    - CAPRMEDIO-GOV-REQU-733--compose-readable-atom-class-short-names
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Bounded scripted migrations

A migration script must be scoped to named carriers or exact patterns, fail
when an expected source pattern is absent, and leave reviewable repository
diffs. It does not rewrite immutable atomic artifacts unless a separately
accepted carrier migration explicitly authorizes that transformation.
