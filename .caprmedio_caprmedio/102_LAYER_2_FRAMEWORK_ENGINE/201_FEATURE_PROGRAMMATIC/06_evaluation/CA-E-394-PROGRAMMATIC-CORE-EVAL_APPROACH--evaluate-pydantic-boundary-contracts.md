---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "python-boundary-validation"
  depends_on:
    - "programmatic software"
version: 7
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-M-286
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate Pydantic boundary contracts

## Claim checked

an admitted Pydantic boundary accepts its contract **and** rejects structural **or**
coercion defects with stable sanitized diagnostics.

## Test case

submit accepted input, a missing required field, an undeclared field, a wrong
type, **and** a violated constraint **to** one strict closed boundary.

## Acceptance criteria

pass **only** **when** accepted input yields the typed value, **every** invalid input is
rejected at a stable location **and** type, no secret is exposed, **and** intentional
schema change is treated as compatibility change.

## Failure disposition

reject the boundary **when** coercion **or** extra fields escape its declared contract.

## Sources

- [Pydantic: error handling](https://docs.pydantic.dev/latest/errors/errors/)
- [Pydantic: JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [CA-M-286 — Validate untrusted structured data with Pydantic](../05_method/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic.md)
