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
      - CAPRMEDIO-GOV-REQU-394--canonical-toml-artifacts
---

# Test Case — Validate canonical TOML migration

The migration test must inventory every governed source, preview without
writing, preserve parsed values and stable IDs, reject collisions and
unsupported values, rewrite every owned reference, and produce a deterministic
old/new digest map. A second apply must be a no-op.

The migrated repository and a generated adopter must pass all validators,
schemas, compilation, traceability, health, bootstrap, release, archive,
runtime, and skill-distribution tests. The gate must reject writable CAPRMEDIO-owned
YAML/JSON authority while accepting only registered host/ecosystem/wire/runtime
exceptions and fresh generated compatibility adapters.

This emitted Test definition is immutable. Runs and evidence are separate.

## Primary claim

Deterministic migration and validation prove canonical TOML artifact equivalence, reference closure, freshness, and external-format boundaries.
