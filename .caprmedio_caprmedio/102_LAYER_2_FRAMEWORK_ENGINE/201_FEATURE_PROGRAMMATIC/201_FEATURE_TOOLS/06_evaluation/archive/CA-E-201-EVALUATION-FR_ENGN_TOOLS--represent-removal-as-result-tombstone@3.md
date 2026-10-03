---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-20 23:50:00
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CHANGE_SET--commit-one-governed-file-action
---
# Represent removal as a result tombstone

## Claim checked

A `REMOVE` event records a singular removed-state result and refers to the last present result without copying its path or digest.

## Test case

Remove one governed subject with an accepted present result, validate the structured event, replay the transition, render the commit message, and inspect the committed tree.

## Acceptance criteria

The current `result` has `state: removed` plus the removed filename and version, omits `path` and `sha256`, references the immediate last present event through `previous_result_event`, renders the canonical `REMOVE` message, and commits the subject removal plus all and only related sidecars.

## Failure disposition

Reject the removal if the tombstone is absent or plural, retains present-only fields, lacks the immediate previous-result reference, or produces a non-replayable transition.
