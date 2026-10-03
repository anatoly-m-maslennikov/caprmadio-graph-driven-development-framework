---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "project-graph-state"
  depends_on: []
version: 5
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-149
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Rebuild one project graph state from configuration

## Claim checked

The graph-state Tool derives one current non-authoritative projection from its declared configuration authority.

## Test case

Rebuild graph state twice from one unchanged configuration frontier.

## Acceptance criteria

The projections agree semantically, name their configuration sources, and no direct output edit becomes authority.

## Failure disposition

Reject the projection as stale, nondeterministic, or authority-creating.
