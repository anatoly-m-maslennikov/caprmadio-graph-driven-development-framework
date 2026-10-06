---
subjects:
  governs: "Workflow Run"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Step Run"
    - "Artifact/Revision"
    - "Journal"
    - "Operator"
version: 3
updated_at: "2026-09-21 00:57:42 +0000"
relations: {"relates_to": ["CA-R-1510", "CA-R-1511", "CA-R-1519", "CA-R-1520", "CAPRMEDIO-META-REQU-158"]}
---
# Bind Workflow Runs to exact definition Revisions

**every** Workflow Run **must** retain the exact Workflow graph Revision, referenced Step Atom Revisions, **and** referenced Action definition Revisions admitted for its execution.

- record references **to** those source Revisions **and** the actual binding used by **every** Step Run **in** the canonical Journal. do **not** create independently maintained copies of the definitions as another authority.
- **before** dispatch **and** on recovery, check whether a bound definition has changed, been withdrawn, **or** become unavailable. a detected change pauses further dispatch for revalidation; the executor **must not** silently substitute the newest Revision **or** assume the old binding remains authorized.
- revalidation **must** identify the exact definitions admitted for the remaining work, check their compatibility with completed effects **and** remaining inputs, **and** satisfy the applicable approval conditions. resume **only** **after** that decision is recorded; unresolved compatibility **or** authority keeps execution blocked.
- completed Step Runs retain their original definition bindings **and** outcomes. revalidation **must not** rewrite history, reset retry allowances, **or** automatically replay completed effects.
- an Action already running follows its admitted interruption policy; a definition change alone does **not** authorize forced termination **or** blind replay. retain its actual result under the binding used **and** revalidate **before** further dispatch.
- definition binding does **not** freeze permissions **or** mutable target state. current authorization, required Operator decisions, **and** input freshness still apply **before** effects.
- a successor Workflow Run obtains its own admitted definition bindings rather than silently inheriting the predecessor's bindings for another Workflow.
