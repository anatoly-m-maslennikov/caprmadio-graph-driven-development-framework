---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-18 23:09:21
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706--make-structural-ownership-immediate-recursive-and-typed
    - CAPRMEDIO-META-REQU-707--support-layer-like-and-feature-like-structural-decomposition
---
# Match structural ownership relations to child kind

A layer-like structural unit must use `layer_of`, and a feature-like structural unit must use `feature_of`; neither relation may originate from the other structural kind.
