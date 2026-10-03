---
subjects:
  - relation-model
  - atom-boundary
version: 2
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  relates_to:
    - CAPRMEDIO-META-REQU-097--provenance-does-not-establish-ops-evidence
    - CAPRMEDIO-GOV-REQU-310--lineage-impact-dispositions
    - CAPRMEDIO-GOV-REQU-311--atomic-revision-change-classes
---
# Record one Lineage Impact Analysis per changed atom revision

Every `refinement`, `semantic_revision`, or `replacement` of an admitted
Atom produces one Analysis Atom whose primary conclusion
is the impact state of that exact changed parent revision.

The report records:

- the changed artifact ID and exact previous and new Git revisions;
- the assigned change class and the observed basis or rationale for the change;
- the responsible operator and session provenance already required for the
  Analysis carrier;
- the expected impact radius;
- every directly examined child and the exact child revision examined;
- one `compatible`, `update_required`, `replacement_required`, or `uncertain`
  disposition for each child;
- the evidence or reasoning supporting each disposition;
- every resulting child revision, successor, or blocking Concern Atom; and
- the recursive branch result and overall fixed-point conclusion.

One report may contain many child rows because those rows support the single
primary conclusion that the changed parent revision's impact review is
complete or blocked. The report does not replace the children, their evidence,
or their own semantic claims.

A compatible disposition is durably recorded in the Analysis Atom without
rewriting the child. An updated or replaced child continues the review
recursively. An uncertain disposition names its blocking Concern Atom and
leaves that branch incomplete.

The Analysis Atom is not Ops evidence of its own correctness. Material Ops
evidence remains claim-bound through explicit evidence relations. A release or
downstream gate that requires the revised atom must not pass until the report
concludes that every affected branch has reached a fixed point.

`carrier_only` changes require lossless-recoding Verification but do not
require a Lineage Impact Analysis Atom.

## Rationale

A single change-bound report avoids per-child artifact explosion while keeping
each disposition tied to exact revisions, supporting evidence, resulting work,
and a replayable completion boundary.
