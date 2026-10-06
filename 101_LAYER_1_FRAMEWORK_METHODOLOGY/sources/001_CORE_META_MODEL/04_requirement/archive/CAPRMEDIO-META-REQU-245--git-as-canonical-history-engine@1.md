---
subject_scope: lifecycle-traceability
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-244--revision-bound-parent-child-transactions
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom
---

# Requirement — Use Git as the canonical history engine

Every CAPRMEDIO-governed project must use Git as its canonical engine for the
persisted history of governed artifacts and their implementation.

Artifact carriers and their relations remain authoritative for current
semantic meaning. Git is authoritative for when and how their persisted
revisions were created, changed, moved, archived, or connected to dependent
work.

Each committed carrier revision is an addressable historical snapshot.
Revision-bound parent-to-child transactions must be recoverable from reachable
Git history. Once another revision depends on a committed revision, that
history must not be rewritten or made unreachable.

CAPRMEDIO must not maintain a second lifecycle ledger as a competing history
authority. Append-only runtime logs and external-system histories may record
operational observations, but they do not replace Git history for persisted
repository state.

GOV defines the concrete commit and archival conventions. Tools may index,
validate, and present Git history, but generated indexes are derived and
rebuildable.

## Primary claim

Git is the canonical history engine for persisted CAPRMEDIO-governed repository
state.

## Rationale

Using the repository's existing version-control history avoids duplicated
lifecycle state while preserving replayable revisions, provenance, renames,
archives, and dependency-bound change transactions.
