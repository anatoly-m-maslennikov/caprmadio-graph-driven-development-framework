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
    - CA-R-1145
  derived_from:
    - CA-A-058
---
# Ingest one external Analysis

## Applicable when

Use this Method when one external review or Analysis must be represented within a bounded project-analysis frontier without becoming accepted project authority.

## Procedure

1. Resolve the external Analysis source identity, source digest, transformation session, and exact target frontier.
2. Preserve the imported content in a provenance envelope that identifies its source, target frontier, and all declared transformations.
3. Mark every imported claim as non-authoritative and require a separate governed adoption decision before any accepted project authority is created or revised.
4. Return the envelope and explicit provenance links without editing source carriers or target authority.
5. Reject a missing source identity, source digest, target frontier, or transformation provenance rather than filling it with inference.

## Outcome

One external Analysis is represented in an attributable bounded provenance envelope while its claims remain distinct from accepted project authority.

## Failure or stop

Do not ingest an Analysis with incomplete provenance and do not create, revise, or imply adoption of any project authority.
