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
updated_at: "2026-09-22 20:48:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the Semantic irreducibility draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--keep-each-atom-semantically-irreducible@2.md`.
- inspected SHA-256: `2421ea93f751286b69e1459ed3cd2d77fc3cbc3d8540bf6675c1e375cd657cdc`.
- review point: 10 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Retire** — Older acceptance-together wording is superseded by the independently replaceable Claim boundary.
>
> Basis: `CA-R-154`, `CA-R-918`; I2. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-154@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-154-CORE_META_MODEL-CORE-REQUIREMENT--keep-each-atom-semantically-irreducible.md`; SHA-256 `4c924f038fc509af31c5d06e328ce956c65115d8907c80924446651b2d83f7f0`.
- `CA-R-918@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-918-CORE_META_MODEL-CORE-REQUIREMENT--give-every-atom-one-claim.md`; SHA-256 `9d474f9b8f33a33d87149066e33a1926396186c0f3f6adb627b620a9179a408c`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved at confidence **>=99%**; the Operator approved archiving this duplicate Draft. no promotion occurred.

- CA-R-918 requires **`=1`** independently replaceable Claim per Atom.
- CA-R-154 limits authoritative content **to** what is necessary for that Claim.
- CA-R-1270 preserves a composite Claim **when** its components **must** be accepted, replaced, **and** retired together.

the earlier review finding was too broad: acceptance-together wording is **not** obsolete. it remains valid for composite Claims under CA-R-1270. the Draft is redundant because the active authority already preserves its useful rule.

- CA-M-002 (DRY) **and** CA-M-005 support reusing this authority rather than promoting a duplicate.
- CA-M-006 supports keeping the irreducibility **and** composite-Claim rules coherent.
- CA-R-1490 is satisfied by preserving the exact Draft bytes, including Version, timestamp, Subjects, **and** Claim, **in** the archive.
- CA-E-001 is satisfied by the explicit coverage above **and** the checked archive, source hashes, **and** incoming references.
- the incoming filename-reference scan found **only** this Question; its Carrier locator now points **to** the archive.

### Authority verified at resolution

- `CA-R-154@14`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-154-CORE_META_MODEL-CORE-REQUIREMENT--keep-each-atom-semantically-irreducible.md`; SHA-256 `4c924f038fc509af31c5d06e328ce956c65115d8907c80924446651b2d83f7f0`.
- `CA-R-918@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-918-CORE_META_MODEL-CORE-REQUIREMENT--give-every-atom-one-claim.md`; SHA-256 `9d474f9b8f33a33d87149066e33a1926396186c0f3f6adb627b620a9179a408c`.
- `CA-R-1270@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1270-CORE_META_MODEL-CORE-REQUIREMENT--permit-one-composite-claim-as-one-authority-unit.md`; SHA-256 `f95fea4bdf00c0fb17e05b87684e9fea6abf6f7b21d62cd965d78ee1b63af5b5`.
