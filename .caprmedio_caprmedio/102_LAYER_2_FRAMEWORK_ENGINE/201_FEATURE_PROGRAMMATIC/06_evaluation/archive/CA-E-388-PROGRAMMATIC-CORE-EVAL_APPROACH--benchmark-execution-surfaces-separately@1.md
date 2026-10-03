---
atom_id: CA-E-388
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - performance-benchmark
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 02:10:00 +0400
relations:
  evaluation_for:
    - CA-M-165
  derived_from:
    - CA-A-053
---
# Benchmark execution surfaces separately

## Claim checked

A performance claim is reproducible for one declared execution surface and is
not generalized to another surface.

## Test case

Benchmark one bounded batch Tool workload and attempt to use that result as the
latency baseline for an interactive Hook.

## Acceptance criteria

Pass only when the batch result preserves command, fixture, runtime, platform,
calibration, distribution, baseline, and comparison, while the Hook claim is
rejected as unmeasured.

## Failure disposition

Reject unstable or cross-surface evidence and reopen the affected claim.

## Sources

- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-M-165 — Measure before optimizing PROGRAMMATIC performance](../05_method/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance.md)
