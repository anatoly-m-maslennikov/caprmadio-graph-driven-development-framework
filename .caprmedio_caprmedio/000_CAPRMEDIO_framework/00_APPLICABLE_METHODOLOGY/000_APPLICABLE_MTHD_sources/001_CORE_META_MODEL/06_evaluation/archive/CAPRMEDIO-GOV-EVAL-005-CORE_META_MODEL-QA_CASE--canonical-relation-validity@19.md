---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "relation validation"
  depends_on:
    - "Atom"
    - "Atom/Content Role"
    - "Atom/Status"
    - "Journal"
    - "Relation Kind"
    - "Relation Kind/Metadata"
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Relation/authority"
    - "Projection"
    - "Single Source of Truth"
version: 19
updated_at: "2026-09-22 23:02:20 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"evaluation_for":["CA-R-806","CA-R-1246","CA-R-1437","CA-R-1472","CA-M-120","CAPRMEDIO-GOV-REQU-767","CA-R-1580","CA-R-807","CA-D-268","CA-R-1040","CA-D-483", "CA-D-466"]}
---
# Summary

Canonical relation validity

## Claim

### Claim checked

**every** registered Relation Kind accepts valid examples **in** its owning graph kind **and** rejects unknown **or** misplaced Relation Kinds, invalid source **or** target classes, invalid cardinality, ambiguous targets, **and** endpoint lifecycle states prohibited for that Relation Kind.

### Applicable conditions

- admit **`=1`** valid example of **every** registered relation kind.
- reject an unknown relation kind.
- reject a relation **without** the endpoint cardinality required by its kind.
- resolve **every** target **to** **`=1`** addressable identity under its relation rules; reject missing **or** ambiguous targets.
- reject a non-Active RMED target of a direct Relation authored by an Active RMED Atom; read target Status from its own Markdown frontmatter under CA-D-483 **and** check lifecycle placement under CA-D-466. this Active-target restriction applies **only** **when** the source is Active **and** both source **and** target have Content Role **in** (Requirement, Method, Evaluation, Delivery). a source **or** target outside that boundary **must not** fail because of this restriction alone; its own applicable Relation constraints still apply.
- accept `A BLOCKS B` with Done Plan `A`; confirm that Backlog, Active, Canceled, **or** Archived blockers do **not** satisfy the Done start gate for `B`.
- confirm that an Archived target remains addressable as history **without** becoming Active authority.
- confirm that **every** independently authored direct Relation is persisted **only** **in** its registered declaration Carrier **and** that **every** inverse remains derived; validate a computed Relation against its admitted derivation authority **and** input facts **without** requiring an invented source declaration.
- confirm that replacement **and** absorption history uses explicit predecessor **and** successor identities **in** Journal events, **not** formal replacement relation payloads **in** active Atom frontmatter.
- accept valid uses of the same Relation Kind **in** multiple instances of its owning graph kind using the same governing definition.
- reject a Relation Kind registration with **`!=1`** owning graph kind, **or** missing **or** conflicting metadata required by CA-R-806.
- reject a Relation Kind admitted as native **in** a different graph kind even **when** its endpoint classes would **otherwise** be valid; an allowed external endpoint does **not** change the Relation Kind's owner.
- reject an invalid source class **and** an invalid target class independently while retaining the valid graph kind **and** other constraints.
- resolve two independently authorized Relation Kind registrations that share a canonical name by their graph-qualified identities; reject an unqualified lookup that cannot distinguish them **or** a registration merged by name alone.
- reject instance-specific redefinitions of a graph-kind vocabulary shared under the same Applicable Methodology.
- accept a source-traceable reference **or** derived graph view of a Relation fact; reject another independently maintained source declaration of the same fact **or** admission of a foreign Relation Kind as native through that view.
- require the compiled registry **to** preserve graph ownership, source traceability, direction, endpoint constraints, **and** **all** other metadata required by CA-R-806 **without** inventing missing authority.

- accept an admitted native Relation between nodes **in** the same secondary graph.
- accept an admitted typed reference **to** another secondary graph **or** its node while preserving endpoint identity **and** graph context.
- accept an admitted typed reference **to** a source Atom **without** making that Atom a native Term **or** other wrongly classified node.
- reject a cross-graph endpoint whose class **or** graph context is **not** admitted, even **when** both endpoints exist.
- reject loss of owning graph qualification, silent foreign-node import, **or** a projected Relation treated as independently authored authority.
- accept a source-traceable derived Relation **without** its own direct source declaration **only** **when** the governing Relation authority admits that derivation; reject its use **to** bypass an explicit-declaration requirement.

### Acceptance criteria

**all** valid fixtures pass **and** **every** invalid fixture fails with the exact Relation Kind, graph kind, metadata conflict, source declaration, endpoint, lifecycle restriction, **or** declaration Carrier identified.

### Failure disposition

record a Concern naming the affected Relation Kind **and** violated authority **and** stop relation-schema readiness.
