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
    - CA-R-1136
---
# Accept a canonical active Markdown Atom

## Test case

**Fixture:** Validate one canonical active Markdown Atom with a registered address, minimal frontmatter, one matching H1, and a non-empty claim body.

**Expected result:** Pass with exit `0`, an empty diagnostic set, and unchanged bytes.
