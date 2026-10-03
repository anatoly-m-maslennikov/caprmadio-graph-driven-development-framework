---
subject_scopes:
  - scope-topology
version: 3
updated_at: 2026-08-22 01:56:15
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-032--assign-immediate-child-scope-ownership
---
# Classify Project Features as unordered units

Every CAPRMEDIO Feature is an `unordered_unit`, is owned by exactly one immediate Structural unit, and has no `local_order`. A Feature owned directly by CAPRMEDIO is at Structural level `1`; a Layer-owned Feature is at Structural level `2`.
