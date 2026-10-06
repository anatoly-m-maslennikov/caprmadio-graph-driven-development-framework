---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-125--three-artifact-forms-with-generated-projections
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Keep Projections versionless

A Projection has no independent revision ordinal because its declared source frontier, generator, and configuration define its reproducible state. It records when it was last rebuilt, while currentness is derived from those declared inputs and never from the rebuild time alone.
