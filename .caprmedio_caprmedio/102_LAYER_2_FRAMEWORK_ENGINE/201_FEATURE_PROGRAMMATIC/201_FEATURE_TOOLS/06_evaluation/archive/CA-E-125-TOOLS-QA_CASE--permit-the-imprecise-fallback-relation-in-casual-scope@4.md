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
# Permit the imprecise fallback relation in casual scope

## Test case

**Fixture:** Add the registered imprecise fallback relation in a casual scope where no precise registered relation applies.

**Expected result:** Pass the authority-mode relation check.
