---
subject_scope: lifecycle-traceability
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-217--three-revision-modes-without-evergreen
      - CAPRMEDIO-META-REQU-236--drafts-precede-atomic-admission
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-243--single-claim-atomic-artifacts
      - CAPRMEDIO-META-REQU-244--revision-bound-parent-child-transactions
      - CAPRMEDIO-META-REQU-245--git-as-canonical-history-engine
---

# Requirement — Preserve Atomic Artifacts as immutable committed revisions

CAPRMEDIO has exactly three Revision modes:

```toml
revision_mode = "atomic" # atomic | append_only | maintained
```

- `atomic` identifies one independently governed claim with a stable artifact
  ID and a Git-addressed sequence of committed revisions.
- `append_only` identifies a growing sequence whose accepted records cannot be
  edited, reordered, or removed.
- `maintained` identifies a current artifact revised through its registered
  update procedure.

`evergreen` is not a Revision mode or lifecycle term.
Revision mode governs change behavior; it does not establish semantic truth.

Atomicity and immutability are distinct. The Atomic Artifact is the continuing
identity of one primary claim. Each committed carrier revision is immutable
and recoverable through Git; the current carrier may gain a later committed
revision under the same artifact ID.

A later revision may clarify, refine, or change the applicability of the claim
only while preserving its primary identity. A different independently
replaceable claim requires a new Atomic Artifact ID and an applicable typed
relation. GOV defines the operational change classes and admission gate.

Every dependency binds to the exact committed revision it consumed. A later
revision never retargets an existing dependency. After any referenced atom
gains a new revision, the lineage-impact invariant determines which dependent
branches remain valid and which require further work.

A Draft remains a mutable pre-admission candidate. It has no stable artifact
ID, consumes no sequence number, carries no project authority, and cannot be a
dependency target. Admission assigns the stable ID and creates the active
Atomic Artifact's initial committed revision.

Draft, active, and archived carrier conditions are derived from placement and
Git history. They are not duplicated as frontmatter status fields. Archival
ends the artifact's current authority but does not remove any committed
revision. “Created based on” always means an explicit revision-bound governed
transaction, not textual similarity or an inferred dependency.

Append-only records become immutable when appended. Maintained artifacts
remain mutable under their registered procedures.

## Primary claim

An Atomic Artifact is one stable claim identity whose committed Git revisions
are individually immutable and whose dependencies bind to exact revisions.

## Rationale

Revision immutability preserves the exact meaning consumed by every dependent
without forcing a new artifact identity for every clarification. Stable IDs,
exact revision bindings, and lineage-impact review keep evolution auditable
without losing historical semantics.
