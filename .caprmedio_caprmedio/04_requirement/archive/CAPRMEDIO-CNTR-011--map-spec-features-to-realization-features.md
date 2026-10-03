---
subject_scopes:
  - scope-topology
version: 2
updated_at: 2026-08-18 20:48:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-CNTR-001--map-spec-features-to-implementation-realizations
relation_kind: feature_realization
endpoints:
  - role: specification
    identity: spec_features
    origin: internal
  - role: realization
    identity: native_realization
    origin: internal
---
# Map SPEC Features to REALIZATION Features

Each canonical SPEC Feature scope declares its applicable native Realization targets through the `feature_realization` Contract without making those targets a parallel structural scope.
