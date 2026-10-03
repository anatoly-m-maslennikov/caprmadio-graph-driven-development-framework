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
updated_at: 2026-09-02 00:15:00 +0400
relations:
  evaluation_for:
    - CA-M-205
---
# Verify reconcile work journal coverage from sealed evidence

## Claim checked

CA-M-205 recovers missing Journal coverage only when sealed evidence supplies every required event fact and does so idempotently.

## Applicable when

Apply whenever Journal coverage recovery logic or required event fields change.

## Test case

Consider two uncovered governed actions under one active Journal-event schema: one has sealed durable evidence for every schema-required event field and action binding; the other lacks one schema-required provenance field. Reconcile the same frontier twice without changing it.

## Acceptance criteria

The first run appends exactly one complete `recovered` event for the fully evidenced action and reports the other as blocked; the second run appends nothing; and no existing Journal line is edited.

## Failure disposition

Reject the realization and preserve both action-evidence bundles, the active event schema, coverage decisions, the appended event, blocked field, Journal before-and-after digests, and second-run result.
