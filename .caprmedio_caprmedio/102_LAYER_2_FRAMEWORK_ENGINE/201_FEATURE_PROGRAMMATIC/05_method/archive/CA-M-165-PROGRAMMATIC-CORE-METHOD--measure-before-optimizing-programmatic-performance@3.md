---
atom_id: CA-M-165
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - performance-measurement
  depends_on:
    continuant:
      - programmatic software
version: 3
updated_at: 2026-09-01 01:45:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Measure before optimizing PROGRAMMATIC performance

Measure a PROGRAMMATIC performance concern before accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, or
background surface rather than treating one surface as universal.

## Applicable when

Apply when a Tool, App backend service, or MCP component proposes or assesses
a performance-sensitive change.

## Procedure

1. Profile the applicable surface to locate the measured bottleneck, then
   select its representative workload.
2. Preserve the input, environment, baseline, observed distribution, and
   comparison threshold with the measurement.
3. Compare the change to the recorded baseline before accepting the claimed
   improvement.
4. Leave numeric budgets to a later bounded authority until current baselines
   and Operator priorities establish them.

## Outcome

An accepted performance claim is tied to one reproducible workload and
measurement boundary instead of a universal or unmeasured optimization claim.

## Failure or stop

Stop the performance claim when no representative workload, preserved
baseline, or comparable observation exists; do not invent a numeric budget.

## Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
