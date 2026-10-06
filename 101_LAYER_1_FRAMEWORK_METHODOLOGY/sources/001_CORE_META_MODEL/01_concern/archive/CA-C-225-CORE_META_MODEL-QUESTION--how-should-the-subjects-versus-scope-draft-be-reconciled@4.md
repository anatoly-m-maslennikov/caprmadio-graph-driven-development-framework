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
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
---
# How should the Subjects versus scope draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived proposal Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--separate-subject-paths-from-scope-coordinates@4.md`.
- inspected SHA-256: `cb26da734ccb0c0ac658d5b7396e76ea9ec419a0f7f8acb541f857b01373ac0a`.
- review point: 16 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise** — Retain the distinction, but replace the obsolete Governed Subject Set with the single direct governed target.
>
> Basis: `CA-R-1201`, `CA-R-1363`, `CA-M-273`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-1201@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1201-CORE_META_MODEL-CORE-REQUIREMENT--require-one-governed-subject-on-every-atom.md`; SHA-256 `2485221d389e3833ab085a3eb3ee37bdec36a8d4fd1642e875d82f67cc3ec3ba`.
- `CA-R-1363@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1363-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-governed-subject.md`; SHA-256 `ded2047969f14db672ebc14c6e77cbe8dae84aacc791a2301132b3e7cdd80412`.
- `CA-M-273@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets.md`; SHA-256 `7b4cb4512b5e4f8f63694c89dc3cd641b902e1c88dfd0374412cca66403f10c8`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved at confidence **>=99%** under the Operator decision: a Subject is a GOVERNS **or** DEPENDS_ON Relation between an Atom **and** an Entity; Actions **and** Workflows are Operations Atoms **and** therefore Entities. the Operator authorized group-2 repair **and** promotion.

the corrected draft is promoted as CA-R-1597. Subject Paths identify Entity targets, not structural ownership or Claim Target Scope Unit. the obsolete Governed Subject Set is removed. contextual Atom Scope still includes the Governed Subject and textual restrictions under CA-R-1014; the promoted Claim does not contradict that rule.

- surviving active authority: CA-R-1597, CA-R-1275, CA-R-1014, CA-E-246.
- CA-M-002 (DRY), CA-M-005 (necessary complexity), **and** CA-M-006 (coherence) favor the existing target identities **and** one assignment policy.
- CA-R-1490 (valuable information) is satisfied by the exact archived proposal bytes **and** retained useful constraints; CA-E-001 is supported by the revised CA-E-246 fixtures.
- the incoming filename-reference scan found **only** this Question; its locator now addresses the archive. unrelated drafts **and** historical review evidence are unchanged.
- active promoted Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1597-CORE_META_MODEL-CORE-REQUIREMENT--separate-subject-paths-from-scope-coordinates.md`; initial accepted Version **`=1`**.
