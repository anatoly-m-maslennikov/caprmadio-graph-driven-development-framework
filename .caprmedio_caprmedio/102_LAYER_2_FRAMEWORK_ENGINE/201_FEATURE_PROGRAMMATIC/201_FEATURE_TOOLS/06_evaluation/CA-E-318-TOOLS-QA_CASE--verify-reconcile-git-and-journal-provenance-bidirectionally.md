---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "programmatic-mutation"
  depends_on: []
version: 10
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-200
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify reconcile git and journal provenance bidirectionally

## Claim checked

CA-M-200 detects Git–Journal discrepancies **in** both directions **and** recovers **only** fully evidenced missing Journal events idempotently.

## Applicable when

apply **to** **any** reconciliation release **or** **after** a suspected provenance-coverage gap.

## Test case

consider one bounded sealed provenance frontier containing one fully evidenced Git commit **without** its Journal event, one Journal event with no reachable commit, one duplicate action **or** event binding, one subject-revision mismatch, one subject-digest mismatch, **and** one Journal-only commit-watermark lag. reconcile that unchanged frontier twice.

## Acceptance criteria

the first run appends **=1** recovered event for the fully evidenced commit **and** reports **every** other introduced discrepancy class with action identity, Initiative, real-change commit SHA, Journal event identity, affected subject identity **and** revision **or** digest, **and** Journal-batch commit SHA; the second run appends nothing **and** returns the same remaining discrepancies.

## Failure disposition

reject the realization **and** preserve Git **and** Journal frontiers, action bindings, recovery evidence, appended lines, **all** discrepancy classifications, **and** the second-run comparison.
