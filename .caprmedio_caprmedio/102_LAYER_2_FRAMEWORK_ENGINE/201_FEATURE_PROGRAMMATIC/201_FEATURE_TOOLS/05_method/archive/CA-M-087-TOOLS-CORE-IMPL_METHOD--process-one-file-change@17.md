---
subjects:
  declared:
    continuant:
      - provenance
version: 17
updated_at: 2026-08-25 01:49:10 +0400
relations:
  method_for:
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
---
# Process one project-path action

Use this composite Method for one sealed project-path action. The subject is one file or one non-empty folder; a folder action has one frozen ordered entry set and remains one action.

1. COMMIT_TRIGGER atomically accepts one immutable source event into the Runtime inbox and returns. It performs no repository scan, context gathering, Journal append, staging, Git mutation, retry, or worker spawn.
2. The independently supervised COMMIT_AUTOMATION service reconciles inbox events with the current Git-admitted repository frontier. Its pure manager defines the fixed action graph and its mechanical Scheduler persists and advances only declared transitions. New events remain durable and mark the repository pending while another Git-mutating action is active.
3. A COMMIT_CONTEXT worker produces provisional deterministic context with the Initiative, expected frontier, resolved atomic target or frozen folder entry set, and provenance facts. Every effectful consumer revalidates those facts at its boundary.
4. An APPEND_CHANGE_RECORDS worker prepares and appends the action's canonical Journal records idempotently through the canonical writer. Shared-carrier serialization belongs to the Journal writer or batcher.
5. A COMMIT_CHANGE_SET worker alone owns the repository-scoped fenced Git lease. It revalidates the sealed Initiative, action state, expected Git base, target frontier, and complete staged target set immediately before the Git effect. It creates either one real-change commit containing all and only the action targets or one separate Journal-only batch commit. It never imports or invokes its peer Tools.
6. Persist transitions through queued, reconciling, context_sealed, journaled, committing, and completed or no_change, with explicit retry_wait, paused, blocked, and dead_letter outcomes. Resume from the last safe persisted phase and reconcile uncertain Git outcomes before any replay.
7. Reconcile at low frequency while enabled so missed Hook delivery and external project edits do not make a host callback the correctness boundary.

Return the common Tool result envelope. Dry run predicts only context, queue and gate eligibility, message Projection, and Journal eligibility. This Method never edits governed subject content or infers Atom meaning beyond the admitted action.
