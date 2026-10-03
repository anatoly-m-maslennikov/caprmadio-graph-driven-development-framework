---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "artifact-operations"
  depends_on: []
version: 6
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-209
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify create one generic Artifact carrier

## Claim checked

CA-M-209 derives and creates exactly one non-Atom generic Artifact carrier without overwrite or identity collision.

## Applicable when

Apply whenever generic Artifact-construction or carrier-identity derivation mechanics change.

## Test case

Supply one structural owner, Content role, title, required metadata, and body that derive a known valid carrier; then repeat with inputs that derive an existing carrier identity.

## Acceptance criteria

The collision case creates nothing and leaves the existing carrier unchanged. The valid case creates exactly one carrier at the derived destination with expected identity, schema-valid metadata, and body digest.

## Failure disposition

Reject the realization and preserve construction inputs, derivation result, collision evidence, created-carrier identity, metadata, and body digest.
