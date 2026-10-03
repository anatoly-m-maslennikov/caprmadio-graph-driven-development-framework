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
    - CA-R-1130
  derived_from:
    - CA-A-058
---
# Patch generic Artifact metadata

## Applicable when

Use this Method when a governed Tool needs the shared mechanics for a field-level frontmatter patch on one generic Artifact.

## Procedure

1. Resolve exactly one generic Artifact and seal its path, revision, digest, schema, current frontmatter, and body digest.
2. Apply only declared add, replace, or remove operations to registered frontmatter fields.
3. Validate the resulting complete frontmatter document and reject unknown fields, failed preconditions, and all relation-target operations.
4. Produce the exact field-level dry-run while preserving the original body bytes and carrier identity.
5. On authorized apply, recheck the sealed preconditions, atomically replace the carrier, advance governed revision metadata once, and prove the unchanged body digest.

## Outcome

The Artifact receives one schema-valid metadata revision while its body and identity remain unchanged.

## Failure or stop

Stop or roll back on stale preconditions, unknown fields, schema failure, failed body preservation, or any requested relation patch.
