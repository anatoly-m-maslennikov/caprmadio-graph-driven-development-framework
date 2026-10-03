---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "engineering-ratchet"
  depends_on:
    - "Journal/Record"
    - "programmatic software"
version: 10
updated_at: "2026-09-17 19:19:49 +0000"
relations:
  evaluation_for:
    - CA-M-164
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify changed-code adoption ratchet

## Claim checked

One changed **or** new PROGRAMMATIC target within an admitted automation **or** typing
capability does **not** regress below its current passing boundary.

## Applicable conditions

Apply **when** a component changes source within an admitted typing, formatting,
linting, **or** behavioral-check capability. Unadmitted capability selection is
**not** applicable.

## Test case

Evaluate one changed target against its current admitted passing boundary.

## Acceptance criteria

pass **only** **when** the target meets the current Method-owned boundary **or** has one
accepted Method-owned bounded exception. Configuration **and** Implementation **must**
materialize that selection, Delivery **must** govern its carrier, **and** Journal Records
**must** carry evidence of the actual result **without** becoming another selection authority.

## Failure disposition

Reject the ratchet claim **and** return the target **to** its change owner.

## Sources

- [CA-M-164 — Ratchet typing and automation adoption](../05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md)
