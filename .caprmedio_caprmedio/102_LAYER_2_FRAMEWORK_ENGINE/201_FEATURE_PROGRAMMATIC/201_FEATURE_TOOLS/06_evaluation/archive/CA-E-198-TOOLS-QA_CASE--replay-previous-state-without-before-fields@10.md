---
subjects:
  governs: "Work Journal/Event/Previous Result Event"
  depends_on: []
version: 10
updated_at: "2026-09-12 04:15:38 +0400"
relations:
  evaluation_for:
    - CAPRMEDIO-GOV-REQU-339
    - CA-M-087
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Replay previous state without before fields

## Claim checked

The immediate previous governed file state is recovered through `previous_result_event`, without copying before-state fields into the current event.

## Test case

Apply an `ADD`, two consecutive `UPDATE` actions, and a `MOVE+UPDATE` for one identity, then replay every transition only from each current event and the event referenced by `previous_result_event`.

## Acceptance criteria

The first event has no previous-result reference; each later event references exactly the immediate accepted prior result; replay reconstructs every transition; and no current event stores a copied before path, digest, filename, version, or message.

## Failure disposition

Reject the event chain at the first missing, stale, cyclic, non-immediate, or duplicated previous state.
