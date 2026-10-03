---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - programmatic-mutation
    occurrent:
      - evaluation
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-200
---
# Verify reconcile git and journal provenance bidirectionally

## Claim checked

CA-M-200 detects Git–Journal discrepancies in both directions and recovers only fully evidenced missing Journal events idempotently.

## Applicable when

Apply to any reconciliation release or after a suspected provenance-coverage gap.

## Test case

Consider one bounded sealed provenance frontier containing one fully evidenced Git commit without its Journal event, one Journal event with no reachable commit, one duplicate action or event binding, one subject-revision mismatch, one subject-digest mismatch, and one Journal-only commit-watermark lag. Reconcile that unchanged frontier twice.

## Acceptance criteria

The first run appends exactly one recovered event for the fully evidenced commit and reports every other introduced discrepancy class with action identity, Initiative, real-change commit SHA, Journal event identity, affected subject identity and revision or digest, and Journal-batch commit SHA; the second run appends nothing and returns the same remaining discrepancies.

## Failure disposition

Reject the realization and preserve Git and Journal frontiers, action bindings, recovery evidence, appended lines, all discrepancy classifications, and the second-run comparison.
