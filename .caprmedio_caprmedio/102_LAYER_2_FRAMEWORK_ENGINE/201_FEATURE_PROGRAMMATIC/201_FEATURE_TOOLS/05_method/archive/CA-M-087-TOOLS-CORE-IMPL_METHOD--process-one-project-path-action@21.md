---
atom_id: CA-M-087
cce_version: cce_1
cce_form: method
subjects:
  governs: "provenance"
  depends_on:
    - "Journal"
    - "Journal/Record"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 21
updated_at: "2026-09-16 21:24:29 +0000"
relations:
  relates_to:
    - CA-R-1491
  method_for:
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Process one project-path action

use this composite Method for **=1** sealed project-path action. its subject is **=1** file **or** **=1** non-empty folder; a folder action has **=1** frozen ordered entry set **and** remains **=1** action.

1. COMMIT_TRIGGER atomically accepts **=1** immutable source event into the Runtime inbox **and** returns. it performs no repository scan, context gathering, Journal append, staging, Git mutation, retry, **or** worker spawn.
2. the independently supervised COMMIT_AUTOMATION service reconciles inbox events with the current Git-admitted repository frontier. its pure manager defines the fixed action graph **and** its mechanical Scheduler persists **and** advances **only** declared transitions. new events remain durable **and** mark the repository pending while another Git-mutating action is active.
3. a COMMIT_CONTEXT worker produces provisional deterministic context with the Initiative, expected frontier, resolved atomic target **or** frozen folder entry set, **and** provenance facts. Project **or** Git mutation consumers revalidate their mutation preconditions at their effect boundary. Journal recording instead checks event **and** storage integrity under CA-R-1491; it does **not** require observed Project state **to** pass conformance checks **or** remain unchanged.
4. from sealed context, advance two independent branches. an APPEND_CHANGE_RECORDS worker prepares **and** appends the action's canonical Journal record idempotently through the canonical writer; shared-Carrier serialization belongs **to** that writer **or** batcher. preserve intact historical observations **without** silently rebinding them **to** later Project state. independently, a real-change item becomes eligible for the Git gate **without** waiting for the Journal branch.
5. a COMMIT_CHANGE_SET worker alone owns the repository-scoped fenced Git lease. it revalidates the sealed Initiative, action state, expected Git base, target frontier, **and** complete staged target set immediately **before** commit creation. it creates **=1** real-change commit containing **all** **and** **only** the action targets **or** **=1** separate Journal-only batch commit containing **only** selected Journal Carriers. it never imports **or** invokes its peer Tools **and** rejects **every** non-commit Git operation.
6. persist branch transitions independently through queued, reconciling, context_sealed, journal_pending **or** journaled, real_change_pending **or** real_change_committed, journal_commit_pending **or** journal_committed, **and** completed **or** no_change, with explicit retry_wait, paused, blocked, **and** dead_letter outcomes. resume from the last safe persisted phase **and** reconcile uncertain commit outcomes **before** replay.
7. reconcile at low frequency while enabled so missed Hook delivery **and** external Project edits do **not** make a host callback the correctness boundary.

return the common Tool result envelope. dry run predicts **only** context, queue **and** gate eligibility, message Projection, **and** Journal eligibility. this Method never edits governed subject content, infers Atom meaning beyond the admitted action, **or** performs branch, upstream, remote, synchronization, push, tag, **or** release operations.
