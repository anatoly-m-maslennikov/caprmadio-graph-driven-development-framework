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
# Accept a canonical active Markdown Atom

## Test case

**Fixture:** Validate one canonical active Markdown Atom with a registered address, minimal frontmatter, one matching H1, and a non-empty claim body.

**Expected result:** Pass with exit `0`, an empty diagnostic set, and unchanged bytes.
