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
updated_at: "2026-09-22 17:13:29 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the Natural rendering draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/drafts/CA-R--MMODEL-CORE-REQUIREMENT--define-natural-rendering-of-a-qualified-subject-expression.md`.
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

awaiting the Operator choice; repair confidence remains below 99%. the source remains unchanged **in** Draft.

CA-R-940 **and** CA-M-301 already require readable, understandable Claims; CA-R-1321 **and** CA-M-228 preserve exact qualified references. DRY **and** CA-M-005 favor reusing these rules rather than introducing a separate presentation concept. however, this draft requires a separator-free phrase with the same named components **in** the same order. that can describe a new constrained notation, **not** ordinary prose; removing that restriction would change the proposed facility.

recommended disposition: use ordinary readable wording that unambiguously preserves the canonical meaning; keep canonical paths **where** registered reference syntax is required. retire the unnecessary Natural Rendering definition **and** reconcile its dependent drafts **without** promoting them. alternative: retain a separate constrained notation **and** specify its intended use **and** exact resolution rules. the Principles support the simpler recommendation, but do **not** establish that the separate notation has no intended use.
