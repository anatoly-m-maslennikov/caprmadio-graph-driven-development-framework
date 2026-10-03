---
subjects:
  governs: "artifact-validation"
  depends_on: []
version: 10
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1136
---
# Reject lifecycle placement

## Test case

**Fixture:** move an active Atom into an unregistered lifecycle directory.

**Expected result:** fail with the stable lifecycle-placement diagnostic **and** a non-zero exit.
