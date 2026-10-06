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
updated_at: "2026-09-23 16:51:13 +0000"
relations: {"relates_to": ["CA-M-123"]}
---
# Summary

How should the Write DoD draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/archive/CA-M--SEMNTC-CORE-METHOD--write-definitions-of-done@2.md`.
- inspected SHA-256: `26cb2df56f3323b68d6c6be27d2b18a4c4057d2dae9e1326e6b41fc60987d990`.
- review point: 47 of 79; campaign `draft-review-8afeac79`.

### Prior review finding

> **Retire** — Task-only formula is obsolete: the active Method says Plan; file-backed Plans require DoD.
>
> Basis: `CA-M-123`, `CA-R-1581`, `CA-D-470`; I2,I6. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-M-123@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done.md`; SHA-256 `cac093e9d046f1fa60208a0f5705d63e43be8cee16980d71a4c184f461af2b27`.
- `CA-R-1581@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1581-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-definition-of-done.md`; SHA-256 `d293bcc3815161e6487ba5a1c0a87398066cfc715c7a752ab1d629d07b50e53f`.
- `CA-D-470@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections.md`; SHA-256 `b02d06896515fb412b44abd20986a5d4ca306521586ac62af5625f5bcad35e00`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved: the Operator approved archiving this duplicate Draft. CA-M-123 remains the active authoring authority; no new DoD Atom is promoted.

- CA-M-123 preserves **all** four useful constraints: the falsifying expression, observable **and** decidable conditions, explicit composite/function parentheses, **and** CA-M-122 evaluation rules.
- the current expression names Plan, **not** a separate Task-only model. CA-R-1581 defines DoD; CA-R-1599 requires it for **every** Plan, **and** CA-D-470 carries it **in** the mandatory Markdown file, including Hubs.
- the old conditional wording about file-backed Plans is historical; all current Plans require their own file **and** DoD. DRY **and** necessity favor the existing authority instead of another copy.

- exact prior Draft preserved at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/archive/CA-M--SEMNTC-CORE-METHOD--write-definitions-of-done@2.md`; SHA-256 `26cb2df56f3323b68d6c6be27d2b18a4c4057d2dae9e1326e6b41fc60987d990`. the previous review evidence **in** this Question remains historical.

#### Current authority checked

- `CA-R-1599@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1599-CORE_META_MODEL-GENERAL-REQUIREMENT--require-a-definition-of-done-for-every-plan.md`; SHA-256 `6d26e675f9e15601622342bcad623c9d9f656f6e13561d476f3b6095a4639543`.
- `CA-D-470@3`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections.md`; SHA-256 `c1fe523ba1550091418a86d8f2ccbd2a7602152861169801d7146ef2cf4a410f`.
- `CA-M-123@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-123-CORE_META_MODEL-METHOD--write-definitions-of-done.md`; SHA-256 `cac093e9d046f1fa60208a0f5705d63e43be8cee16980d71a4c184f461af2b27`.
- `CA-M-122@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-122-CORE_META_MODEL-METHOD--evaluate-condition-expressions.md`; SHA-256 `b78712742bf7f98e81202faea4863acc1367e8523ab2752822c95f096722841b`.
- `CA-R-1581@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1581-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-definition-of-done.md`; SHA-256 `d293bcc3815161e6487ba5a1c0a87398066cfc715c7a752ab1d629d07b50e53f`.
