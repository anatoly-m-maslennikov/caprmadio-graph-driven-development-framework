---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Project Configuration"
  depends_on:
    - "Framework Instance Settings"
    - "Applicable Methodology/Sources"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 18:04:39 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Goal preserves Project Configuration without duplicating Settings selections?

which current Goal should replace CA-R-1176's instruction for PROJECT_CONFIGURATION **to** select Methodology Sources, **without** duplicating current Settings selections **or** losing its intended Project-specific expansion responsibility?

## Evidence

CA-R-1176 requires Project-owned Customizations **and** composition decisions that select CORE_META_MODEL **and** PROJECT_CONFIGURATION for compilation. CA-R-1207 instead assigns Project Configuration expansion rules, constraints, **and** defaults within Core permission; current Extension activation **and** selected revisions belong **to** Framework Instance Settings. CA-R-1228 already requires the Core, Project Configuration, **and** applicable installed Extension Sources. the Goal's selection wording does **not** distinguish a composition rule from a current selected value.

## Principle check

CA-M-002 prohibits independent duplicate selection authority; CA-M-006 requires coherent ownership; CA-R-1490 requires preservation of the Goal's useful intent. these rules settle that current selections cannot be independently owned here, but do **not** establish whether the Goal should be replaced by an expansion Goal **or** absorbed into existing Goal authority. changing its Summary also requires a new Atom identity under CA-R-1464.

## Disposition

preserve CA-R-1176 pending a lossless Goal replacement **or** deduplication decision. do **not** populate Settings, remove the Goal, fabricate a structural declaration, **or** interpret this Concern as permission **to** maintain a second selection source. the active R-1207 **and** R-1228 boundaries remain applicable.

## Inspected source Revisions

- `CA-R-1176@12`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/04_requirement/CA-R-1176-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-PROJECT_CONFIGURATION--select-core-meta-model-and-project-configuration-for-compilation.md`; SHA-256 `3323c09dea331719b57ebfbf2cbe7dcb64239973fbbd45420116bca9ae3a8469`.
- `CA-R-1207@11`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1207-CORE_META_MODEL-CORE-REQUIREMENT--separate-project-configuration-rules-from-current-settings.md`; SHA-256 `39bc32faff60c2d7f18982eea2e00a855892d9b04efdfbbd1f96c055a9cbd700`.
- `CA-R-1228@13`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1228-CORE_META_MODEL-GENERAL-REQUIREMENT--include-all-applicable-methodology-sources.md`; SHA-256 `aff98878a08d052159bdcf288eb1821ed15ef7b78e5184e7b992bfe64b7caffb`.
- `CA-R-1464@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity.md`; SHA-256 `4f4e2f8528afe32b916a73df97f7652201d258a570faeb76fc43452c9fa0da44`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
