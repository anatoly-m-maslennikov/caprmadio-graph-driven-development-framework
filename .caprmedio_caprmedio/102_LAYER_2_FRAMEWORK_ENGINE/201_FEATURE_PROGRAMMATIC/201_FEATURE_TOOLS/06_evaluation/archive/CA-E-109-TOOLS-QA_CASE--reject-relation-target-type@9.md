---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 9
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1137
---
# Reject relation target Type

## Test case

**Fixture:** Use a registered relation kind toward a target Type it does **not** admit.

**Expected result:** Fail with the stable relation-target-Type diagnostic **and** a non-zero exit.
