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
# Reject structural parent address

## Test case

**Fixture:** Give one structural scope a directory address inconsistent with its registered parent.

**Expected result:** Fail with the stable structural-parent-address diagnostic and a non-zero exit.
