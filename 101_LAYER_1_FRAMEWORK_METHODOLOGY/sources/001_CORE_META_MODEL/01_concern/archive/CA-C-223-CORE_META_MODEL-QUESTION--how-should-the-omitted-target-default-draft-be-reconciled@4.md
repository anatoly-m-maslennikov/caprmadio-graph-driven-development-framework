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
# How should the Omitted target default draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--resolve-omitted-claim-target-scope-to-current-scope-unit@1.md`.
- inspected SHA-256: `091249566391bbd29c17d3478b5bb78d65411d9811101ffe044441657c4b51d8`.
- review point: 14 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Retire** — Current structural-target serialization and resolution already own this behavior.
>
> Basis: `CA-D-367`, `CA-M-273`, `CA-R-1588`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-D-367@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-367-CORE_META_MODEL-DELIVERY--serialize-claim-structural-entity-only-for-relational-atoms.md`; SHA-256 `1c8fc657fad1462771e98190f36f0d0052b5a553fd82e24eaeff0b366b8b1da9`.
- `CA-M-273@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets.md`; SHA-256 `7b4cb4512b5e4f8f63694c89dc3cd641b902e1c88dfd0374412cca66403f10c8`.
- `CA-R-1588@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1588-CORE_META_MODEL-CORE-REQUIREMENT--default-plan-target-to-the-enclosing-scope-unit.md`; SHA-256 `d63c04f1adcf30553d3e2da1a866da65f7842368871970b1f105330b933190be`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the Operator decision: `Atom/Claim/Target Scope Unit` is the structural target Property; Claim Scope is applicability expressed within Claim text, **not** a separate metadata Property. this decision supersedes the older terminology **in** the quoted review.

- disposition: archived as superseded; the exact original bytes, Version, **and** timestamp remain recoverable. no promotion occurred.
- surviving authority: `CA-D-476`, `CA-M-273`, `CA-R-1588`.
- structural ownership remains independent; text restrictions do **not** add targets **or** make an Atom Relational by themselves.
- CA-M-002 favors one authority for each fact; CA-M-006 requires coherent consumers; CA-R-1490 is satisfied by exact archives **and** preserved useful checks.
- the incoming filename-reference scan found **only** this Question; its current locator is updated. historical quotations **and** their recorded hashes remain unchanged.
- confidence **>=99%** for this bounded reconciliation; no new design decision remains **in** this review point. Tools, generated Projections, **and** other draft groups are outside this change.
