---
atom_id: CA-M-255
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 3
updated_at: 2026-09-04 03:10:59 +0400
relations:
  method_for:
    - CA-R-1156
  derived_from:
    - CA-A-058
---
# Rebuild affected Projections

## Applicable when

Use this Method when `PROJECTION_REBUILD` must refresh Projections affected by declared changed source frontiers.

## Procedure

1. Confirm that `PROJECTION_REBUILD` is registered as one `unordered_unit` Doer owned immediately by `TOOLS` at Structural level `4`, with prefix `PROJECTION_REBUILD`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/PROJECTION_REBUILD`, and realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/301_TOOLS/PROJECTION_REBUILD/`.
2. Resolve the changed source frontiers and derive the complete affected Projection set using declared Projection dependencies.
3. Order affected Projections by those dependencies and reject an unresolved or cyclic dependency order.
4. Preview every derived output effect, including output identity, source frontier, and expected currentness state.
5. Materialize only the explicitly approved preview outputs and attach their source frontier and generator provenance; verify currentness and idempotence after publication by rebuilding against the unchanged frontier and comparing the resulting outputs.

## Outcome

One `PROJECTION_REBUILD` operation materializes every and only affected approved Projection in dependency order and verifies its currentness and idempotence.

## Failure or stop

Do not publish on an unresolved dependency, incomplete affected set, unapproved output, changed source frontier, failed currentness check, or failed idempotence check.
