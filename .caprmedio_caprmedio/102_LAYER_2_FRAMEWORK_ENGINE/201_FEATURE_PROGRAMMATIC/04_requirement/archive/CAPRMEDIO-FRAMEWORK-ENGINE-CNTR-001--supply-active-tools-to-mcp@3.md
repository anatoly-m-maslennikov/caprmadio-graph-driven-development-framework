---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 3
updated_at: 2026-08-23 15:33:04 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relational_endpoints:
  controller:
    scope_unit: ./MCP
    content_role: requirement
  followers:
    - scope_unit: ./TOOLS
      content_roles:
        - delivery
relations:
  realization_input:
    - ./TOOLS
  depends_on:
    - ./TOOLS
---
# Supply active TOOLS to MCP

TOOLS supplies MCP with the complete current set of active immediate Tool units and each Tool's machine-invocation contract. MCP must deterministically project exactly one callable endpoint for every valid active Tool, omit inactive or disabled Tools, report every invalid active Tool explicitly, and delegate execution without duplicating or changing Tool meaning or mechanics.
