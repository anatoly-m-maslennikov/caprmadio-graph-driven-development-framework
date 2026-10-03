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
# Reject same scope tier direction

## Test case

**Fixture:** In one structural scope, point a tier-classified RMED child at a parent with the same global tier number.

**Expected result:** Fail with the stable same-scope-tier-direction diagnostic and a non-zero exit.
