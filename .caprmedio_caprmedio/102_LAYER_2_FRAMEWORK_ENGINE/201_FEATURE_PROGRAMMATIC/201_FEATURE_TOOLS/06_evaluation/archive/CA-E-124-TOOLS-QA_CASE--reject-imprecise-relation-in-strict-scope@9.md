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
# Reject imprecise relation in strict scope

## Test case

**Fixture:** Add `related_to` as an operative relation **in** a strict scope.

**Expected result:** Fail with the stable imprecise-relation-in-strict-scope diagnostic **and** a non-zero exit.
