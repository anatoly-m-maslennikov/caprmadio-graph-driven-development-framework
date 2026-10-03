---
atom_id: CA-E-359
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subtype-contract"
  depends_on:
    - "programmatic software"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-158
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject inheritance without a substitutable contract

## Claim checked

One PROGRAMMATIC inheritance relationship exists only for a stable
substitutable subtype contract.

## Test case

Evaluate one changed subclass that inherits behavior for code reuse but cannot
replace its base under the base contract.

## Acceptance criteria

Pass only when the inheritance is rejected and the behavior is expressed by a
function, module, or composed collaborator.

## Failure disposition

Reject the subtype boundary until substitutability is demonstrated or
inheritance is removed.

## Sources

- [CA-M-158 — Allocate owned state and lifecycle to objects](../05_method/CA-M-158-PROGRAMMATIC-CORE-METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
