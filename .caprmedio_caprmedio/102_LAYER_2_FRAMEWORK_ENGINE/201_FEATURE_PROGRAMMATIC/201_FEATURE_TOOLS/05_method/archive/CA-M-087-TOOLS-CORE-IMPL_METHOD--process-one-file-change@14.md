---
subject_scopes:
  - provenance
version: 14
updated_at: "2026-08-23 11:48:51"
relations:
  method_for:
    - CA-R-803
    - CA-R-804
    - CA-R-805
    - CA-R-812
---
# Process one project-path action

Use this composite Method for one Git-admitted project-path action. The subject
can be one file or one non-empty folder; a folder action remains one action,
one Journal event set, and one commit rather than one action per file.

`COMMIT_TRIGGER`, `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and
`COMMIT_CHANGE_SET` are participating Tools/mechanisms, not unnamed
part-Methods. This Method governs their composition only; each Tool's own
Requirement owns its standalone contract.

1. `COMMIT_TRIGGER` observes the Git-admitted frontier, excludes
   `.caprmedio_runtime` and every other top-level dot-directory except
   `.caprmedio`, coalesces repeated observations by adapter and source-event
   identity, and gives one unchanged trigger to `COMMIT_CHANGE_SET`. The
   trigger carries repository identity, subject kind, before/after candidates,
   observation time, and a structured LLM-session candidate. The Tool does not
   classify Artifact meaning. If it cannot establish the boundary or required
   provenance, it emits no trigger and no action begins.
2. `COMMIT_CHANGE_SET` gives that trigger to the shared deterministic
   `COMMIT_CONTEXT` logic, which is also independently available as a
   read-only Finder. The Finder resolves one file or non-empty folder, its
   `ADD`, `MOVE`, `UPDATE`, or `MOVE+UPDATE` action, its ordered entry set and
   aggregate digest when it is a folder, and non-blocking direct typed relation
   references for an Atom. It seals the author, `llm_session`, timezone,
   `occurred_at`, action and event identities, paths, revisions, digests, Git
   base, sources, singular result, prior-result reference when available, and
   validation results as schema-version-3 `COMMIT_CONTEXT`. It may form a
   recovered baseline only from sufficient evidence. A rejected or incomplete
   context ends the action before any Journal, index, or Git mutation.
3. In dry-run mode, `COMMIT_CHANGE_SET` returns the sealed context, predicted
   ordered Journal sidecar records and partitions, lease availability, and the
   deterministic Git-message Projection without mutation. The presentation
   `<app>:<uuid>:<occurred_at>` is derived only; no session provenance is
   written to an Atom or Projection.
4. In apply mode, `COMMIT_CHANGE_SET` gives the sealed context to peer Doer
   `APPEND_CHANGE_RECORDS`. That Tool acquires the repository-scoped lease,
   repeats its preflight against the sealed inputs, appends and fsyncs the
   ordered idempotent Journal sidecars, and returns their ordered receipts plus
   the live lease token. Its internal Journal and runtime writes are suppressed
   from re-entering `COMMIT_TRIGGER`. An append failure returns no commit
   boundary; an interrupted or partial append retains one recoverable blocked
   action instead of creating a second event set.
5. `COMMIT_CHANGE_SET` accepts only a complete matching receipt set and live
   lease, repeats its mutation-boundary checks, stages exactly the one subject
   action with all and only its receipt-bound Journal lines, creates the one
   deterministic commit, and verifies the commit tree, records, message, and
   parent Git base before releasing the lease. Rename detection is disabled for
   this verification so the sealed before/after path boundary remains visible.
   A post-append failure retains the same blocked action, identities,
   `llm_session`, `occurred_at`, and receipts for idempotent retry; a different
   action waits until retry succeeds or an Operator resolves it.
6. Return the common Tool result envelope: on apply, the Journal receipts,
   lease disposition, and commit identifier; on dry-run, their predicted
   values. The flow never edits the governed subject content or infers graph
   meaning beyond the non-blocking typed relation decoration admitted to the
   sealed context.
