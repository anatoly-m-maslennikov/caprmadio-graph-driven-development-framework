---
subject_scopes:
  - scope-topology
semantic_shape: relational
version: 8
updated_at: "2026-09-09 21:33:29 +0400"
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relational_endpoints:
  controller:
    scope_unit: ./AGENTIC/SKILLS
    content_role: requirement
  followers:
    - scope_unit: ./PROGRAMMATIC/MCP
      content_roles:
        - delivery
relations:
  child_of:
    - CA-R-881
  realization_input:
    - ./PROGRAMMATIC/MCP
---
# Supply the MCP Tool interface to SKILLS

MCP supplies SKILLS with the current generated discovery **and** invocation interface for active Tools. Skills select **and** use that interface **without** redefining Tool behavior, while MCP preserves each Tool's identity, accepted inputs, structured outputs, **and** failure meaning.
