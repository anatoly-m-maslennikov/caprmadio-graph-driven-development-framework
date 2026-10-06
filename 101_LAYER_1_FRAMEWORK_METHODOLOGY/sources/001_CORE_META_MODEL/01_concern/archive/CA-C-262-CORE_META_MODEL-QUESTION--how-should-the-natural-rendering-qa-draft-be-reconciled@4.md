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
updated_at: "2026-09-22 17:30:37 +0000"
relations: {}
---
# How should the Natural-rendering QA draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--MMODEL-QA_CASE--validate-natural-renderings-of-qualified-subject-expressions@1.md`.
- inspected SHA-256: `e0228924e8b8cb5f27a419d21375959d165fb15d596caff5d8b91e35e1282b3a`.
- review point: 53 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise** — Fix `Content Role/Requirement`: allowed-value qualification needs `:`; distinguish valid references from ordinary prose.
>
> Basis: `CA-R-1204`, `CA-R-1245`, `CA-M-228`; I4. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-1204@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1204-CORE_META_MODEL-REQUIREMENT--use-subject-path-slash-only-for-bearer-qualification.md`; SHA-256 `a6da5282044bff900a9d2826f6c14a37f405da40c915896ceef73fef666e2d34`.
- `CA-R-1245@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1245-CORE_META_MODEL-REQUIREMENT--qualify-allowed-values-with-colon.md`; SHA-256 `ac3823579333397d267b15c8fc5671cf3518e101096ef231165cc70aac44e9f2`.
- `CA-M-228@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md`; SHA-256 `1c83ca0d007ce7c4c2d624e46fc6f270a5ac7dfd992687c2f0dc7e508016d80d`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the explicit Operator decision: drop Natural Rendering **and** archive the proposal. the dependent-draft disposition is supported at confidence **>=99%** by the authority comparison below.

the natural-phrase conversion fixtures test the rejected notation **and** are withdrawn. the useful bearer, allowed-value, unresolved-target, **and** ambiguous-target checks remain under CA-E-383 **and** CA-E-246. the obsolete examples, including `Content Role/Requirement`, are preserved **only** as historical proposal content, **not** accepted as valid fixtures. no executed test result is claimed.

- CA-M-002 (DRY) **and** CA-M-005 favor reusing the surviving rules **without** maintaining an additional presentation system.
- CA-M-006 favors retiring dependent rules that would reintroduce the rejected concept.
- CA-R-1490 is satisfied by the exact archived bytes, including the original Version **and** timestamp. no proposal receives an Atom ID **or** promotion.
- the direct incoming filename-reference check found **only** this Question; its Carrier locator now addresses the archive. historical evidence remains unchanged.

## Surviving authority checked for this disposition

- `CA-R-1204@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1204-CORE_META_MODEL-REQUIREMENT--use-subject-path-slash-only-for-bearer-qualification.md`; SHA-256 `a6da5282044bff900a9d2826f6c14a37f405da40c915896ceef73fef666e2d34`.
- `CA-R-1245@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1245-CORE_META_MODEL-REQUIREMENT--qualify-allowed-values-with-colon.md`; SHA-256 `ac3823579333397d267b15c8fc5671cf3518e101096ef231165cc70aac44e9f2`.
- `CA-E-383@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION--reject-invalid-subject-expressions.md`; SHA-256 `0f44dcff6ce349e401c14d2c799f8f5644de141d699994c38d33c16f3d2525ba`.
- `CA-E-246@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-246-CORE_META_MODEL-QA_CASE--validate-atom-subjects.md`; SHA-256 `048619289f08b8fcca6d0494ba47b629de90ca8f741cf76a6ad65e8df9e37a55`.
