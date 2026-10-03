---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 3
updated_at: "2026-09-22 17:59:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the Target-scope QA draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- Draft Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/drafts/CA-E--CORE_META_MODEL-QA_CASE--validate-target-scope-unit-and-textual-claim-scope.md`.
- prior Draft inspected SHA-256: `73fb0f9da8b454192894c886ce0cf18e3a479196ba539033f58b52679d40ccfc`.
- review point: 52 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise** — Preserve useful ownership tests while separating Claim Scope restrictions from structural-target cardinality.
>
> Basis: `CA-R-919`, `CA-R-1446`, `CA-E-240`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-919@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-919-CORE_META_MODEL-CORE-REQUIREMENT--give-every-claim-one-structural-entity.md`; SHA-256 `11a17807a5bfd7fb871233ebe9801dd53f5e6a4c63808d0f8e7c603e878328ee`.
- `CA-R-1446@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1446-CORE_META_MODEL-CORE-REQUIREMENT--define-claim-structural-entity.md`; SHA-256 `01ede2ab34ecdaac39d9d3a62b37e9b66a4590bfa081332f247b47ce082d2f1f`.
- `CA-E-240@23`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-240-CORE_META_MODEL-QA_CASE--validate-atom-scope-and-claim-scope.md`; SHA-256 `1c36e58b64b53e275b85513ff9d7a6a559b5494ab650475d24843b88b7cdc102`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the Operator decision: `Atom/Claim/Target Scope Unit` is the structural target Property; Claim Scope is applicability expressed within Claim text, **not** a separate metadata Property. this decision supersedes the older terminology **in** the quoted review.

- disposition: revised **and** retained **in** Draft; no promotion occurred. the exact prior draft is preserved at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--MMODEL-QA_CASE--validate-claim-target-scope-semantics@1.md`.
- surviving authority: `CA-R-1595`, `CA-R-1596`, `CA-E-240`, `CA-D-476`, `CA-D-477`.
- structural ownership remains independent; text restrictions do **not** add targets **or** make an Atom Relational by themselves.
- CA-M-002 favors one authority for each fact; CA-M-006 requires coherent consumers; CA-R-1490 is satisfied by exact archives **and** preserved useful checks.
- the incoming filename-reference scan found **only** this Question; its current locator is updated. historical quotations **and** their recorded hashes remain unchanged.
- confidence **>=99%** for this bounded reconciliation; no new design decision remains **in** this review point. Tools, generated Projections, **and** other draft groups are outside this change.
