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
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-535--validate-project-integrity
---
# Reject settings source digest

## Test case

**Fixture:** Change one Project Settings source digest so it no longer matches the recorded source revision.

**Expected result:** Fail with the stable settings-source-digest diagnostic and a non-zero exit.
