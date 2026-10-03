---
cce_version: cce_1
cce_form: evaluation
artifact_subtype: qa_case
subjects:
  governs:
    occurrent:
      - evaluation
version: 8
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  check_of:
    - CAPRMEDIO-GOV-METH-006--canonical-artifact-relations
  child_of:
    - CA-R-1054
---
# Canonical relation validity

## Claim checked

**every** registered relation accepts valid endpoints **and** rejects unknown kinds, invalid cardinality, **and** ambiguous active targets.

## Applicable conditions

1. Admit one valid example of **every** registered relation kind.
2. Reject an unknown relation kind.
3. Reject a relation **without** the endpoint cardinality required by its kind.
4. Resolve **every** target by active identity **and** reject zero **or** multiple active matches.
5. Confirm an archived target remains addressable as history but does **not** become active authority.
6. Confirm **every** direct relation is persisted **only** **in** its registered `declaration_carrier`, **and** that **every** inverse remains derived.
7. Confirm `replaced_by` occurs **only** **in** the archival Work Journal event, **not in** (predecessor **or** successor) Atom frontmatter.

## Acceptance criteria

**all** valid examples pass **and** **every** invalid fixture fails with the exact relation, endpoint, **or** declaration carrier identified.

## Failure disposition

Record a Concern naming the relation **and** invalid endpoint behavior **and** stop relation-schema readiness.
