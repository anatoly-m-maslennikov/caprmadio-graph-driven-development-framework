---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-migration
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1139
  derived_from:
    - CA-A-058
---
# Apply one generic Artifact migration

## Applicable when

Use this Method when one approved generic Artifact migration plan must be applied against its unchanged recorded preconditions.

## Procedure

1. Resolve the approved migration plan and seal its plan digest, source preconditions, carrier mappings, and required reference mutations.
2. Recheck every recorded precondition against the current source frontier and reject any changed, missing, or additional required source fact.
3. Construct one transaction containing exactly the approved carrier and reference mutations; exclude unplanned effects.
4. Apply the transaction rollbackably, appending the governed migration event through the Work Journal Tool only after all mutation effects succeed.
5. Return the applied transaction identity and exact resulting frontier without interpreting it as a CAPRMEDIO Atom migration.

## Outcome

One approved unchanged generic Artifact migration is applied as one rollbackable carrier-and-reference transaction with attributable Work Journal evidence.

## Failure or stop

Do not apply an unapproved or stale plan; roll back every carrier and reference mutation on any failed effect or Journal append failure.
