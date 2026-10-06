---
atom_id: CA-O-081
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Prepare Atom Carrier Validation"
  depends_on:
    - "Action"
    - "Action/Execution Kind"
    - "Atom"
    - "Atom/Revision"
    - "Scope Unit"
    - "Applicable Methodology"
    - "Projection"
    - "Artifact/Carrier"
    - "Operator"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  relates_to:
    - CA-D-305
    - CA-D-478
    - CA-D-479
    - CA-D-482
    - CA-D-483
    - CA-R-1598
---
# Summary

Prepare Atom Carrier validation

## Claim

Prepare Atom Carrier Validation **means** the Programmatic Action that returns a bounded validation input set **and** its applicable machine-checkable authority **without** changing sources.

- inputs: a requested folder, explicit applicable methodology context, caller-selected membership restrictions, reference-resolution context, admitted read boundaries, **and** any selected execution limits.
- precondition: the caller has authority **to** read the requested inputs; missing permission is **not** supplied by this Action.
- inspect Markdown Carrier candidates within the requested boundary. retain candidates with malformed **or** missing Atom metadata; a filename **may** locate a candidate but **must not** supply an Atom Property.
- distinguish source Atoms, projected copies, history, **and** non-Atom material from declared values **and** supplied context. ambiguous classification remains visible. report **every** excluded candidate with its reason; do **not** treat an unreadable directory, broken link, missing identity, **or** parse failure as an empty successful selection.
- resolve admitted Properties, Carrier sections, Content Roles, Types, Status models, cardinalities, Subject forms, **and** Relation ownership/target constraints from the applicable authority. bind each executable check **to** its governing Atom identity **and** exact Revision.
- preserve content fingerprints **and** exact definition bindings for the target set, rule authority, reference context, **and** relevant selection inputs. external references **may** be resolved against the supplied context **without** expanding the reported target coverage.
- return prepared with the complete input set **and** checks, incomplete with explicit gaps **when** selection **or** authority is unresolved, **or** error for an execution failure. an empty target set returns incomplete rather than proving Atom conformance.

this Action performs no source edits, repairs, network fetches, **or** secret discovery. protected **or** out-of-bound targets are reported **without** reading their content.
