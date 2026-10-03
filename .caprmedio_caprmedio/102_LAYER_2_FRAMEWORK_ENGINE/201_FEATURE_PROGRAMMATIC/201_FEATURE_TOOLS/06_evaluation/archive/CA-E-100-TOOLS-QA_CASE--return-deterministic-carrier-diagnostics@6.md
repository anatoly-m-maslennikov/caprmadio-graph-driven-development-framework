---
subjects:
  governs:
    continuant:
      - artifact-validation
version: 6
updated_at: 2026-09-12 04:15:38 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1136
---
# Return deterministic carrier diagnostics

## Test case

**Fixture:** Run ACV-002 twice with the same settings and source frontier.

**Expected result:** Return identical ordered diagnostics and exit status on both runs.
