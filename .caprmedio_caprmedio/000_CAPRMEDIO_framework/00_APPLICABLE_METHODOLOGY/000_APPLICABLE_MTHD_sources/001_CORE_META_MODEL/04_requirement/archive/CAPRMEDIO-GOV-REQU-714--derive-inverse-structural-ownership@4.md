---
subjects:
  - relation-model
  - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 4
updated_at: 2026-08-23 11:32:10
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706--make-structural-ownership-immediate-recursive-and-typed
---
# Derive inverse structural ownership

CAPRMEDIO MUST derive the inverse `structural_children` view from stored `structural_parent` relations and MUST NOT persist that inverse separately.
