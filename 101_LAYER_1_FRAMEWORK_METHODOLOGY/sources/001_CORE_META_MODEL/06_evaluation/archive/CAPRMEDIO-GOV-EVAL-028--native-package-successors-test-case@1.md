---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMEDIO-GOV-METH-026--native-package-successors
---

# Test Case — Validate native package-registry successors

The migration suite must preserve every selector-sealed legacy package YAML
digest, emit exactly one parseable sibling `package.toml`, include active
native IDs and current artifact paths, prefer TOML for current reads, and keep
legacy YAML as read-only historical input.

It must reject a missing or changed legacy carrier, an existing conflicting
TOML target, incomplete active-ID reconciliation, two writable current owners,
or readiness evidence whose preserved-input or final-output digest is stale.
A second apply is a no-op.

This Test definition is immutable. Runs and evidence are separate.

## Primary claim

Deterministic tests prove byte-stable legacy package carriers, one TOML current successor, current-ID reconciliation, reader precedence, and fail-closed package cutover.
