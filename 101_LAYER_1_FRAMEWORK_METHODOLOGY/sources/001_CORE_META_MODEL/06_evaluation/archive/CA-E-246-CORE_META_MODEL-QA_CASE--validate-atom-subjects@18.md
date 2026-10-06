---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Atom/Subjects"
  depends_on:
    - "Atom"
    - "Subject"
    - "Subject Path"
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Entity"
    - "Action"
    - "Workflow"
    - "Term"
    - "Projection/Type: Atom Subjects Graph"
    - "Concern"
    - "Atom/Claim"
    - "Atom/Content Role: Evaluation"
    - "Evaluation For Relation"
    - "Property"
    - "Primary Entity"
    - "Dependent Entity"
    - "Scope Unit"
    - "Atom/Scope"
    - "Atom/Claim/Target Scope Unit"
version: 18
updated_at: "2026-09-22 20:07:50 +0000"
relations:
  evaluation_for:
    - CA-R-1275
    - CA-R-1279
    - CA-M-125
    - CA-R-1018
    - CA-R-1248
    - CA-R-1194
    - CA-R-1192
    - CA-R-1193
    - CA-R-1201
    - CA-R-1202
    - CA-R-1452
    - CA-R-1508
    - CA-R-1597
    - CA-R-1014
    - CA-D-269
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Atom Subjects

## Claim checked

**every** Atom has valid typed Subject Relations with canonical target resolution **and** no separately identified intermediate Subject object.

## Test case

create valid flat Carrier fixtures with **`=1`** scalar GOVERNS target, **`>=0`** distinct scalar DEPENDS_ON targets, Entity targets including an Action Atom **and** a Workflow Atom, a qualified Subject Path, **and** a definition Claim. reuse the same Entity target, including an Action **or** Workflow Atom, from different Atoms: those Atoms have distinct Subject Relations **to** the same target **without** duplicating its definition **or** identity. distinguish a reusable Action **or** Workflow definition from a particular execution **and** its Journal Records.

introduce **in** the source Subjects encoding zero **or** multiple GOVERNS targets, an unresolved **or** ambiguous target, a nested Subject/Entity **or** Subject/Reference wrapper, a repeated source target-kind field, a stored copy of a target definition, a duplicate dependency, an omitted prerequisite, an invalid qualified path, a Term's spelling used **without** its canonical target, **and** a separate Entity identity invented for an existing Action **or** Workflow Atom. a definition whose GOVERNS reference identifies the wrong target **or** omits its defined terminal Term **must** fail. add `Atom/Content Role: Requirement/Type: Demand` as **`=1`** target path composed of **`=5`** Term references: `Atom`, `Content Role`, `Requirement`, `Type`, **and** `Demand`. its source Atom has **`=1`** GOVERNS Subject Relation **to** that target, **not** five Subjects. reject confusing the Relation with its target **or** treating the referencing Atom as defining **all** five Terms.

add conformance-check Evaluation fixtures whose direct GOVERNS Subject Relations identify the checked targets **and** whose `evaluation_for` relations separately identify the checked authority under CA-R-1018. reject a generic Evaluation label **or** check execution substituted for the checked target **and** a missing **or** invalid `evaluation_for` target. reject treating an Atom's Subject DEPENDS_ON reference **or** dependency-list position as Workflow execution order; preserve the separately governed Plan `BLOCKS` completion gate.

accept an unmigrated legacy temporal Carrier **only** under CA-D-269's migration-limited compatibility **and** confirm that its decoded direct references preserve the same targets **and** relation meanings. do **not** require temporal nesting on a migrated flat Carrier. a Projection **may** derive target classification from canonical authority **when** its own Spec calls for it; reject independent classification authority **or** a requirement **to** repeat that kind **in** source Subjects metadata. reject independent reauthoring of either a referenced definition **or** a projected relation fact.

an Action **or** Workflow Atom is a valid Entity target under its existing Atom identity. reject excluding it merely because it has Type Action **or** Workflow. being both an Atom **and** an Entity is **not** duplicate identity.

include a Property borne by a Primary Entity **and** a Property borne by a Dependent Entity, retaining **`=1`** immediate bearer **in** either case. reference the narrowest exact Entity for both GOVERNS **and** DEPENDS_ON; a broader bearer is invalid **when** the Claim actually concerns its qualified Dependent Entity. entry **or** exit criteria use this same target rule. do **not** invent a separate criterion Entity **without** governing authority.

give two Atoms the same Subject target but different owning Scope Units **and** different permitted explicit Claim Target Scope Units. preserve their independent ownership **and** targeting; reject deriving either Scope Unit from the Subject Path. preserve **any** textual Claim Scope constraints **in** the Claim **without** a separate scope field. this check does **not** remove the Governed Subject contribution **to** contextual Atom Scope under CA-R-1014.

## Acceptance criteria

**every** valid fixture passes. **every** invalid fixture fails with the affected Atom, direct Relation Kind, Subject Path, canonical target, representation, **or** cardinality rule. the Atom Subjects Graph reproduces exactly the selected direct references **without** another authoritative relation fact **or** Subject identity.

## Failure disposition

record a Concern naming **every** affected Atom **and** direct Subject reference.
