---
artifact_subtype: qa_case
subject_scopes:
  - artifact-validation
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-535--validate-project-integrity
---
# Accept a conforming project

## Test case

**Fixture:** Validate a complete conforming project fixture containing registered Atoms, settings, current Projections, replayable Journals, and valid provenance.

**Expected result:** Pass with exit `0`, an empty diagnostic set, and unchanged project bytes.
