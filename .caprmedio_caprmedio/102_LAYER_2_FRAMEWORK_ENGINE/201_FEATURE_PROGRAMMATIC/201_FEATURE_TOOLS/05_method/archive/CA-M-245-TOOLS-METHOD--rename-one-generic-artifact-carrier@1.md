---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1133
  derived_from:
    - CA-A-058
---
# Rename one generic Artifact carrier

## Applicable when

Use this Method when one generic Artifact carrier requires a filename change under the active generic filename grammar.

## Procedure

1. Resolve the exact source carrier, current identity, and requested target filename, then validate the target against the active grammar.
2. Preflight the target path and reject every collision, unresolved canonical reference, or unavailable source carrier.
3. Discover every governed canonical reference that must change and construct the complete old-to-new identity mapping.
4. Expose one dry-run containing the rename, mapping, and all required reference rewrites.
5. On authorized apply, perform the rename and every required rewrite as one rollbackable transaction, then verify that no governed reference retains the old identity.

## Outcome

One generic Artifact carrier has a grammar-valid new name, an attributable identity mapping, and fully rewritten governed canonical references.

## Failure or stop

Stop or roll back on an invalid filename, collision, stale source, incomplete rewrite set, or failed required rewrite; do not use this helper as an Atom move operation.
