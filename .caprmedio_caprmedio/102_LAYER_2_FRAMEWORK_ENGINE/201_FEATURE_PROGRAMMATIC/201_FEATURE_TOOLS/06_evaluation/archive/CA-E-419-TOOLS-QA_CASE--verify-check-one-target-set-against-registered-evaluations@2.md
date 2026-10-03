---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 2
updated_at: 2026-09-02 00:40:00 +0400
relations:
  evaluation_for:
    - CA-M-253
---
# Verify check one target set against registered Evaluations

## Claim checked

CA-M-253 returns stable attributable registered-Evaluation verdicts for one unchanged sealed target set without mutating any governed carrier.

## Applicable when

Apply whenever `GRAPH_CHECK` target-set verification, criterion application, verdict ordering, or no-mutation boundary changes.

## Test case

Inspect the registered `GRAPH_CHECK` unit, then use one sealed target set with two targets and two registered criteria yielding satisfied, unsatisfied, and inapplicable outcomes. Execute the check, then alter the target-set source frontier and execute it again.

## Acceptance criteria

`GRAPH_CHECK` has prefix `GRAPH_CHECK`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK`, and realization path `002_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/GRAPH_CHECK/`. The unchanged case returns every attributable verdict, issue, and evidence in stable target-and-criterion order with no governed carrier change. The altered-frontier case is blocked and performs no evaluation or mutation.

## Failure disposition

Reject the realization and preserve target set, criteria, expected verdicts, ordered result, source-frontier comparison, and no-mutation evidence.
