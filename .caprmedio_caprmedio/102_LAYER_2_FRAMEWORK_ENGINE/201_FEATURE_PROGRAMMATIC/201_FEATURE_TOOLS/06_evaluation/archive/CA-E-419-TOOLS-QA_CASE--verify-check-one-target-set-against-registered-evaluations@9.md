---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "feature-boundary"
  depends_on: []
version: 9
updated_at: "2026-09-17 22:49:15 +0000"
relations:
  evaluation_for:
    - CA-M-253
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify check one target set against registered Evaluations

## Claim checked

CA-M-253 returns stable attributable registered-Evaluation verdicts for one unchanged sealed target set **without** mutating **any** governed carrier.

## Applicable when

Apply whenever `GRAPH_CHECK` target-set verification, criterion application, verdict ordering, **or** no-mutation boundary changes.

## Test case

Inspect the registered `GRAPH_CHECK` unit, **then** use one sealed target set with two targets **and** two registered criteria yielding satisfied, unsatisfied, **and** inapplicable outcomes. Execute the check, **then** alter the target-set source frontier **and** execute it again. separately exercise an unresolved target set **and** a registered criterion that reports an execution error. retain the exact registered criterion identity **and** failure evidence; error **or** blocked is **not** satisfied, unsatisfied **or** inapplicable.

## Acceptance criteria

`GRAPH_CHECK` has prefix `GRAPH_CHECK`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/GRAPH_CHECK`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/GRAPH_CHECK/`. The unchanged case returns **every** attributable verdict, issue, **and** evidence **in** stable target-and-criterion order with no governed carrier change. The altered-frontier case is blocked **and** performs no evaluation **or** mutation. an unresolved target set returns the declared blocked **or** error disposition **without** criterion application; a criterion execution error remains explicitly attributable as error rather than an omitted **or** successful verdict. **all** cases preserve governed Atoms, Journals, native Implementation **and** derived outputs unchanged under CA-M-253.

## Failure disposition

Reject the realization **and** preserve target set, criteria, expected verdicts, ordered result, source-frontier comparison, **and** no-mutation evidence.
