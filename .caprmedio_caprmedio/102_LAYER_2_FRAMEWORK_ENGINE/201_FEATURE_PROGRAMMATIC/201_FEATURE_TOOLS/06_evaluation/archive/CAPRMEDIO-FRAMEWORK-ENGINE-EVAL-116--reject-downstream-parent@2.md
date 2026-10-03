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
# Reject downstream parent

## Test case

**Fixture:** Point a tier-classified RMED child at a parent with a greater global tier number.

**Expected result:** Fail with the stable downstream-parent diagnostic and a non-zero exit.
