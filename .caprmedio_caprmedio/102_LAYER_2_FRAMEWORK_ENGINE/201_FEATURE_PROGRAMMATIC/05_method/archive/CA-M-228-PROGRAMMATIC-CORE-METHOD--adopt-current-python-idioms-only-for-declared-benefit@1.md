---
atom_id: CA-M-228
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - python-idiom-adoption
  depends_on:
    continuant:
      - programmatic software
version: 1
updated_at: 2026-09-01 01:50:00 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Adopt current Python idioms only for declared benefit

Adopt a stable idiom available in the selected Python boundary only when it
improves a named project quality such as correctness, understandability,
safety, or measured performance. Preserve the simpler supported idiom when a
newer construct adds no useful distinction.

## Applicable when

Apply when new or materially changed PROGRAMMATIC Python source proposes a
runtime-specific language construct or concurrency model.

## Procedure

1. State the quality improved and the supported Python boundary that admits
   the idiom.
2. Prefer the simplest current construct that expresses the required meaning.
3. Use f-strings for immediate trusted string construction; use t-strings only
   when a processor needs structured interpolation data.
4. Keep synchronous work synchronous unless related concurrent operations
   create a demonstrated need for structured concurrency.
5. Record a compatibility exception when an admitted host boundary cannot use
   the selected idiom.

## Outcome

Current Python capabilities improve the code for an explicit reason without
turning novelty into a requirement or obscuring the supported boundary.

## Failure or stop

Stop adoption when the benefit is unnamed, the simpler idiom is equally clear,
or the construct exceeds the selected runtime or compatibility boundary.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [Python documentation: task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
