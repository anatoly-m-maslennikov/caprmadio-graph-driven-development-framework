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
# Accept registered control-root carriers

## Test case

**Fixture:** Keep only registered Atom, Journal, Projection, Settings, catalog, map, hub, and control-file carriers under the control root.

**Expected result:** Pass the control-root carrier allowlist check.
