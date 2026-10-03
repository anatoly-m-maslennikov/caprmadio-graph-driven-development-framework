---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 7
updated_at: 2026-09-02 03:30:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject strict orphan

## Test case

**Fixture:** Leave one non-Goal tier-classified RMED Atom parentless in a strict scope.

**Expected result:** Fail with the stable strict-orphan diagnostic and a non-zero exit.
