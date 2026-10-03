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
    - CA-R-1136
---
# Reject RMED subject cardinality

## Test case

**Fixture:** Give an RMED Atom two subject tokens.

**Expected result:** Fail with the stable RMED-subject-cardinality diagnostic and a non-zero exit.
