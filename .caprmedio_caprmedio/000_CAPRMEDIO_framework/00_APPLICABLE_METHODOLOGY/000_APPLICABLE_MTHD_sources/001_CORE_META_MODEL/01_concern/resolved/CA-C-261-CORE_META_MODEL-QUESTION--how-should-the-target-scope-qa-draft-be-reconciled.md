---
atom_id: CA-C-261
content_role: Concern
type: Question
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: resolved
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom"
  depends_on:
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Operator"
    - "Project"
priority: medium
version: 5
updated_at: "2026-09-23 21:34:42 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-269", "CA-D-270", "CA-D-478", "CA-D-479", "CA-D-482", "CA-D-483", "CA-E-001", "CA-M-002", "CA-M-005", "CA-M-006", "CA-R-1270", "CA-R-1464", "CA-R-1470", "CA-R-1490", "CA-R-1493", "CA-R-1494", "CA-R-1598", "CA-R-918", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

How should the Target-scope QA draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Historical Draft under review

- Draft Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--CORE_META_MODEL-QA_CASE--validate-target-scope-unit-and-textual-claim-scope@2.md`.
- prior Draft inspected SHA-256: `73fb0f9da8b454192894c886ce0cf18e3a479196ba539033f58b52679d40ccfc`.
- review point: 52 of 79; campaign `draft-review-8afeac79`.

### Historical review finding

> **Revise** — Preserve useful ownership tests while separating Claim Scope restrictions from structural-target cardinality.
>
> Basis: `CA-R-919`, `CA-R-1446`, `CA-E-240`; I1. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-R-919@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-919-CORE_META_MODEL-CORE-REQUIREMENT--give-every-claim-one-structural-entity.md`; SHA-256 `11a17807a5bfd7fb871233ebe9801dd53f5e6a4c63808d0f8e7c603e878328ee`.
- `CA-R-1446@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1446-CORE_META_MODEL-CORE-REQUIREMENT--define-claim-structural-entity.md`; SHA-256 `01ede2ab34ecdaac39d9d3a62b37e9b66a4590bfa081332f247b47ce082d2f1f`.
- `CA-E-240@23`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-240-CORE_META_MODEL-QA_CASE--validate-atom-scope-and-claim-scope.md`; SHA-256 `1c36e58b64b53e275b85513ff9d7a6a559b5494ab650475d24843b88b7cdc102`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the Operator-approved Draft repair, not for promotion **or** implementation. the specialized Realization Graph model belongs **in** PROJECT_CONFIGURATION; general Projection, representation, **and** acceptance boundaries remain **in** CORE_META_MODEL.

- Preserve the semantic target/textual-applicability test; reject omitted carried targets and replace retired CA-D-476 with CA-D-482.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--CORE_META_MODEL-QA_CASE--validate-target-scope-unit-and-textual-claim-scope@2.md`; SHA-256 `ac192e42b5c50210f728331cf0ae80afd195f2e31d53c4dc3ac20be5f65f4d94`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/drafts/CA-E--CORE_META_MODEL-QA_CASE--validate-target-scope-unit-and-textual-claim-scope.md`.

DRY supports consolidation; necessary complexity rejects an unsupported universal view pair; coherence requires current target carriers; preservation keeps exact history; checkability separates derivation evidence from correctness. no runtime graph, Tool, Projection output, Settings, installed package, **or** unrelated Draft is changed.
