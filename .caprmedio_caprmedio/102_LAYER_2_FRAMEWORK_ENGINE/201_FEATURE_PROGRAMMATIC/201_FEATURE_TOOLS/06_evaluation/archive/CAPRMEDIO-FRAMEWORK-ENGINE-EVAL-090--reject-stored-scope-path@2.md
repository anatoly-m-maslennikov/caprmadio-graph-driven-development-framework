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
# Reject stored scope path

## Test case

**Fixture:** Persist `scope_path` in frontmatter when the canonical address derives it completely.

**Expected result:** Fail with the stable derived-frontmatter-fact diagnostic and a non-zero exit.
