---
atom_id: CA-E-261
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "effect-plan"
  depends_on:
    - "programmatic software"
version: 6
updated_at: 2026-09-01 02:00:00 +0400
relations:
  evaluation_for:
    - CA-M-160
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject incomplete plan at effect boundary

## Claim checked

One PROGRAMMATIC effect boundary refuses a plan that lacks the information
needed to execute its declared effect.

## Applicable conditions

Apply when a component applies filesystem, process, clock, environment,
network, persistence, or logging-export effects from a decision result.

## Test case

Submit one effect plan with its expected outcome or required ordering omitted.

## Acceptance criteria

Pass only when the effect boundary returns a typed incomplete-plan result and
applies no effect.

## Failure disposition

Reject the operation and correct the decision boundary before retrying.

## Sources

- [CA-M-160 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-160-PROGRAMMATIC-CORE-METHOD--separate-deterministic-transformations-from-effects-and-lifecycle.md)
