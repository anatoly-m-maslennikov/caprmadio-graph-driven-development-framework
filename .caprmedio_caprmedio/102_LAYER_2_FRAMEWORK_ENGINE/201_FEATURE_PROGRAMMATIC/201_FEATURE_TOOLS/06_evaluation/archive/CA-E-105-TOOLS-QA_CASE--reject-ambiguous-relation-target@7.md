---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 7
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject ambiguous relation target

## Test case

**Fixture:** Make one relation stem resolve to two carriers.

**Expected result:** Fail with the stable ambiguous-relation-target diagnostic and a non-zero exit.
