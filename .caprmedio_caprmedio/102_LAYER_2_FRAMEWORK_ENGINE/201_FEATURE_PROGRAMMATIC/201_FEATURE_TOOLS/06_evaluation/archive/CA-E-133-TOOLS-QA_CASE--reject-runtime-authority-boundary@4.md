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
# Reject runtime authority boundary

## Test case

**Fixture:** Place the only authoritative copy of one active Atom under `.caprmedio_runtime`.

**Expected result:** Fail with the stable runtime-authority-boundary diagnostic and a non-zero exit.
