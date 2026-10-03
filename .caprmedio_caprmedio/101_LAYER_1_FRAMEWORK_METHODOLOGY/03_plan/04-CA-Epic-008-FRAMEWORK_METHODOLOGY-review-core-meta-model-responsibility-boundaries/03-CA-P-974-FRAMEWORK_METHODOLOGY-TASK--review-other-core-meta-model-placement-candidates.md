---
atom_id: CA-P-974
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    occurrent:
      - "methodology ownership review"
  depends_on:
    continuant:
      - "Core Meta-Model"
      - "Extension"
      - "Local Configuration"
      - "Methodology Source/Expansion Boundary"
      - "Project"
      - "Applicable Methodology"
      - "Projection"
      - "Atom/Claim"
      - "Atom/Content Role"
      - "Atom/Local Tier"
      - "Confidence Threshold"
version: 1
updated_at: "2026-09-11 03:04:50 +0400"
relations:
  depends_on:
    - CA-P-973
---
# Review other Core Meta-Model placement candidates

the Assignee **must** review non-Settings responsibility boundaries for the active Claims **in** CORE_META_MODEL.

## Scope

(active Claims **in** CORE_META_MODEL screened for non-Settings destinations **and** their review evidence)

## Definition of Done

the Task is **not** Done **if** ((an inventoried Atom lacks a non-Settings screening result) **or** (a candidate lacks an evidence-backed retain, relocate, split, deduplicate, **or** retirement recommendation) **or** (a proposed destination lacks its ownership rationale) **or** (a reusable Core capability is removed merely because it currently serves caprmedio) **or** (an Extension **or** Local Configuration proposal violates Core expansion permission) **or** (a derived output is proposed as authoritative) **or** (a lower Local Tier **or** different Content Role is treated as proof of a different source owner) **or** (a conclusion below the effective Confidence Threshold bypasses the Operator) **or** (a recommendation is executed)).

## Details

review the complete inventory, including mixed Claims previously screened as Settings candidates. distinguish Project-specific methodology expansions for LOCAL_CONFIGURATION; optional reusable expansions that could belong **to** an Extension; actual caprmedio product decisions owned by Project Scope Units; derived facts owned by Projections; **and** execution-specific data owned by Tools **or** runtime state. a proposed future owner does **not** authorize creating a new Extension, Scope Unit, **or** Term.

retain the necessary reusable entities, relations, invariants, extension points, configuration mechanisms, **and** general RMED capabilities **in** CORE_META_MODEL. retain generic Applicable Methodology compilation authority as required by CA-R-1434; particular installed Extension identities **and** Local Configuration contents are separate concerns. coordinate recommendations with Epic CA-Epic-007 **without** executing **or** assuming completion of its Tasks.

check whether concrete workflows, tools, architecture views, catalog contents, naming choices, release choices, **or** obsolete Bootstrap constraints are generic model authority **or** belong **to** a narrower owner. treat those categories as hypotheses. historical Atoms remain excluded; active historical restrictions **may** be reviewed for justified retirement.

support **every** proposed move **or** split with exact source references, relevant Project Principles, **and** the authority that admits the destination. include affected direct references **and** subject declarations **in** the recommendation evidence. do **not** perform moves, role changes, tier changes, splits, retirement, reference rewrites, Settings edits, **or** Projection rebuilds.
