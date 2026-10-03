---
subjects:
  declared:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-08-23 17:53:53 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject a childless Principle in strict scope

## Test case

**Fixture:** Leave one Principle without an active permitted child in a strict scope.

**Expected result:** Fail with the stable strict-child-coverage diagnostic and a non-zero exit.
