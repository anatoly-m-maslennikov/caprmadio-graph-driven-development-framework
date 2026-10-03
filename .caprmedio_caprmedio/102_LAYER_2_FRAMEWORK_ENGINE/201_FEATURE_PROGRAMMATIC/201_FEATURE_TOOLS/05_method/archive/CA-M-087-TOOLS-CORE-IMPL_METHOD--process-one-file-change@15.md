---
subject_scopes:
  - provenance
version: 15
updated_at: 2026-08-23 16:45:00 +0400
relations:
  method_for:
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
---
# Process one project-path action

Use this composite Method for one sealed project-path action. The subject is one file or one non-empty folder; a folder action has one frozen ordered entry set and remains one action. `COMMIT_TRIGGER`, `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and `COMMIT_CHANGE_SET` are peer Tools, not parts of this Method.

1. An authorized MCP Atom mutation or registered project-change adapter supplies a sealed Initiative and stable action identity to `COMMIT_TRIGGER`. The Trigger validates the intake boundary, durably records one idempotent outbox item, and returns intake acknowledgement without gathering context, appending a Journal record, or waiting for Git.
2. One or more `COMMIT_CONTEXT` workers read that outbox item. Each produces a provisional deterministic context with the Initiative, expected frontier, resolved atomic target or frozen folder entry set, and provenance facts. An effectful consumer always revalidates it at its own boundary.
3. `APPEND_CHANGE_RECORDS` may prepare and append the action's canonical Journal record independently. Journal append is action-owned and idempotent; shared-carrier serialization belongs to the Journal writer or batcher, not to the Git gate. A Journal-only batch may later commit selected Journal carrier changes through the gate.
4. `COMMIT_CHANGE_SET` is the only Git-mutation gate. Its lease holder and fencing token revalidate the sealed Initiative, current outbox state, expected Git base, target frontier, and complete staged target set immediately before each Git effect. It creates one real-change commit containing all and only the action's governed target changes, with the Initiative-based message Projection; that commit does not require or include the Journal record.
5. A failed or interrupted append, real-change commit, or Journal batch remains a durable recoverable action. Reconciliation binds the independent Git and Journal evidence when available and never replays an uncertain Git mutation as a second commit.

Return the common Tool result envelope. Dry run reports only predicted context, outbox/gate eligibility, message Projection, and Journal eligibility; it mutates nothing. The Method never edits the governed subject content or infers Atom meaning beyond the explicitly admitted action.
