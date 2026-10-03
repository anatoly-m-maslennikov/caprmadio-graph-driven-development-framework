---
subject_scopes:
  - scope-topology
version: 3
updated_at: 2026-08-18 00:26:51
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-META-REQU-281--share-canonical-features-across-spec-and-implementation
relation_kind: feature_realization
endpoints:
  - role: specification
    identity: spec_features
    origin: internal
  - role: realization
    identity: implementation_features
    origin: internal
---
# Map SPEC features to implementation realizations

Each canonical SPEC Feature scope corresponds to exactly one IMPLEMENTATION Feature scope with the same Feature name and order while remaining a distinct Layer-owned structural scope.
