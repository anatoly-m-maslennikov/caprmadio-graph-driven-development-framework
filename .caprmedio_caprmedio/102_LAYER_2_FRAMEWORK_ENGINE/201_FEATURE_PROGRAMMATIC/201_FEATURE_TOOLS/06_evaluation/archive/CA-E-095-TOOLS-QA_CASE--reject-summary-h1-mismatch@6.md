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
# Reject summary H1 mismatch

## Test case

**Fixture:** Change the H1 so it no longer faithfully renders the immutable filename summary.

**Expected result:** Fail with the stable summary-H1-mismatch diagnostic and a non-zero exit.
