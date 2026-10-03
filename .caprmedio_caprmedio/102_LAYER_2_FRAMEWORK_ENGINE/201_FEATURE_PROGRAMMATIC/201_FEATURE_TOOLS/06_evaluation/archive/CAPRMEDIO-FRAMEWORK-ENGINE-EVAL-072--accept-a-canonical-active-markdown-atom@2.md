---
artifact_subtype: qa_case
subject_scopes:
  - artifact-validation
version: 2
updated_at: 2026-08-18 22:44:59
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-534--validate-one-artifact-carrier
---
# Accept a canonical active Markdown Atom

## Test case

**Fixture:** Validate one canonical active Markdown Atom with a registered address, minimal frontmatter, one matching H1, and a non-empty claim body.

**Expected result:** Pass with exit `0`, an empty diagnostic set, and unchanged bytes.
