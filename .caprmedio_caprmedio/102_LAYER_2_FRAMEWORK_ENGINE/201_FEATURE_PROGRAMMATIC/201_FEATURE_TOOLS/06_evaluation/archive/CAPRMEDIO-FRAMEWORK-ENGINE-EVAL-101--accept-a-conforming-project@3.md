---
artifact_subtype: qa_case
subject_scopes:
  - artifact-validation
version: 3
updated_at: 2026-08-23 16:40:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Accept a conforming project

## Test case

**Fixture:** Validate a complete conforming project fixture containing registered Atoms, settings, current Projections, replayable Journals, and valid provenance.

**Expected result:** Pass with exit `0`, an empty diagnostic set, and unchanged project bytes.
