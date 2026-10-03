---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-catalog
    occurrent:
      - evaluation
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  evaluation_for:
    - CA-M-249
---
# Verify validate one generic Artifact catalog

## Claim checked

CA-M-249 fails closed and separately identifies every missing, stale, duplicate, unknown, and inconsistent catalog entry against declared authority.

## Applicable when

Apply whenever generic catalog-validation comparison or discrepancy classification changes.

## Test case

Use one registered catalog whose declared authority frontier is known, then prepare a catalog representation containing one missing, stale, duplicate, unknown, and inconsistent entry. Validate it and compare every carrier before and after validation.

## Acceptance criteria

Validation fails and emits five separately attributable discrepancy findings. The catalog and all authority carriers remain unchanged.

## Failure disposition

Reject the realization and preserve catalog definition, authority frontier, tampered representation, all discrepancy findings, and no-mutation evidence.
