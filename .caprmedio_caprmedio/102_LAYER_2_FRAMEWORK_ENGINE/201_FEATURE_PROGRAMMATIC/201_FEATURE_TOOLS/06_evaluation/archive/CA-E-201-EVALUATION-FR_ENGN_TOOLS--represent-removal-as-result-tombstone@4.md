---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 4
updated_at: 2026-08-23 16:45:00 +0400
relations:
  evaluation_for:
    - CA-R-805
    - CA-R-812
    - CA-R-1121
---
# Represent removal as a result tombstone

## Claim checked

A `REMOVE` action records one singular removed-state result while preserving independent real-change and Journal evidence.

## Test case

Remove one governed subject with an accepted present result, validate the structured Journal event, apply the real-change gate, batch the Journal record later, and reconcile the transition.

## Acceptance criteria

The canonical Journal result has `state: removed`, the removed filename and revision, omits present-only path and digest fields, and refers to the immediate prior present result. The real-change commit contains only the removal target and its Initiative-based message. The later Journal-only batch contains only Journal carriers, and reconciliation binds both without a duplicate event.

## Failure disposition

Reject the removal if the tombstone is absent or plural, retains present-only fields, lacks the immediate prior-result reference, or mixes Journal changes into the real-change commit.
