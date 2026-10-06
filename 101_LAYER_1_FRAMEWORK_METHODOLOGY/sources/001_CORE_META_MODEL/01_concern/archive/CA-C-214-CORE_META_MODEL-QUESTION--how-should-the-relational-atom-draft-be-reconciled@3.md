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
# How should the Relational Atom draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--define-relational-atom-by-claim-target-scope@1.md`.
- inspected SHA-256: `3e16cf9ae34cfaa86146f0fe61e71f5c207318429308234275027af67262af65`.
- review point: 5 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Retire** — Superseded by the current structural-target definition.
>
> Basis: `CA-R-923`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-923@18`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-923-CORE_META_MODEL-CORE-REQUIREMENT--define-relational-atom.md`; SHA-256 `5bee4155f4ca9f2776f08b5f41f30eb22d5f4d05dde339d25afd409300a399e1`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the Operator decision: `Atom/Claim/Target Scope Unit` is the structural target Property; Claim Scope is applicability expressed within Claim text, **not** a separate metadata Property. this decision supersedes the older terminology **in** the quoted review.

- disposition: archived as superseded; the exact original bytes, Version, **and** timestamp remain recoverable. no promotion occurred.
- surviving authority: `CA-R-923`.
- structural ownership remains independent; text restrictions do **not** add targets **or** make an Atom Relational by themselves.
- CA-M-002 favors one authority for each fact; CA-M-006 requires coherent consumers; CA-R-1490 is satisfied by exact archives **and** preserved useful checks.
- the incoming filename-reference scan found **only** this Question; its current locator is updated. historical quotations **and** their recorded hashes remain unchanged.
- confidence **>=99%** for this bounded reconciliation; no new design decision remains **in** this review point. Tools, generated Projections, **and** other draft groups are outside this change.
