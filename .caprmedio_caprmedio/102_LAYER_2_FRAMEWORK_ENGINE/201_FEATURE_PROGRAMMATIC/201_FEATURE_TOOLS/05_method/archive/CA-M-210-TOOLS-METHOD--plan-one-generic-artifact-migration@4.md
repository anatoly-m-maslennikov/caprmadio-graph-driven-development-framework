---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-migration
version: 4
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1138
  derived_from:
    - CA-A-058
---
# Plan one generic Artifact migration

## Applicable when

Use this Method when a declared generic Artifact transformation must be expanded into a reviewable read-only migration plan.

## Procedure

1. Accept one declared transformation rule and bounded source frontier in read-only mode.
2. Resolve every source carrier and derive its preconditions, old-to-new identity mapping, collision checks, required reference rewrites, affected Projections, and expected postconditions.
3. Record the source frontier identities, revisions or digests, transformation inputs, and complete derived effect set in a stable order.
4. Mark the result as a plan only: it grants neither approval nor mutation authority.
5. Return explicit unresolved, ambiguous, and collision findings rather than omitting affected carriers or effects.

## Outcome

One reviewable migration plan describes the complete expected transformation of the declared unchanged source frontier without mutating it.

## Failure or stop

Do not mutate any carrier, reference, Projection, or Journal; stop on an invalid transformation, unresolved source, ambiguous mapping, or collision.
