---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Projection"
  depends_on:
    - "Atom/Content Role"
    - "Entity/Type"
    - "Project Structure"
    - "Artifact/Revision"
priority: medium
version: 1
updated_at: "2026-09-17 19:50:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which canonical Type identity does the active Atom snapshot count?

which canonical Type identity is counted by the current active Atom snapshot **without** conflating differently qualified Type values **or** inventing another Type Property?

## Evidence

R-1060 requires counts by canonical Type, Structural Level, **and** Structural Unit. M-147 **and** E-070 require one complete zero-inclusive rollup for **every** dimension, with no omissions **or** double counting, but do **not** establish whether the Type key includes its applicable Content Role qualification. R-1284 defines one single-valued Type Property; R-1349 requires qualified Type Subjects of one Entity occurrence **to** identify that same slot. these rules do **not** select a display key **or** an exact registry schema for this Projection.

M-147/E-070 also assume lifecycle placement as the sole activity source, concrete output fields, a stored frontier, **and** an atomic rebuild/recording flow. retain those conditions for their separate Carrier **and** workflow reconciliation rather than claiming that a renamed count column fixes the whole family.

## Principle check

coherence requires distinct governed meanings **to** remain distinguishable. DRY rejects a second independently maintained Type registry. information preservation protects every admitted Type, zero counts, grand-total reconciliation, malformed-input rejection, **and** deterministic currentness evidence.

## Disposition

preserve the snapshot family while identifying the exact canonical Type key **and** admitted source registry. do **not** equate equal labels across Content Roles **or** introduce multiple simultaneous Types on one Atom. separate output Carrier **and** rebuilding behavior only with a lossless map; C-117 retains the structural authority migration **and** C-177 retains provenance ownership. no snapshot is rebuilt **or** certified current by this Concern.

## Inspected source Revisions

- `CA-R-1060@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1060-TOOLS-REQUIREMENT--generate-current-active-atom-snapshot.md`; SHA-256 `a79f18cb419fc5d9ebe917b90a54b39fc98c11f5504d13f474f09eee335ce711`.
- `CA-M-147@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/05_method/CA-M-147-TOOLS-CORE-METHOD--generate-current-active-atom-snapshot.md`; SHA-256 `0de31bd5a12862cbd8d2381f363c5f245934465866255ae514f72f16de392ada`.
- `CA-E-070@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-070-TOOLS-QA_CASE--current-active-atom-snapshot-correctness.md`; SHA-256 `2a34036838f2c787ae18d67b8f435e1642ba8f5a6b0c6190989a04fe835b99f2`.
- `CA-R-1284@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1284-CORE_META_MODEL-CORE-REQUIREMENT--define-type.md`; SHA-256 `3588c90de4d71b71549801d1a6b695e418a1da97f38aa7875f0f7b7c7e1a98d8`.
- `CA-R-1285@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1285-CORE_META_MODEL-CORE-REQUIREMENT--give-every-borne-type-property-one-value.md`; SHA-256 `a25ac490b25f54bacb2568798c9918395f198a621000c942872151a3b7b09a6b`.
- `CA-R-1349@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1349-CORE_META_MODEL-CORE-REQUIREMENT--identify-one-type-property-slot.md`; SHA-256 `febe00e4ebe1a95063e8118fe53a2c1c81cd3f6d33c09d13b15f5260cf2f3338`.
- `CA-C-117@1`: `.caprmedio_caprmedio/01_concern/CA-C-117-QUESTION--which-declarations-complete-the-authoritative-project-structure.md`; SHA-256 `18c58f8ab5fb4afaffe39137e0e0a54006d68bd45993b09d714e1cefea2a7846`.
- `CA-C-177@1`: `.caprmedio_caprmedio/01_concern/CA-C-177-QUESTION--what-source-frontier-information-must-methodology-projections-preserve.md`; SHA-256 `85b21f9021e15fdd20e65dd3896229c4bc25dfe66e55d6f3ffffa1ed1df59ca1`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
