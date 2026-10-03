---
subject_scopes:
  - scope-topology
tier: core
version: 5
updated_at: 2026-09-05 00:44:25 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001
---
# Ordered realization topology

CAPRMEDIO must order the Project root as structural level `0` followed by numbered Layers. Every Layer may depend only on the Project root and lower-numbered Layers; same-Layer, higher-numbered, and forward dependencies are forbidden.
