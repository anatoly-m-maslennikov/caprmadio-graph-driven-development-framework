---
atom_id: CA-P-905
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
subjects:
  governs:
    continuant:
      - Accepted Atom Update Frontier
    occurrent:
      - Atom Update Frontier Freezing
  depends_on:
    continuant:
      - FPF Term-System Challenge Result
version: 1
updated_at: 2026-08-28 21:11:50 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Freeze Accepted Term-System Atom Update Frontier

the Assignee **must** freeze the exact accepted decision frontier and every active or draft Atom whose content may need change before any authority Atom is updated.

## Scope

`((fpf-reports/20260828T160248Z-fpf-design-challenge-caprmedio-term-system.md) union (the accepted Operator corrections listed in Details) union (all active and draft non-Bootstrap Atoms whose Claims or Subject metadata define, constrain, serialize, evaluate, or apply any listed Entity, Property, value, Subject Expression, Relation Kind, Artifact kind, Atom classification, Scope Unit rule, Plan rule, Status rule, Carrier rule, Methodology Source rule, or Applicable Methodology rule))`

## Definition of Done

the Task is **not done if** (any accepted Operator correction is absent from the frozen decision set **or** any affected active or draft non-Bootstrap Atom is absent from the frozen Carrier manifest **or** any listed Carrier lacks its exact path, digest, Atom identity when applicable, current lifecycle location, and one disposition in (UPDATE, REPLACE, ARCHIVE_AS_CONFLICT, KEEP) **or** any historical Bootstrap Carrier is selected for mutation **or** any mutable authority Carrier is assigned to more than one direct update Task **or** any affected authority Claim is assigned to no direct update Task **or** any Project-specific Delivery authority is classified as Methodology authority **or** any uncertainty below 99 percent is resolved without Operator disposition).

## Details

freeze the following accepted decisions: the Term system uses SUBTYPE_OF, IS_BORNE_BY, and IS_ALLOWED_VALUE_OF; `/` serializes bearer dependence and `:` serializes an allowed value while permitting further bearer qualification; Type is borne by a value-qualified Content Role; Core default Concern Types are Question, Conflict, and Problem; Core default Analysis Types are Analysis Report and Rationale; Local Tier remains distinct from Atom Type; every governed Term and Subject Expression segment uses initial capitalization, but registered CCE operators remain lowercase and bold in Atom content; no Entity name contains `/`; no governed Term or Scope Unit name equals a registered CCE operator; Subjects are independent of Artifacts; each Claim-Subject relation has one Kind in (GOVERNS, DEPENDS_ON) and one Temporal Form in (CONTINUANT, OCCURRENT); Core Meta-Model is open; SUBTYPE_OF is an acyclic multiple-inheritance graph; every Entity bears zero or more Properties and every Property occurrence has exactly one bearer; every Atom has one independently replaceable Claim and one atomic or composite Claim Scope; logical composition does not create multiple Claims or Claim Scopes unless a component can be independently governed; Summary is a non-authoritative navigation Projection derived from the complete Claim and Claim Scope; every Carrier-specific Claim has Content Role Delivery; CARRIES with inverse IS_CARRIED_BY relates Carrier to Artifact Revision; Current Scope and Claim Scope are references; only a Job Atom may establish a Scope Unit; Job and Demand are distinct Requirement Atom Types; Epic and Scope Unit are folder-carried Relational Artifacts; Relational Atom and Relational Artifact are distinct; Epic may recursively contain Epics; CONTAINS with inverse IS_CONTAINED_BY is derived only by Delivery from canonical Carrier nesting for folder Relational Artifacts and is never declared separately; Demand needs no additional relation kind beyond its Consumer and Producer references; Status is Type-qualified, while Delivery maps Active to the current folder and every other value to its status subfolder; relations are graph-specific; concrete CAPRMEDIO folder names are Project Delivery authority; Methodology Source is the target role of DERIVED_FROM; Applicable Methodology is a Projection and Relational Artifact whose Delivery-projected files carry exact source Atom Revisions; CORE_META_MODEL, LOCAL_CONFIGURATION, and extension Scope Units are named instances rather than Scope Unit subtypes. produce a deterministic manifest that partitions every mutable authority Carrier among CA-P-906 through CA-P-914 and CA-P-916.
