---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-18 02:06:50
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
  replacement_of:
    - CAPRMEDIO-CNTR-007--supply-cumulative-authority-to-ops
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
    identity: field_layer
    origin: internal
---
# Supply cumulative authority to FIELD

FIELD consumes the complete applicable upstream normative authority set from PROJECT, META, GOV, and SPEC through the `authority_input` Contract.
