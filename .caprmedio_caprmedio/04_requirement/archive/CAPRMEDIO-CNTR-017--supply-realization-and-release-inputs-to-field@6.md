---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 6
updated_at: 2026-09-05 04:24:46 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relational_endpoints:
  controller:
    scope_unit: ./FIELD
    content_role: requirement
  followers:
    - scope_unit: ./FRAMEWORK_ENGINE
      content_roles:
        - implementation
    - scope_unit: ./RELEASES
      content_roles:
        - delivery
relations:
  child_of:
    - CA-R-881
  realization_input:
    - ./FRAMEWORK_ENGINE
    - ./RELEASES
---
# Supply REALIZATION and RELEASES inputs to FIELD

Native Realization and published releases supply the enacted inputs from which field observations arise through the `realization_input` Contract.
