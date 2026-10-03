---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 5
updated_at: 2026-08-22 02:37:15
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
    - CA-R-881-REQUIREMENT--own-cross-unit-relational-atoms-at-the-common-scope
  realization_input:
    - ./FRAMEWORK_ENGINE
    - ./RELEASES
---
# Supply REALIZATION and RELEASES inputs to FIELD

Native Realization and published releases supply the enacted inputs from which field observations arise through the `realization_input` Contract.
