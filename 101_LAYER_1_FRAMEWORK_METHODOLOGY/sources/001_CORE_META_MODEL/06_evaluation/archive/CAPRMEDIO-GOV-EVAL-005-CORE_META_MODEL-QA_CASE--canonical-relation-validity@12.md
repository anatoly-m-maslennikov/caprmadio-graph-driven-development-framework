---
atom_id: CAPRMEDIO-GOV-EVAL-005
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - relation validation
  depends_on:
    continuant:
      - Atom
      - Atom/Content Role
      - Atom/Status
      - Journal
      - Relation Kind
      - Relation Kind/Metadata
      - CAPRMEDIO Graph
      - Applicable Methodology
      - Relation/authority
      - Projection
version: 12
updated_at: "2026-09-11 05:04:26 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
    - CA-M-120
    - CAPRMEDIO-GOV-REQU-767
    - CA-R-1007
    - CA-R-807
    - CA-D-268
    - CA-R-1040
---
# Canonical relation validity

## Claim checked

**every** registered Relation Kind accepts valid examples **in** its owning graph kind **and** rejects unknown **or** misplaced Relation Kinds, invalid source **or** target classes, invalid cardinality, ambiguous targets, **and** endpoint lifecycle states prohibited for that Relation Kind.

## Applicable conditions

1. admit **`=1`** valid example of **every** registered relation kind.
2. reject an unknown relation kind.
3. reject a relation **without** the endpoint cardinality required by its kind.
4. resolve **every** target to **`=1`** addressable identity under its relation rules; reject missing **or** ambiguous targets.
5. reject a non-Active RMED target of a direct relation authored by an Active RMED Atom.
6. accept a Task dependency that resolves to a Done prerequisite Task; confirm that Draft, Active, **or** Cancelled prerequisites do **not** satisfy the Done completion gate.
7. confirm that an Archived target remains addressable as history **without** becoming Active authority.
8. confirm that **every** direct relation is persisted **only** in its registered declaration Carrier **and** that **every** inverse remains derived.
9. confirm that replacement **and** absorption history uses explicit predecessor **and** successor identities in Journal events, **not** formal replacement relation payloads in active Atom frontmatter.
10. accept valid uses of the same Relation Kind **in** multiple instances of its owning graph kind using the same governing definition.
11. reject a Relation Kind registration with **`!=1`** owning graph kind, **or** missing **or** conflicting metadata required by CA-R-806.
12. reject a Relation Kind used **in** a different graph kind even **when** its source **and** target classes would **otherwise** be valid.
13. reject an invalid source class **and** an invalid target class independently while retaining the valid graph kind **and** other constraints.
14. resolve two independently authorized Relation Kind registrations that share a canonical name by their graph-qualified identities; reject an unqualified lookup that cannot distinguish them **or** a registration merged by name alone.
15. reject instance-specific redefinitions of a graph-kind vocabulary shared under the same Applicable Methodology.
16. accept a source-traceable reference **or** derived graph view of a Relation fact; reject another independently maintained source declaration of the same fact **or** admission of a foreign Relation Kind as native through that view.
17. require the compiled registry **to** preserve graph ownership, source traceability, direction, endpoint constraints, **and** **all** other metadata required by CA-R-806 **without** inventing missing authority.

## Acceptance criteria

**all** valid fixtures pass **and** **every** invalid fixture fails with the exact Relation Kind, graph kind, metadata conflict, source declaration, endpoint, lifecycle restriction, **or** declaration Carrier identified.

## Failure disposition

record a Concern naming the affected Relation Kind **and** violated authority **and** stop relation-schema readiness.
