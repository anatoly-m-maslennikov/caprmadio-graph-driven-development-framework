---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "installed-runtime"
  depends_on:
    - "programmatic software"
version: 10
updated_at: "2026-09-17 19:19:46 +0000"
relations:
  evaluation_for:
    - CA-M-110
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify installed selected-runtime component

## Claim checked

one delivered installable PROGRAMMATIC component runs under the runtime **and**
dependency selections owned by accepted Methods from the carrier placed **and**
encoded by its Delivery.

## Applicable conditions

apply **only** **when** a lower-Scope Delivery declares the component installable.
this case does **not** establish a platform-support claim.

## Test case

install one delivered component from its Delivery-owned carrier, invoke its
declared entry boundary, **and** compare the observed runtime **and** dependencies with
their Method-owned selections **and** materializations.

## Acceptance criteria

pass **only** **when** the installed carrier reaches its declared entry boundary,
the observed runtime **and** dependencies match their applicable Method-owned
selections **and** materializations, **and** no undeclared runtime **or** dependency is
required. the carrier **must not** claim selection authority.

## Failure disposition

reject the installation claim **and** return the component **to** its Delivery owner.

## Sources

- [CA-M-110 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-110-PROGRAMMATIC-CORE-IMPL_METHOD--implement-programmatic-components-in-python.md)
