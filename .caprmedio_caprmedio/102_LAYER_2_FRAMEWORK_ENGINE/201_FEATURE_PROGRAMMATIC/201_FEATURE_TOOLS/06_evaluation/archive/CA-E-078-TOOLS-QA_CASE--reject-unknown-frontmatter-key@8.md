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
    - CA-R-1136
---
# Reject unknown frontmatter key

## Test case

**Fixture:** Add one unregistered frontmatter key.

**Expected result:** Fail with the stable unknown-frontmatter-key diagnostic and a non-zero exit.
