---
atom_id: CA-M-233
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - software-evaluation-selection
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
# Select software Evaluation techniques by failure mode

Select the smallest complementary Evaluation set that can expose the declared
failure modes of the affected PROGRAMMATIC component.

## Applicable when

Apply when defining or changing behavioral evidence for a Tool, App, MCP
component, Hook, or background service.

## Procedure

1. Enumerate the failure modes and the observable condition for each.
2. Use examples for known behavior, property-based or stateful generation for
   broad input or transition spaces, mutation testing for weak assertions,
   contract checks for machine boundaries, and reviewed golden baselines for
   large deterministic output.
3. Keep fast syntax, format, lint, type, and focused behavioral checks in the
   changed-code gate.
4. Run expensive mutation, fuzz, broad compatibility, and snapshot-review work
   outside synchronous Git or host Hooks unless a measured bound admits it.
5. Record target, configuration, source frontier, tool versions, seed or case,
   result, and replay command.

## Outcome

Each Evaluation technique covers a named failure mode and no passing technique
is treated as evidence for an uncovered one.

## Failure or stop

Stop acceptance when a declared failure mode lacks evidence or the evidence
cannot be replayed at its recorded frontier.

## Sources

- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
