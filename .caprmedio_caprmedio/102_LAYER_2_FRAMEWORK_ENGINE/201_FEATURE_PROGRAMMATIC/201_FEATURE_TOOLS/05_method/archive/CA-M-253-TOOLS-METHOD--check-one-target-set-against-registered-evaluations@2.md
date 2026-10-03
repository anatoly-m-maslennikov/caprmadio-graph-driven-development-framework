---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 2
updated_at: 2026-09-02 00:40:00 +0400
relations:
  method_for:
    - CA-R-1154
  derived_from:
    - CA-A-058
---
# Check one target set against registered Evaluations

## Applicable when

Use this Method when `GRAPH_CHECK` must apply selected registered Evaluation criteria to one previously sealed target set.

## Procedure

1. Confirm that `GRAPH_CHECK` is registered as one `unordered_unit` Checker owned immediately by `TOOLS` at Structural level `4`, with prefix `GRAPH_CHECK`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK`, and realization path `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK/`.
2. Resolve one sealed target-set identity and selected registered Evaluation criteria.
3. Confirm that the target set retains its recorded membership, source frontier, and digest before beginning evaluation.
4. Apply each selected criterion to each applicable target and retain attributable issue, evidence, and verdict records in deterministic target-and-criterion order.
5. Distinguish satisfied, unsatisfied, inapplicable, blocked, and error verdicts, and return the complete result without changing governed Atoms, Journals, native Implementation, or derived outputs.

## Outcome

One read-only `GRAPH_CHECK` result provides stable attributable issues, evidence, and verdicts for the selected registered criteria over one sealed target set.

## Failure or stop

Do not evaluate a stale or unresolved target set and do not mutate any governed carrier; return explicit blocked or error verdicts instead.
