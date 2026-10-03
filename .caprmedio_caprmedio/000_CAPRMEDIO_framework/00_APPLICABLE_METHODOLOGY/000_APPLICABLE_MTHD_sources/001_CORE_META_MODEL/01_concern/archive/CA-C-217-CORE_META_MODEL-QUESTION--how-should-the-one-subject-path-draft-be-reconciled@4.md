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
# How should the One Subject Path draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- archived proposal Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-CORE-REQUIREMENT--give-every-subject-one-subject-path@2.md`.
- inspected SHA-256: `14aeebee87493660d696f8ce89a7e733c2649b0db549999cc7cd1227f1e1d524`.
- review point: 8 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Retire** — Subject is now a direct Relation; canonical target resolution supplies the needed uniqueness.
>
> Basis: `CA-R-1275`, `CA-R-1202`; I1. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-R-1275@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL-CORE-REQUIREMENT--define-subject.md`; SHA-256 `a50169ea2b888f746e5df44f5bbe72722ecad5343bc0b524bbaabc21a739978a`.
- `CA-R-1202@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once.md`; SHA-256 `828cff8ec4e119f8a5c78c63db889e481bfe78e887af9f34821754c80645804f`.

## Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

resolved at confidence **>=99%** under the Operator decision: a Subject is a GOVERNS **or** DEPENDS_ON Relation between an Atom **and** an Entity; Actions **and** Workflows are Operations Atoms **and** therefore Entities. the Operator authorized group-2 repair **and** promotion.

Subject is the typed Atom-to-Entity Relation, not an intermediate object with its own Property. one resolved Entity per direct reference and its path encoding are already governed; no second Subject-object model is admitted.

- surviving active authority: CA-R-1275, CA-R-1202, CA-D-269.
- CA-M-002 (DRY), CA-M-005 (necessary complexity), **and** CA-M-006 (coherence) favor the existing target identities **and** one assignment policy.
- CA-R-1490 (valuable information) is satisfied by the exact archived proposal bytes **and** retained useful constraints; CA-E-001 is supported by the revised CA-E-246 fixtures.
- the incoming filename-reference scan found **only** this Question; its locator now addresses the archive. unrelated drafts **and** historical review evidence are unchanged.
- this duplicate is consolidated into active authority, **not** promoted as a second independently maintained Atom.
