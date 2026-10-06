---
subject_scopes:
  - relation-model
version: 3
updated_at: 2026-08-22 02:37:15
relations:
  child_of:
    - CA-R-873-REQUIREMENT-BSEED_SEMANTICS--give-each-relational-atom-one-semantic-controller
    - CA-R-876-REQUIREMENT-BSEED_SEMANTICS--separate-control-dependency-and-result-flow
---
# Encode Contract endpoints

Every Contract Atom encodes semantic control in this frontmatter structure:

```yaml
relational_endpoints:
  controller:
    scope_unit: ./FRAMEWORK_ENGINE
    content_role: requirement
  followers:
    - scope_unit: ./FRAMEWORK_METHODOLOGY
      content_roles:
        - method
```

`controller` occurs exactly once. `followers` contains one or more unique descriptors. Every `scope_unit` uses the governed relative-reference grammar and the exact full registered Scope Unit name. The controller declares one `content_role`; each follower declares one or more `content_roles`. Content-role values use their full registered names.

This structure identifies the nodes and role projections governed by the Contract; it is not a graph relation and has no inverse. The former `contract_for` and `controls_endpoint` relation kinds are invalid. Dependency, authority, information-flow, result-flow, realization, and obligation-bearing meanings remain separately registered relations under `relations`.
