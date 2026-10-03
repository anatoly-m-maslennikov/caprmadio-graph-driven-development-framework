---
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 4
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
---
# How should the Composite target scope draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-GENERAL-REQUIREMENT--permit-one-composite-claim-target-scope@1.md`.
- inspected SHA-256: `6a27da73b99b9b2ea0d3c56dbc26b6e1efcbfd60ce64ca90e3a5f14cf4ceb742`.
- review point: 20 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Retire** — Composite applicability remains Claim Scope; do not equate a selected Entity set with one structural target.
>
> Basis: `CA-R-1271`, `CA-R-919`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-1271@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1271-CORE_META_MODEL-GENERAL-REQUIREMENT--permit-one-composite-claim-scope.md`; SHA-256 `18148d27c5b0c71f2e9999e634dd85e7dcf37b92334a6a94a72c03e3410c1d94`.
- `CA-R-919@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-919-CORE_META_MODEL-CORE-REQUIREMENT--give-every-claim-one-structural-entity.md`; SHA-256 `11a17807a5bfd7fb871233ebe9801dd53f5e6a4c63808d0f8e7c603e878328ee`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the Operator decision: `Atom/Claim/Target Scope Unit` is the structural target Property; Claim Scope is applicability expressed within Claim text, **not** a separate metadata Property. this decision supersedes the older terminology **in** the quoted review.

- disposition: archived as superseded; the exact original bytes, Version, **and** timestamp remain recoverable. no promotion occurred.
- surviving authority: `CA-R-1271`, `CA-D-477`.
- structural ownership remains independent; text restrictions do **not** add targets **or** make an Atom Relational by themselves.
- CA-M-002 favors one authority for each fact; CA-M-006 requires coherent consumers; CA-R-1490 is satisfied by exact archives **and** preserved useful checks.
- the incoming filename-reference scan found **only** this Question; its current locator is updated. historical quotations **and** their recorded hashes remain unchanged.
- confidence **>=99%** for this bounded reconciliation; no new design decision remains **in** this review point. Tools, generated Projections, **and** other draft groups are outside this change.
