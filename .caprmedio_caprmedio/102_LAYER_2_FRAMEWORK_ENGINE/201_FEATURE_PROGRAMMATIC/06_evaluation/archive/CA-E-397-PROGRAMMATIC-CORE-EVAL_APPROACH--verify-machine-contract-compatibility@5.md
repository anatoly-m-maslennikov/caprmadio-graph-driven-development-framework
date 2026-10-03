---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "machine-contract-compatibility"
  depends_on:
    - "programmatic software"
version: 5
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-166
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify machine-contract compatibility

## Claim checked

One public machine boundary preserves structural, semantic, version, **and**
adjacent producer-consumer compatibility.

## Test case

Pass valid, missing-field, forbidden-field, wrong-type, **and** unsupported-version
fixtures from one producer **to** its supported adjacent consumer.

## Acceptance criteria

pass **only** **when** valid meaning survives, structural **and** semantic failures remain
distinct, unsupported versions are rejected, **and** the declared compatibility
promise is preserved **or** explicitly replaced.

## Failure disposition

Reject release **or** the compatibility claim **until** the boundary is restored.

## Sources

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [CA-M-166 — Preserve declared interface compatibility boundaries](../05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md)
