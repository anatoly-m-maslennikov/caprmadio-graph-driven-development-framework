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
# How should the Four-set selection QA draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- Draft Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/drafts/CA-E--CORE_META_MODEL-QA_CASE--validate-ownership-and-target-scope-unit-selections.md`.
- prior Draft inspected SHA-256: `a3782b2471eb6695ddbee37169621382e2a790b2b84739a4d0994c359f9d6b40`.
- review point: 51 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise** — Keep cross-owner/incomplete-frontier cases; target Claim Structural Entity and add Plan-Hub invariance.
>
> Basis: `CA-M-273`, `CA-R-1448`, `CA-R-1449`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-M-273@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets.md`; SHA-256 `7b4cb4512b5e4f8f63694c89dc3cd641b902e1c88dfd0374412cca66403f10c8`.
- `CA-R-1448@5`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms.md`; SHA-256 `8742763eeced903bf47e2762ea1d164d46a161ac914a2b22ae82f3807a68a059`.
- `CA-R-1449@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms.md`; SHA-256 `42c83e58102b052f2a6aef7e6655cebcf4fc651056b24ac316d7b2fb2b44b906`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the Operator decision: `Atom/Claim/Target Scope Unit` is the structural target Property; Claim Scope is applicability expressed within Claim text, **not** a separate metadata Property. this decision supersedes the older terminology **in** the quoted review.

- disposition: revised **and** retained **in** Draft; no promotion occurred. the exact prior draft is preserved at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--MMODEL-QA_CASE--validate-claim-target-atom-set-selection@1.md`.
- surviving authority: `CA-M-273`, `CA-E-460`.
- structural ownership remains independent; text restrictions do **not** add targets **or** make an Atom Relational by themselves.
- CA-M-002 favors one authority for each fact; CA-M-006 requires coherent consumers; CA-R-1490 is satisfied by exact archives **and** preserved useful checks.
- the incoming filename-reference scan found **only** this Question; its current locator is updated. historical quotations **and** their recorded hashes remain unchanged.
- confidence **>=99%** for this bounded reconciliation; no new design decision remains **in** this review point. Tools, generated Projections, **and** other draft groups are outside this change.
