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
    - CA-R-1129
  derived_from:
    - CA-A-058
---
# Read generic Artifact metadata

## Applicable when

Use this Method when framework internals need selected frontmatter and derived identity for exactly one generic Artifact.

## Procedure

1. Resolve exactly one generic Artifact carrier from the caller-supplied carrier identity or path, without applying CAPRMEDIO Atom selector semantics.
2. Seal its path, filename, and source digest, then parse only its frontmatter without loading its body.
3. Return the requested registered fields and carrier-derived identity; represent each absent field and each parse error explicitly.
4. Mark the result as a form-agnostic helper result and retain the source identity and digest needed to attribute it.
5. Return no mutation plan and do not expose this helper as a public substitute for `ATOM_READ`.

## Outcome

Callers receive an attributable body-free metadata result for exactly one generic Artifact carrier.

## Failure or stop

Return an explicit result for an absent carrier, ambiguous identity, unsupported field, or malformed frontmatter without mutation.
