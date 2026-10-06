---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-242--immutable-committed-atomic-revisions
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-229--closed-constitutional-amendment-protocol
      - CAPRMEDIO-META-REQU-241--atomic-only-governance-phase
---

# Requirement — Give every Atomic Artifact one independently replaceable claim

One Atomic Artifact owns exactly one independently replaceable claim. “One”
describes a lifecycle and replacement unit, not a sentence, paragraph, or file
length.

A candidate contains more than one claim and must be split when any part can:

- be implemented independently;
- be checked or evidenced independently;
- be resolved independently;
- change without changing the rest; or
- be replaced while the rest remains valid.

Supporting rationale, examples, acceptance criteria, and relation references
may remain in the same carrier only when they explain or bound the one primary
claim rather than establish another independently replaceable claim.

This invariant applies to every Atomic Artifact Type. In particular:

- a Definition atom establishes one obligation, boundary, or desired outcome;
- a Problem atom establishes one observed discrepancy;
- an Evaluation atom establishes one check; and
- an Analysis atom establishes one primary conclusion.

Atomic identity liveness is binary:

- `active` means the artifact ID has a current carrier revision; and
- `dead` means the carrier is archived and the artifact ID is no longer
  current.

These conditions are derived from placement and relations, not stored as a
frontmatter status. Partial absorption, partial replacement, and partially
active artifact identities are forbidden. Earlier committed revisions remain
immutable Git history and may retain revision-bound dependents.

A multi-claim candidate must be split before admission. If an admitted
historical artifact contains several independently replaceable claims, one
governed replacement creates the complete set of single-claim successors and
replaces the predecessor in full. The predecessor moves unchanged to
`archive/` only after no part of its claim set remains current solely through
that predecessor. Its committed revisions and existing dependency bindings
remain reachable in Git.

## Primary claim

Every Atomic Artifact is one independently replaceable claim and is either
fully active or fully dead; CAPRMEDIO has no partial absorption state.

## Rationale

Single-claim atoms align implementation, evaluation, replacement, and archive
boundaries. A claim can then be superseded without silently killing unrelated
authority or leaving an ambiguous partially active predecessor.
