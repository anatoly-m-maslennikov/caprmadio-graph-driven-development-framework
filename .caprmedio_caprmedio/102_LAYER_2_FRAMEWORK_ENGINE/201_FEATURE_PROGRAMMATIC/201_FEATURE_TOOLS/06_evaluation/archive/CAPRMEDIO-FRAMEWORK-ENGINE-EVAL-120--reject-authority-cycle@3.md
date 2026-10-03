---
artifact_subtype: qa_case
subject_scopes:
  - artifact-validation
version: 3
updated_at: 2026-08-21 00:39:48
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-535--validate-project-integrity
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
    - CA-R-838-REQUIREMENT-BSEED_GOVERNANCE--validate-normative-authority-hierarchy
    - CAPRMEDIO-REQU-030--require-complete-authority-topology-in-strict-mode
---
# Reject authority cycle

## Test case

**Fixture:** Add one `child_of` edge that closes a cycle.

**Expected result:** Fail with the stable authority-cycle diagnostic and a non-zero exit.
