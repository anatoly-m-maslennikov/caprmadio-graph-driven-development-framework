---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - methodology
version: 10
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CA-R-1050
  child_of:
    - CA-R-1054
---
# Bounded scripted migrations

A migration script MUST be scoped to named carriers or exact patterns, fail when an expected source pattern is absent, and leave reviewable repository diffs. It does not rewrite immutable atomic artifacts unless a separately accepted carrier migration explicitly authorizes that transformation.
