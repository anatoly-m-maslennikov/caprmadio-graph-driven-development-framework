---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Validate Artifact Catalog"
  depends_on:
    - "Action"
    - "Artifact"
    - "Artifact/Revision"
    - "Projection"
version: 6
updated_at: "2026-09-17 03:15:32 +0000"
relations: {"evaluation_for":["CA-R-1142","CA-O-034"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify validate one generic Artifact catalog

## Claim checked

CA-O-034 fails closed **and** separately identifies **every** missing, stale, duplicate, unknown, **and** inconsistent catalog entry against declared authority.

## Applicable when

Apply whenever generic catalog-validation comparison **or** discrepancy classification changes.

## Test case

Use one registered catalog whose declared authority frontier is known, **then** prepare a catalog representation containing one missing, stale, duplicate, unknown, **and** inconsistent entry. Validate it **and** compare **every** carrier **before** **and** **after** validation.

## Acceptance criteria

Validation fails **and** emits five separately attributable discrepancy findings. The catalog **and** **all** authority carriers remain unchanged.

## Failure disposition

Reject the realization **and** preserve catalog definition, authority frontier, tampered representation, **all** discrepancy findings, **and** no-mutation evidence.
