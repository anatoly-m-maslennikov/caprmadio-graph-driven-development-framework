---
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 1
updated_at: 2026-08-17 07:46:32
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-288--give-atoms-explicit-revision-ordinals
  child_of:
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Atoms have version and updated at

Every Atom revision has one positive monotonic `version` scoped to its stable Artifact identity and one unambiguous `updated_at` identifying when that revision was created. Creation assigns version one, each governed carrier-content edit advances the version exactly once, replacement assigns version one to the successor identity, and a path-only lifecycle move preserves both properties.
