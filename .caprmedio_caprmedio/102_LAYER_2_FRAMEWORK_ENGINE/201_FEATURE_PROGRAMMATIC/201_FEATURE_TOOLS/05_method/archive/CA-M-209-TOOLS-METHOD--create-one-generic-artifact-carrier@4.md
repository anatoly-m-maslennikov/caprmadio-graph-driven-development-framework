---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1132
  derived_from:
    - CA-A-058
---
# Create one generic Artifact carrier

## Applicable when

Use this Method when a Content-role-specific Tool delegates generic construction of exactly one non-Atom Artifact carrier.

## Procedure

1. Accept one structural owner, Content role, title, required metadata, and body for a new generic Artifact carrier.
2. Derive the canonical Artifact ID, filename, and owner-relative destination from the active generic carrier rules.
3. Preflight the resolved destination and identity against existing carriers and reject every collision or implicit overwrite.
4. Build the carrier from the supplied body and schema-valid metadata, preserving the derivation inputs in the dry-run result.
5. On authorized apply, create exactly the derived carrier and verify its identity, placement, metadata, and body digest.

## Outcome

One generic Artifact carrier is created with valid identity, placement, metadata, and body, or the repository remains unchanged.

## Failure or stop

Reject absent owner, role, title, required metadata, or body; invalid derivation; collisions; and requests that treat this helper as a public alternative to `ATOM_CREATE`.
