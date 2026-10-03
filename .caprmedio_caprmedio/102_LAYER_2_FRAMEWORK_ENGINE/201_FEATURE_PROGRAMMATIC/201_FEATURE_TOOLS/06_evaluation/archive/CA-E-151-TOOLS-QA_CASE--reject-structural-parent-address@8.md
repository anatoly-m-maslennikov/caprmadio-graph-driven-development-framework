---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 8
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject structural parent address

## Test case

**Fixture:** Give one structural scope a directory address inconsistent with its registered parent.

**Expected result:** Fail with the stable structural-parent-address diagnostic and a non-zero exit.
