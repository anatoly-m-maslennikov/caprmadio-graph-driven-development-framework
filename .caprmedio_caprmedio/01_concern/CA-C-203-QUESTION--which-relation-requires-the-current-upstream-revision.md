---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Relation"
  depends_on:
    - "Artifact/Revision"
    - "Journal"
    - "Evaluation"
priority: medium
version: 1
updated_at: "2026-09-17 21:51:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Relation requires the current upstream Revision?

which registered Relation **and** effect precondition make E-188's old upstream Revision invalid, as distinct from historical provenance **or** a valid observation of nonconforming state?

## Evidence and Principle check

E-188 prohibits both sealing **and** applying a Relation whose upstream target Revision is **not** current. R-804 requires read-only context **to** preserve observed invalid state **and** separates that capture from mutation preconditions. GOV-REQU-767 restricts Active RMED-to-RMED target Status; it does **not** by itself establish that **every** versioned reference **must** name the latest Revision. R-1491 preserves intact historical observations rather than rebinding them **to** current state.

coherence requires these observation, Status **and** effect-precondition rules **to** remain distinct. DRY favors the registered Relation authority, **not** a test-created universal constraint. information preservation prohibits dropping a stale observation **or** silently rewriting its reference.

## Disposition

preserve E-188 while identifying its graph-qualified Relation, current-Revision requirement **and** exact diagnostic. a correction **must** allow provisional observation of invalid state **without** granting effect permission, **and** **must** preserve historical references **where** admitted. do **not** certify this fixture, make **all** provenance references current-only, **or** weaken an actual mutation precondition merely **to** resolve the wording.

## Inspected source Revisions

- `CA-E-188@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-188-TOOLS-QA_CASE--reject-non-current-upstream-version.md`; SHA-256 `51380f837c5404c8c899fe7e1e441e3511b3d6ff3609658c5a3d9fca3e60006d`.
- `CA-R-804@20`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/COMMIT_CONTEXT/04_requirement/CA-R-804-COMMIT_CONTEXT-REQUIREMENT--gather-provisional-programmatic-action-context-concurrently.md`; SHA-256 `a048c3d5ce9e68d67164cca92f035cb38ded4a94d6494a0bdf7d88273648c130`.
- `CAPRMEDIO-GOV-REQU-767@15`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-767-CORE_META_MODEL-CORE-REQUIREMENT--keep-rmed-to-rmed-relations-within-active-authority.md`; SHA-256 `01c9614a5ef8a444d4d2bdc072f39804c31d5777d2944d60996e4703d5e5f314`.
- `CA-R-1491@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1491-CORE_META_MODEL-CORE-REQUIREMENT--keep-project-validation-out-of-journal-admission.md`; SHA-256 `8c8b7fcbe12d2ebc1e02e26229f528a5539953f88261d411a5950d7f84e97052`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
