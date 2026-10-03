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
# Reject Journal replay link

## Test case

**Fixture:** Point one Work Journal event at a nonexistent preceding event.

**Expected result:** Fail with the stable Journal-replay-link diagnostic and a non-zero exit.
