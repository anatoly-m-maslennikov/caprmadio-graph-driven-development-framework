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
    - CAPRMEDIO-CNTR-005--supply-cumulative-authority-to-implementation
relation_kind: authority_input
endpoints:
  - role: provider
    identity: project
    origin: internal
  - role: provider
    identity: meta_layer
    origin: internal
  - role: provider
    identity: gov_layer
    origin: internal
  - role: provider
    identity: spec_layer
    origin: internal
  - role: consumer
    identity: native_realization
    origin: internal
---
# Supply cumulative authority to REALIZATION

Native Realization targets consume the complete applicable upstream authority set from PROJECT, META, GOV, SPEC, and their owning SPEC Feature scopes through the `authority_input` Contract.
