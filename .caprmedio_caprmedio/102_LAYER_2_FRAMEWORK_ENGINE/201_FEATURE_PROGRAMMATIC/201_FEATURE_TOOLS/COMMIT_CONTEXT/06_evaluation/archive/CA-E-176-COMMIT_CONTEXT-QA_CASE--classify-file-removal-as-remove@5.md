---
subjects:
  declared:
    continuant:
      - evaluation
    occurrent:
      - evaluation
version: 5
updated_at: 2026-08-23 17:53:53 +0400
relations:
  evaluation_for:
    - CA-M-087-METHOD-FR_ENGN_TOOLS--process-one-file-change
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_COMMIT_CONTEXT--gather-complete-commit-action-context
---
# Classify file removal as REMOVE

## Claim checked

Disappearance of one governed file identity from the active carrier address is classified only as `REMOVE`.

## Test case

Supply a trigger whose committed graph contains one governed file identity that is absent from the resulting working and staged graph.

## Acceptance criteria

The sealed context reports `REMOVE`, emits one removed-state `result` with the removed filename and version but no present-only path or digest, references the immediate last present result through `previous_result_event`, and resolves upstream relations from the last committed graph.

## Failure disposition

Reject classification and report any competing change set, missing or malformed tombstone, missing immediate previous-result reference, copied before-state field, or incorrect relation source.
