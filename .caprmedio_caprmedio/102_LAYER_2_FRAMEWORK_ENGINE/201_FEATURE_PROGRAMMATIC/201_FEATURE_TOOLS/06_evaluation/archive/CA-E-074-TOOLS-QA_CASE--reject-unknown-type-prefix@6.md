---
subjects:
  governs:
    continuant:
      - artifact-validation
version: 6
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1136
---
# Reject unknown Type prefix

## Test case

**Fixture:** Replace the filename Type prefix with an unregistered four-character prefix.

**Expected result:** Fail with the stable unknown-Type-prefix diagnostic and a non-zero exit.
