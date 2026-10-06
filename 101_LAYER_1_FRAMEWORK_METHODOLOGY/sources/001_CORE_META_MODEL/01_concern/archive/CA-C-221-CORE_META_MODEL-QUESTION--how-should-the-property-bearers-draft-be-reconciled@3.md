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
updated_at: "2026-09-22 20:07:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the Property bearers draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived proposal Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--permit-properties-on-base-and-dependent-entities@2.md`.
- inspected SHA-256: `aab33bf8ef3f456f0738c66c63de4056d92f8b87ac0bc5fb4e701931b24a5045`.
- review point: 12 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Consolidate** — Property already is a Dependent Entity with one bearer Entity; add only a demonstrated missing constraint.
>
> Basis: `CA-R-1192`, `CA-R-1193`, `CA-R-1251`; I2. Reviewer confidence: 97%.

## Active authority cited by the review

- `CA-R-1192@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1192-CORE_META_MODEL-CORE-REQUIREMENT--define-dependent-entity.md`; SHA-256 `39a0dd677e1c1ac118def4e9101ff8741304bd4ec09d80a4da1aa15e9611a6e0`.
- `CA-R-1193@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1193-CORE_META_MODEL-CORE-REQUIREMENT--define-property.md`; SHA-256 `70ef20f6daf01bfeda9df182c4f094726600c87dbafd661c68a6f8320f506497`.
- `CA-R-1251@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1251-CORE_META_MODEL-CORE-REQUIREMENT--classify-property-as-a-dependent-entity.md`; SHA-256 `b26c95c2a3965ca60581f9de6eb663326832c18170e7decc738ad88c0aeacbac`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved at confidence **>=99%** under the Operator decision: a Subject is a GOVERNS **or** DEPENDS_ON Relation between an Atom **and** an Entity; Actions **and** Workflows are Operations Atoms **and** therefore Entities. the Operator authorized group-2 repair **and** promotion.

a Property already is a Dependent Entity whose identity requires one immediate bearer Entity. neither definition restricts that bearer to Primary Entities; the acceptance fixtures now explicitly cover Primary and Dependent bearers. Base Entity is not reintroduced.

- surviving active authority: CA-R-1192, CA-R-1193, CA-R-1251, CA-E-246.
- CA-M-002 (DRY), CA-M-005 (necessary complexity), **and** CA-M-006 (coherence) favor the existing target identities **and** one assignment policy.
- CA-R-1490 (valuable information) is satisfied by the exact archived proposal bytes **and** retained useful constraints; CA-E-001 is supported by the revised CA-E-246 fixtures.
- the incoming filename-reference scan found **only** this Question; its locator now addresses the archive. unrelated drafts **and** historical review evidence are unchanged.
- this duplicate is consolidated into active authority, **not** promoted as a second independently maintained Atom.
