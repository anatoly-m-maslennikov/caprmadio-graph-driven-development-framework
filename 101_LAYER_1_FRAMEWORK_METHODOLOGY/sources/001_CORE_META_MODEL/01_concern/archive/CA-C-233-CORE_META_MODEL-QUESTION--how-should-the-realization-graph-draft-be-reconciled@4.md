---
atom_id: CA-C-233
content_role: Concern
type: Question
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
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
version: 4
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-269", "CA-D-270", "CA-D-478", "CA-D-479", "CA-D-482", "CA-D-483", "CA-E-001", "CA-M-002", "CA-M-005", "CA-M-006", "CA-R-1270", "CA-R-1464", "CA-R-1470", "CA-R-1490", "CA-R-1493", "CA-R-1494", "CA-R-1598", "CA-R-918", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

How should the Realization Graph draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Historical Draft under review

- Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-REQUIREMENT--define-realization-graph@5.md`.
- inspected SHA-256: `ad1673ecb4f7aab4b4524c7a0b7f0a9e9bf9877ffe8cf284898d64ad570b16d8`.
- review point: 24 of 79; campaign `draft-review-8afeac79`.

### Historical review finding

> **Revise** — Keep exact frontier provenance; clarify legacy “Implementation-role Projection” as an I-contribution output. No Atom status is asserted by this draft.
>
> Basis: `CA-R-1568`, `CAPRMEDIO-META-REQU-657`; I5. Reviewer confidence: 96%.

### Active authority cited by the review

- `CA-R-1568@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1568-CORE_META_MODEL-GENERAL-REQUIREMENT--permit-projections-as-implementation-outputs.md`; SHA-256 `38b3f987bc2891083e295667d573e1de791438e178f62db97f7e566b4d667afc`.
- `CAPRMEDIO-META-REQU-657@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-657-CORE_META_MODEL-CORE-REQUIREMENT--define-projection-artifact-form.md`; SHA-256 `c996dd4ef8fdf7a5c9e8fef82a2929c874015d6e4ffd9d8363ddb767027975ff`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the Operator-approved Draft repair, not for promotion **or** implementation. the specialized Realization Graph model belongs **in** PROJECT_CONFIGURATION; general Projection, representation, **and** acceptance boundaries remain **in** CORE_META_MODEL.

- Keep the reviewed Claim in Draft; normalize its carrier and align it to current Principles. Specialized Realization Graph authority belongs to PROJECT_CONFIGURATION.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-REQUIREMENT--define-realization-graph@5.md`; SHA-256 `5a03aa206da91202e8c61a05091681d96e3cb6fe1eea17f003b9e1e6fd654da9`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/drafts/CA-R--PROJECT_CONFIGURATION-REQUIREMENT--define-realization-graph.md`.
- Keep the reviewed Claim in Draft; normalize its carrier and align it to current Principles. Keep the general representation or acceptance boundary in CORE_META_MODEL.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--CORE_META_MODEL-REQUIREMENT--keep-reverse-engineered-rmed-provisional@1.md`; SHA-256 `c7bb490d6737644ea97e7c1f6e248112179c948a3857b94ce04f496246b40073`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/drafts/CA-R--CORE_META_MODEL-REQUIREMENT--keep-reverse-engineered-rmed-provisional.md`.
- Keep the reviewed Claim in Draft; normalize its carrier and align it to current Principles. Keep the general representation or acceptance boundary in CORE_META_MODEL.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--CORE_META_MODEL-REQUIREMENT--separate-legacy-observations-from-refactoring-decisions@1.md`; SHA-256 `8c1d89721e2c81dbd2c25fe6410fdb64988a6c36de71bd6ff1e3eaea97ac6c72`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/drafts/CA-R--CORE_META_MODEL-REQUIREMENT--separate-legacy-observations-from-refactoring-decisions.md`.
- Keep the reviewed Claim in Draft; normalize its carrier and align it to current Principles. Specialized Realization Graph authority belongs to PROJECT_CONFIGURATION.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/archive/CA-R--GOVERN-REQUIREMENT--register-realization-graph-projection-type@4.md`; SHA-256 `db60575768e5f1a0feb409a77bb646658f8cc52cd68d5b9c8e7dc828d551f669`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/drafts/CA-R--PROJECT_CONFIGURATION-REQUIREMENT--register-realization-graph-projection-type.md`.
- Consolidate into CAPRMEDIO-META-REQU-657 and CAPRMEDIO-META-REQU-097: Projections are non-authoritative and evidence must support a separately identified Claim. Keep the specialized permission boundary in the pre-runtime-pass Draft; reverse-engineering use remains permitted.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--SEMNTC-REQUIREMENT--use-realization-graphs-only-as-evaluation-evidence@5.md`; SHA-256 `7aa711b5c8be1b23b97711e926991a2d6bb552f81f7f332e7951c8c581755be9`.

DRY supports consolidation; necessary complexity rejects an unsupported universal view pair; coherence requires current target carriers; preservation keeps exact history; checkability separates derivation evidence from correctness. no runtime graph, Tool, Projection output, Settings, installed package, **or** unrelated Draft is changed.
