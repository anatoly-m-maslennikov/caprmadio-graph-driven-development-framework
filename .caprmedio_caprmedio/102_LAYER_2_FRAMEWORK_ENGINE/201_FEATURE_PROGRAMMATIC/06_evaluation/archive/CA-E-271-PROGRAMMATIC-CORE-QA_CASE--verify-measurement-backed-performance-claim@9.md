---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "performance-measurement"
  depends_on:
    - "programmatic software"
version: 9
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-165
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify measurement-backed performance claim

## Claim checked

one PROGRAMMATIC performance claim is supported by a representative workload,
preserved baseline, observed distribution, **and** comparable observation.

## Applicable conditions

apply **when** a component proposes **or** assesses a performance-sensitive change.
no numerical budget is implied **where** no bounded owner has admitted one.

## Test case

evaluate one claimed performance change against its selected surface **and**
recorded baseline.

## Acceptance criteria

pass **only** **when** the workload input, environment, baseline, observed
distribution, **and** comparison threshold are recoverable **and** support the stated
claim.

## Failure disposition

reject the performance claim **without** a representative baseline; do **not** invent
a numeric budget.

## Sources

- [CA-M-165 — Measure before optimizing PROGRAMMATIC performance](../05_method/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance.md)
