---
subjects:
  governs:
    continuant:
      - artifact-validation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1136
---
# Reject numeric tier

## Test case

**Fixture:** Give a tier-classified RMED Atom a numeric `tier`.

**Expected result:** Fail with the stable numeric-tier diagnostic and a non-zero exit.
