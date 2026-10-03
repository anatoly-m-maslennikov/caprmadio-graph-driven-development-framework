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
# Reject non direct relation

## Test case

**Fixture:** Persist a transitive semantic edge in addition to the direct path that already entails it.

**Expected result:** Fail with the stable non-direct-relation diagnostic and a non-zero exit.
