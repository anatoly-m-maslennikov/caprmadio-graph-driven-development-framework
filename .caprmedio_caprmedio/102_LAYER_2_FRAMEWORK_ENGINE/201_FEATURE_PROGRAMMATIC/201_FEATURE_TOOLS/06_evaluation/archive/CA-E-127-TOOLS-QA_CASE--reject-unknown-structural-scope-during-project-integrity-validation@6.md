---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 6
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
  derived_from:
    - CA-A-057
---
# Reject unknown structural scope during project integrity validation

## Test case

**Fixture:** Add one unregistered structural-scope folder under the control root.

**Expected result:** Fail with the stable unknown-structural-scope diagnostic and a non-zero exit.
