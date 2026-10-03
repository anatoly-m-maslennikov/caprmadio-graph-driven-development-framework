---
atom_id: CAPRMEDIO-REQU-030
subject_scopes:
  - requirement-topology
version: 9
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-029-CORE-REQUIREMENT--govern-each-scope-by-authority-mode
    - CA-R-833-CORE-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
---
# Require complete authority topology in strict mode

A scope in strict authority mode must maintain a complete, conflict-free active PRMEDO topology: every Principle and Core has at least one permitted active child unless GOVERNANCE registers its Type as terminal, the operative graph is acyclic, every edge follows the permitted tier and structural direction, and every operative relation target is active.
