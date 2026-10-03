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
# How should the Dependent-entity criteria draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived proposal Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--govern-dependent-entity-criteria-through-the-dependent-entity@2.md`.
- inspected SHA-256: `1ad5f8626d39d28bc53d613fd6e1176b2072709e4c8d99c5dbdc8e2b2d5f9995`.
- review point: 9 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Consolidate** — Preserve the narrowest governed target rule in Subject assignment; avoid a parallel subject-selection rule.
>
> Basis: `CA-M-125`, `CA-R-1203`; I2. Reviewer confidence: 96%.

## Active authority cited by the review

- `CA-M-125@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-125-CORE_META_MODEL-METHOD--assign-subjects-from-the-claim.md`; SHA-256 `e68c04a597b150c1070698afc897cc9d38c5f84f0c78f052e138e50b5f5e4ccc`.
- `CA-R-1203@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1203-CORE_META_MODEL-CORE-REQUIREMENT--split-at-multiple-governed-subject-boundaries.md`; SHA-256 `1d525c4eabdf44b89f5a77fc92e77bfbf373373f3c7999ad67bbbc22303c5119`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved at confidence **>=99%** under the Operator decision: a Subject is a GOVERNS **or** DEPENDS_ON Relation between an Atom **and** an Entity; Actions **and** Workflows are Operations Atoms **and** therefore Entities. the Operator authorized group-2 repair **and** promotion.

entry and exit criteria reuse the same narrowest-target assignment. the specific dependent-Entity case is retained in CA-M-125 and CA-E-246; no separate selection policy or ungoverned criterion Entity is introduced.

- surviving active authority: CA-M-125, CA-R-1203, CA-E-246.
- CA-M-002 (DRY), CA-M-005 (necessary complexity), **and** CA-M-006 (coherence) favor the existing target identities **and** one assignment policy.
- CA-R-1490 (valuable information) is satisfied by the exact archived proposal bytes **and** retained useful constraints; CA-E-001 is supported by the revised CA-E-246 fixtures.
- the incoming filename-reference scan found **only** this Question; its locator now addresses the archive. unrelated drafts **and** historical review evidence are unchanged.
- this duplicate is consolidated into active authority, **not** promoted as a second independently maintained Atom.
