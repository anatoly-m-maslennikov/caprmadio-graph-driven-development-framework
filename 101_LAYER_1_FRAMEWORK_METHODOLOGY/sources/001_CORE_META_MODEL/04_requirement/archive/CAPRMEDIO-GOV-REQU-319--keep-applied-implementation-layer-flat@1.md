---
subject_scopes:
  - layout
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  override_of:
    - CAPRMEDIO-GOV-REQU-475--repeat-ordered-role-folders-in-every-scope
---
# Keep the applied Implementation layer flat

The applied project layer `400_LAYER_4_IMPLEMENTATION` (`105_LAYER_IMPL`) contains no subfolders for now. Any governed carriers assigned to that layer live directly in its root.

This is a narrow project-layout exception to the recursive Content-role folders required by `CAPRMEDIO-GOV-REQU-475--repeat-ordered-role-folders-in-every-scope`. It does not flatten the reusable root methodology, the installed external methodology, another applied layer, a feature scope, or native implementation outside `.caprmedio/`.

Bootstrap, discovery, routing, migration, and validation reproduce and accept this flat applied-layer boundary. A later Requirement must explicitly replace this one before introducing subfolders under `105_LAYER_IMPL`.
