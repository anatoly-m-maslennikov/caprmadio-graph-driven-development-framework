---
subject_scope: artifact-model
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMEDIO-META-REQU-260--one-independently-replaceable-claim-per-atom
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-248--three-artifact-forms
      - CAPRMEDIO-META-REQU-254--eight-content-roles-with-delivery-and-ops
  - type: relates_to
    targets:
      - CAPRMEDIO-META-REQU-099--close-amendments-through-atoms-and-projections
      - CAPRMEDIO-META-REQU-274--place-rationale-in-analysis
---

# Requirement — Give every Atom one independently replaceable claim

One semantic-claim Atom owns exactly one independently replaceable claim. “One”
describes a lifecycle and replacement unit, not a sentence, paragraph, or file
length.

A candidate contains more than one claim and must be split when any part can:

- be implemented independently;
- be checked or evidenced independently;
- be resolved independently;
- change without changing the rest; or
- be replaced while the rest remains valid.

Examples, acceptance criteria, and relation references may remain in the same carrier only when they explain or bound the one primary claim rather than establish another independently replaceable claim. Material rationale is owned by a separate Analysis Atom under CAPRMEDIO-META-REQU-274--place-rationale-in-analysis. Text that determines the claim's normative meaning remains part of the claim and is not rationale.

Plan atomicity uses a bounded execution unit rather than the one-claim test. One
Plan file may contain multiple action points. Those points remain together while
they share one owner, lifecycle, execution boundary, and terminal disposition;
otherwise they belong in separate Plans.

The one-claim invariant applies to semantic-claim Atom Types. For example:

- a Requirement Atom establishes one obligation, boundary, or desired outcome;
- a Concern Atom establishes one matter requiring disposition;
- an Evaluation Atom establishes one check or proof obligation;
- a Delivery Atom establishes one delivery rule;
- a Method Atom establishes one realization approach;
- an Analysis Atom establishes one primary conclusion; and
- an Ops Atom establishes one enacted or observed fact.

Active semantic-claim Atom identity liveness is binary:

- `active` means the artifact ID has a current carrier revision; and
- `dead` means the carrier is archived and the artifact ID is no longer current.

These conditions are derived from placement and relations under
CAPRMEDIO-META-REQU-130--define-atom-admission-and-lifecycle, not stored as frontmatter status. A draft is
not yet active, while a completed Plan is terminal without representing a dead
semantic claim. Partial absorption, partial replacement, and partially active
artifact identities are forbidden. Earlier committed revisions remain
immutable Git history and may retain revision-bound dependents.

A Plan has three derived lifecycle placements: active while it is being revised
or executed, `done/` after every action point is executed, and `archive/` after
abandonment or full absorption. `done/` and `archive/` are both terminal and do
not keep the Plan active.

A multi-claim candidate must be split before admission. If an admitted historical artifact contains several independently replaceable claims, one governed replacement creates the complete set of single-claim successors and replaces the predecessor in full. The predecessor moves unchanged to `archive/` only after no part of its claim set remains current solely through that predecessor.

## Primary claim

Every semantic-claim Atom is one independently replaceable claim. A Plan is one
bounded execution unit containing one or more action points. Neither kind
permits partial absorption of its identity.
