---
artifact_subtype: qa_case
subject_scopes:
  - project-settings
version: 5
updated_at: 2026-08-23 11:39:04
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1070
---
# Keep operator settings out of the Scope Unit Graph generator

## Test case

**Fixture:** Inspect the registered generator implementation and change one
operator-selected value only in the governed Project Configuration Atom.

**Expected result:** The generator contains no project-specific effective-value
catalog or ordinary-Atom `project_settings` input. Rebuilding changes the
projected value and binding solely from the Configuration revision, current
graph structure, admitted Project Scope Unit Graph sources, and Journal inputs.
