---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "operational-diagnostic"
  depends_on:
    - "programmatic software"
    - "Logging Policy"
version: 9
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-163
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify structured diagnostic schema

## Claim checked

one PROGRAMMATIC operational diagnostic uses an admitted severity **and** provides
the actionable contextual fields required by its declared schema.

## Applicable conditions

apply **when** a component emits a diagnostic for normal operation, degraded
operation, failure, recovery, **or** diagnostic detail.

## Test case

evaluate one emitted diagnostic record for a declared component event.

## Acceptance criteria

pass **only** **when** the record uses ERROR, WARNING, INFO, **or** DEBUG, includes its
declared actionable contextual fields, **and** does **not** repurpose Journal history
as an operational diagnostic.

## Failure disposition

reject the diagnostic path **until** its schema **and** severity are corrected.

## Sources

- [CA-M-163 — Emit structured operational diagnostics](../05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md)
