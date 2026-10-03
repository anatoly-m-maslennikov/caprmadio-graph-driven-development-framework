---
subjects:
  governs: "Governed Change/Change Class"
  depends_on: []
version: 9
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-804
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
