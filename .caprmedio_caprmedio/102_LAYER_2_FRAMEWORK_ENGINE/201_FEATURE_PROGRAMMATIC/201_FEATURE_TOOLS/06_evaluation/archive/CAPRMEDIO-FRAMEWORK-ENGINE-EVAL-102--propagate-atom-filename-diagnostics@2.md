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
# Propagate Atom filename diagnostics

## Test case

**Fixture:** Add one carrier that fails ACV-002 while leaving the rest of the project valid.

**Expected result:** Fail with the propagated malformed-filename diagnostic and a non-zero exit.
