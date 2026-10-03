---
subjects:
  - relation-model
  - atom-boundary
version: 3
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706--make-structural-ownership-immediate-recursive-and-typed
---
# Derive inverse structural ownership

CAPRMEDIO must derive the inverse `structural_children` view from stored `structural_parent` relations and must not persist that inverse separately.
