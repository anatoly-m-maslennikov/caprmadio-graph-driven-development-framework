---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Project/information necessity assessment"
  depends_on:
    - "Atom/Content Role"
    - "Process"
    - "Action"
    - "Confidence Threshold"
    - "Atom/Claim"
priority: medium
version: 1
updated_at: "2026-09-17 16:59:22 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should progressive context acquisition separate flow from criteria?

which gap-free separation preserves REQU-035's progressive context-acquisition behavior, information-necessity criterion, **and** confidence interpretation **without** repeating them across Requirements, Methods, **and** Operations?

## Evidence

REQU-035 prescribes reading active Principles, using indexes, Relations, **and** Subjects for discovery, checking full applicable Claims, **and** expanding inspection for dependencies, conflicts, missing evidence, **or** uncertainty. it also prohibits substituting indexes for Claims **and** loading every ancestor's content merely because of structural placement. its second paragraph defines necessary information through the effective Confidence Threshold **and** distinguishes that heuristic from comparable probabilities. GOV-REQU-375 currently depends on this authority through its parent link.

## Principle check

CA-M-003 requires sufficient context while keeping omitted information recoverable. CA-M-002 **and** CA-M-005 reject a duplicate retrieval algorithm **or** unjustified Action nodes; CA-M-006 requires the M/O boundary under R-1282 **and** R-1344. CA-R-1490 requires retaining the no-blanket-ancestry-read guard **and** confidence qualification. C-141 already records the related general derivation-versus-execution boundary, but it does **not** settle this complete context-acquisition split.

## Disposition

preserve the source. map the execution flow **and** its reused Actions separately from selection **and** adequacy criteria, retaining the M-271 threshold resolver **without** copying it. rebind GOV-REQU-375 **only** **after** that map establishes its true parent. do **not** turn the paragraph into invented Process nodes **or** discard its second Claim **to** force one-Claim conformance.

## Inspected source Revisions

- `CAPRMEDIO-REQU-035` Version **14**: `.caprmedio_caprmedio/04_requirement/CAPRMEDIO-REQU-035-CORE-REQUIREMENT--identify-necessary-information-by-confidence.md`; SHA-256 `89022a24bc11fefa4b891c87bf0620211dd284b89ad73b946d3d93687f53fc38`.
- `CAPRMEDIO-GOV-REQU-375` Version **18**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-375-CORE_META_MODEL-GENERAL-REQUIREMENT--configure-necessary-information-confidence-threshold.md`; SHA-256 `304c8a67684d3dac4e97a9c90f08065a6ba71d9029e38529d3cfcff7a0bb291f`.
- `CA-M-003` Version **12**: `.caprmedio_caprmedio/05_method/CA-M-003-CORE-METHOD--show-what-is-needed-keep-the-rest.md`; SHA-256 `598b2d1727642493b479dbbc62015d6ebf940951328e5e216190afd41f7b2b6e`.
- `CA-M-271` Version **3**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-271-CORE_META_MODEL-METHOD--resolve-confidence-thresholds-by-source-precedence.md`; SHA-256 `1e873d4a4a2fbb22c51a5047efd72948fb3c68b62869baa7216d75a27612113b`.
- `CA-R-1344` Version **9**: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `585952b47af26e45181a2d144380d491eb3282729ebbd03b099d20aa9132bf22`.
- `CA-C-141` Version **3**: `.caprmedio_caprmedio/01_concern/CA-C-141-QUESTION--which-derivation-rules-are-methods-rather-than-actions.md`; SHA-256 `b78dc7d6c21d85401877d88b2942cee0765b6e726d6814a14a8e1be3f7129fc8`.
