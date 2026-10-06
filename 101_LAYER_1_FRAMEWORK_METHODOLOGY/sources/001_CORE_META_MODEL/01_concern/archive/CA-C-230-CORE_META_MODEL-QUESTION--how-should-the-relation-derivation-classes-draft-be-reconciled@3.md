---
atom_id: CA-C-230
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
version: 3
updated_at: "2026-09-23 20:47:56 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-D-269", "CA-D-270", "CA-D-478", "CA-D-479", "CA-D-482", "CA-D-483", "CA-E-001", "CA-M-002", "CA-M-005", "CA-M-006", "CA-R-1270", "CA-R-1464", "CA-R-1470", "CA-R-1490", "CA-R-1493", "CA-R-1494", "CA-R-1598", "CA-R-918", "CAPRMEDIO-META-REQU-097", "CAPRMEDIO-META-REQU-657"]}
---
# Summary

How should the Relation derivation classes draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Historical Draft under review

- Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-REQUIREMENT--classify-each-realization-graph-relation-by-derivation@4.md`.
- inspected SHA-256: `0268b90c88c3a1c84c223ab386a23be710fb4c762d565bb329bc2c70bd005eac`.
- review point: 21 of 79; campaign `draft-review-8afeac79`.

### Historical review finding

> **Revise** — Keep multiple provenance classifications, but require per-class evidence and claim/frontier bindings.
>
> Basis: `CAPRMEDIO-META-REQU-657`; I5. Reviewer confidence: 97%.

### Active authority cited by the review

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
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/archive/CA-R--MMODEL-REQUIREMENT--classify-each-realization-graph-relation-by-derivation@4.md`; SHA-256 `0268b90c88c3a1c84c223ab386a23be710fb4c762d565bb329bc2c70bd005eac`.
- current repaired Draft: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/drafts/CA-R--PROJECT_CONFIGURATION-REQUIREMENT--classify-each-realization-graph-relation-by-derivation.md`.

DRY supports consolidation; necessary complexity rejects an unsupported universal view pair; coherence requires current target carriers; preservation keeps exact history; checkability separates derivation evidence from correctness. no runtime graph, Tool, Projection output, Settings, installed package, **or** unrelated Draft is changed.
