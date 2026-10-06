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
version: 11
updated_at: "2026-09-10 05:28:44 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CA-R-806
    - CAPRMEDIO-GOV-REQU-767
    - CA-R-1007
    - CA-R-807
    - CA-D-268
    - CA-R-1040
---
# Canonical relation validity

## Claim checked

**every** registered relation accepts valid endpoints **and** rejects unknown kinds, invalid cardinality, ambiguous targets, **and** endpoint lifecycle states prohibited for that relation.

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

## Acceptance criteria

**all** valid fixtures pass **and** **every** invalid fixture fails with the exact relation, endpoint, lifecycle restriction, **or** declaration Carrier identified.

## Failure disposition

record a Concern naming the relation **and** invalid endpoint behavior **and** stop relation-schema readiness.
