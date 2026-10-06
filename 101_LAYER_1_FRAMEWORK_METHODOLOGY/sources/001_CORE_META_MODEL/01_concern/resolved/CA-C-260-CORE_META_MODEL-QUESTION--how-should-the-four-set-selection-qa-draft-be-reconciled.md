---
atom_id: CA-C-260
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

How should the Four-set selection QA draft be reconciled?

## Claim

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

### Historical Draft under review

- Draft Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--CORE_META_MODEL-QA_CASE--validate-ownership-and-target-scope-unit-selections@2.md`.
- prior Draft inspected SHA-256: `a3782b2471eb6695ddbee37169621382e2a790b2b84739a4d0994c359f9d6b40`.
- review point: 51 of 79; campaign `draft-review-8afeac79`.

### Historical review finding

> **Revise** — Keep cross-owner/incomplete-frontier cases; target Claim Structural Entity and add Plan-Hub invariance.
>
> Basis: `CA-M-273`, `CA-R-1448`, `CA-R-1449`; I1. Reviewer confidence: 99%.

### Active authority cited by the review

- `CA-M-273@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-273-CORE_META_MODEL-METHOD--derive-ownership-and-claim-target-atom-sets.md`; SHA-256 `7b4cb4512b5e4f8f63694c89dc3cd641b902e1c88dfd0374412cca66403f10c8`.
- `CA-R-1448@5`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1448-CORE_META_MODEL-GENERAL-REQUIREMENT--define-targeting-atoms.md`; SHA-256 `8742763eeced903bf47e2762ea1d164d46a161ac914a2b22ae82f3807a68a059`.
- `CA-R-1449@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1449-CORE_META_MODEL-GENERAL-REQUIREMENT--define-subtree-targeting-atoms.md`; SHA-256 `42c83e58102b052f2a6aef7e6655cebcf4fc651056b24ac316d7b2fb2b44b906`.

### Principles to apply

- [CA-M-002](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

### Resolution

resolved for the Operator-approved Draft repair, not for promotion **or** implementation. the specialized Realization Graph model belongs **in** PROJECT_CONFIGURATION; general Projection, representation, **and** acceptance boundaries remain **in** CORE_META_MODEL.

- Consolidate unique textual-applicability cases into active CA-E-460; keep its source fixture, exact sets, and missing-coverage checks. Discard the obsolete omitted-target behavior in favor of CA-D-482.
- exact prior Carrier: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/archive/CA-E--CORE_META_MODEL-QA_CASE--validate-ownership-and-target-scope-unit-selections@2.md`; SHA-256 `72cefdd48513d2341674b5bb8e1b2c5d55888a01e8f60d769dfa443709ee7503`.

DRY supports consolidation; necessary complexity rejects an unsupported universal view pair; coherence requires current target carriers; preservation keeps exact history; checkability separates derivation evidence from correctness. no runtime graph, Tool, Projection output, Settings, installed package, **or** unrelated Draft is changed.
