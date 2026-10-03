---
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 5
updated_at: "2026-09-22 17:30:37 +0000"
relations: {}
---
# How should the Natural rendering draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--define-natural-rendering-of-a-qualified-subject-expression@1.md`.
- inspected SHA-256: `224d814353bac52deecbdade70ae467185ab3f16b94a9de082d26991a99e0190`.
- review point: 4 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise** — Useful interaction rule; allow natural prose when uniquely resolved, with canonical identity preserved.
>
> Basis: `CA-R-1321`, `CA-M-228`; I4. Reviewer confidence: 96%.

## Active authority cited by the review

- `CA-R-1321@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE-REQUIREMENT--define-subject-expression.md`; SHA-256 `e9ee1b5918295cb6b979e36ba64a304fccb91d6cfce20c5fd54b7e4746aad44f`.
- `CA-M-228@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md`; SHA-256 `1c83ca0d007ce7c4c2d624e46fc6f270a5ac7dfd992687c2f0dc7e508016d80d`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved following the explicit Operator decision: drop Natural Rendering **and** archive the proposal. the dependent-draft disposition is supported at confidence **>=99%** by the authority comparison below.

the Operator explicitly rejected the additional Natural Rendering concept. canonical target identity remains under CA-R-1321 **and** CA-M-228; understandable wording remains under CA-M-301. no separate separator-free notation **or** fixed component-order requirement is retained.

- CA-M-002 (DRY) **and** CA-M-005 favor reusing the surviving rules **without** maintaining an additional presentation system.
- CA-M-006 favors retiring dependent rules that would reintroduce the rejected concept.
- CA-R-1490 is satisfied by the exact archived bytes, including the original Version **and** timestamp. no proposal receives an Atom ID **or** promotion.
- the direct incoming filename-reference check found **only** this Question; its Carrier locator now addresses the archive. historical evidence remains unchanged.

## Surviving authority checked for this disposition

- `CA-R-1321@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1321-CORE_META_MODEL-CORE-REQUIREMENT--define-subject-expression.md`; SHA-256 `e9ee1b5918295cb6b979e36ba64a304fccb91d6cfce20c5fd54b7e4746aad44f`.
- `CA-M-228@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md`; SHA-256 `1c83ca0d007ce7c4c2d624e46fc6f270a5ac7dfd992687c2f0dc7e508016d80d`.
- `CA-M-301@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand.md`; SHA-256 `4738745a26c982c352ab2ffd051fa7d02b211482c910f0e8f99b11d17de86868`.
