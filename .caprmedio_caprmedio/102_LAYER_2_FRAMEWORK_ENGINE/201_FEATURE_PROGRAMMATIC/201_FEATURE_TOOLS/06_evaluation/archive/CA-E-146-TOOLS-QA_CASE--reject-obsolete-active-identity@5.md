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
    - CA-R-1137
---
# Reject obsolete active identity

## Test case

**Fixture:** Retain an obsolete framework identity in an active non-historical carrier after the governed identity migration.

**Expected result:** Fail with the stable obsolete-active-identity diagnostic and a non-zero exit.
