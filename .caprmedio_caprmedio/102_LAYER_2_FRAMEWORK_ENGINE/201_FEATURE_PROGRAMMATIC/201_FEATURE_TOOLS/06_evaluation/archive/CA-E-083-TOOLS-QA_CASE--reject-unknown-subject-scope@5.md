---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1136
---
# Reject unknown subject scope

## Test case

**Fixture:** Add one subject token outside the vocabulary registered for the carrier's structural scope.

**Expected result:** Fail with the stable unknown-subject-scope diagnostic and a non-zero exit.
