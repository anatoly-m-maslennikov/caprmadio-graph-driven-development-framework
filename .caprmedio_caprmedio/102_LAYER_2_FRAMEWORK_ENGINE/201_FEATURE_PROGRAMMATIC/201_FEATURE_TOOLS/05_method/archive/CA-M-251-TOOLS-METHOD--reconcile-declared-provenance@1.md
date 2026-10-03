---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - provenance
version: 1
updated_at: 2026-09-02 00:25:00 +0400
relations:
  method_for:
    - CA-R-1146
  derived_from:
    - CA-A-058
---
# Reconcile declared provenance

## Applicable when

Use this Method when selected Artifacts require a read-only comparison of their declared source, draft, session, revision, and content-digest provenance.

## Procedure

1. Resolve the selected Artifacts and their declared provenance fields without modifying carriers or following undeclared inferences.
2. Compare every declared source, draft, session, revision, and content digest with the referenced current carrier or recorded value.
3. Classify each link as current, missing, conflicting, stale, or unverifiable and retain the exact observed evidence.
4. Attribute each finding to its source Artifact, declared field, target reference, and observed digest or revision.
5. Return the reconciliation result without creating authority, repairing provenance, or deciding semantic adoption.

## Outcome

One read-only provenance reconciliation result reports every current, missing, conflicting, stale, or unverifiable declared link in the selected scope.

## Failure or stop

Do not mutate Artifacts or infer provenance; return an explicit unresolved result when a selected Artifact or declared target cannot be read.
