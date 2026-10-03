---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:02:58
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
relation_kind: realization_input
endpoints:
  - role: provider
    identity: implementation_layer
    origin: internal
  - role: provider
    identity: delivery_layer
    origin: internal
  - role: consumer
    identity: ops_layer
    origin: internal
---
# Supply realization inputs to Ops

IMPLEMENTATION and DELIVERY supply realized project artifacts and enacted delivery outputs to OPS through the `realization_input` Contract.
