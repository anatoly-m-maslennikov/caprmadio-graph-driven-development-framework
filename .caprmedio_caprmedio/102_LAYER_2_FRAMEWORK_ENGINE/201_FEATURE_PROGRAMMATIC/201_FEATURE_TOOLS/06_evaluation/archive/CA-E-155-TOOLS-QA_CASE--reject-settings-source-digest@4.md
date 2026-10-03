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
# Reject settings source digest

## Test case

**Fixture:** Change one Project Settings source digest so it no longer matches the recorded source revision.

**Expected result:** Fail with the stable settings-source-digest diagnostic and a non-zero exit.
