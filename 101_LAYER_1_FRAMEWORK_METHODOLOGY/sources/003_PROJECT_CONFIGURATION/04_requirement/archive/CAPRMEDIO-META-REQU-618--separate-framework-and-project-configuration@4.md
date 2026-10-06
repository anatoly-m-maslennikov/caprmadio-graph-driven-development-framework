---
subject_scopes:
  - semantics
tier: core
version: 4
updated_at: 2026-08-21 00:26:09
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-832-REQUIREMENT--select-optional-capabilities-through-configuration
---
# Separate Project Configuration from Project Graph State

CAPRMEDIO must distinguish the human-editable Project Configuration Atom from generated Project Graph State Projections. Only the Configuration Atom is settings and owns operator-selected values; Graph State Projections are read-only derived views and never configuration authority.
