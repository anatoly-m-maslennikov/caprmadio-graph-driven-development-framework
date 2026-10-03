---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-migration
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-247
---
# Verify apply one generic Artifact migration

## Claim checked

CA-M-247 applies only an approved unchanged generic migration plan as one rollbackable transaction with attributable Work Journal evidence.

## Applicable when

Apply whenever generic migration precondition checking, transaction construction, rollback, or Work Journal append mechanics change.

## Test case

Prepare one approved two-carrier migration plan with one reference rewrite. Change one recorded precondition before an apply attempt, then restore it and apply the unchanged approved plan.

## Acceptance criteria

The stale attempt changes no carrier or reference and appends no migration event. The valid attempt applies every planned effect once, appends one attributable migration event, and exposes one transaction identity.

## Failure disposition

Reject the realization and preserve plan digest, precondition comparison, carrier and reference diffs, Work Journal evidence, transaction identity, and rollback evidence.
