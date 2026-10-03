---
artifact_subtype: qa_case
subject_scopes:
  - artifact-validation
version: 3
updated_at: 2026-08-23 16:40:00 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-1137
---
# Accept registered control-root carriers

## Test case

**Fixture:** Keep only registered Atom, Journal, Projection, Settings, catalog, map, hub, and control-file carriers under the control root.

**Expected result:** Pass the control-root carrier allowlist check.
