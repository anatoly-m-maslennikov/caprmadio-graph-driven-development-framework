---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  method_for:
    - CA-R-1109
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile disabled and removed Tool projections

## Applicable when

Apply when the current Tool source set or its enablement decisions change.

## Procedure

1. Resolve the complete current source set before changing the registry.
2. Add newly eligible Tools, exclude explicitly disabled Tools, and remove projections without current sources.
3. Publish only the resulting complete set rather than retaining a separate allowlist.

## Outcome

The registry has no stale, disabled, or independently configured Tool projection.

## Failure or stop

Stop when source discovery is incomplete or any resulting projection cannot be classified.
