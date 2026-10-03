---
atom_id: CA-M-087
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - provenance
version: 19
updated_at: 2026-09-04 03:10:59 +0400
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
4. From sealed context, advance two independent branches. An APPEND_CHANGE_RECORDS worker prepares and appends the action's canonical Journal record idempotently through the canonical writer; shared-carrier serialization belongs to the Journal writer or batcher. Independently, a real-change item becomes eligible for the Git gate without waiting for the Journal branch.
5. A COMMIT_CHANGE_SET worker alone owns the repository-scoped fenced Git lease. It revalidates the sealed Initiative, action state, expected Git base, target frontier, and complete staged target set immediately before commit creation. It creates either one real-change commit containing all and only the action targets or one separate Journal-only batch commit containing only selected Journal carriers. It never imports or invokes its peer Tools and rejects every non-commit Git operation.
6. Persist each branch's transitions independently through queued, reconciling, context_sealed, journal_pending or journaled, real_change_pending or real_change_committed, journal_commit_pending or journal_committed, and completed or no_change, with explicit retry_wait, paused, blocked, and dead_letter outcomes. Resume from the last safe persisted phase and reconcile uncertain commit outcomes before any replay.
7. Reconcile at low frequency while enabled so missed Hook delivery and external project edits do not make a host callback the correctness boundary.

Return the common Tool result envelope. Dry run predicts only context, queue and gate eligibility, message Projection, and Journal eligibility. This Method never edits governed subject content, infers Atom meaning beyond the admitted action, or performs branch, upstream, remote, synchronization, push, tag, or release operations.
