---
subject_scopes:
  - scope-topology
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-153--preserve-bounded-meaning-across-structural-scales
    - CAPRMEDIO-META-REQU-159--allow-scope-sets-to-vary-by-structural-owner
    - CAPRMEDIO-CNTR-001--map-spec-features-to-implementation-realizations
---
# Use flat Layer-owned Feature scopes

An explicitly structured CAPRMEDIO project has one ordered sequence of Layers. Every explicit Feature belongs to exactly one Layer and cannot exist outside a Layer or belong to several Layers.

Layer and Feature scope directories are physical siblings. Their governed numeric addresses encode semantic containment: every Feature address identifies its sole parent Layer and its order within that Layer.
