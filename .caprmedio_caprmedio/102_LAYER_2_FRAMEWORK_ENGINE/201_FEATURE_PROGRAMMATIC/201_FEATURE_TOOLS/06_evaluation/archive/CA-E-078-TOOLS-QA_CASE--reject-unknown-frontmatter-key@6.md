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
# Reject unknown frontmatter key

## Test case

**Fixture:** Add one unregistered frontmatter key.

**Expected result:** Fail with the stable unknown-frontmatter-key diagnostic and a non-zero exit.
