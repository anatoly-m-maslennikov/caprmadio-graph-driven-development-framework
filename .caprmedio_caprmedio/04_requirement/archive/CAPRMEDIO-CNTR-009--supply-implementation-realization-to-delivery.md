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
  - role: consumer
    identity: delivery_layer
    origin: internal
---
# Supply implementation realization to delivery

IMPLEMENTATION supplies realized project artifacts to DELIVERY through the `realization_input` Contract.
