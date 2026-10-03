---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Relation Kind"
  depends_on:
    - "CAPRMEDIO Graph"
    - "Artifact"
    - "Scope Unit"
    - "Atom/Subjects"
    - "Carrier"
priority: medium
version: 1
updated_at: "2026-09-17 19:57:02 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which schemas govern generic Artifact selectors and Relation patches?

which admitted selector **and** Relation schemas replace the legacy generic Artifact fields **without** losing target precision **or** transferring Atom operation semantics **to** generic helpers?

## Evidence

R-1131 names `relational_endpoints`, relative Scope Unit references, endpoint classes, direction, lifecycle, cardinality, **and** Content Role applicability under one generic project-graph reference. R-1246/R-806 require graph-qualified Relation Kind identity **and** admitted endpoint contexts; equal names **or** compatible classes do **not** identify the same Relation Kind. no exact replacement for the legacy endpoint descriptor was established by this review.

R-1135 mixes structural scope, layer, tier, Feature, Content Role, subject scope, lifecycle state, **and** typed relations. a layer **or** Feature Label is **not** an additional structural parent axis; Current Scope Unit, Claim Scope Unit, **and** Subject targets are **not** interchangeable. R-1067 requires common selectors but leaves operation semantics with the canonical Atom Tool. C-111/C-117/C-125 retain unresolved Subject, structural declaration, **and** legacy scope mappings.

## Principle check

DRY favors one schema owner per fact **and** reusable mechanics. coherence requires graph-qualified relations **and** unambiguous filters. information preservation protects existing target distinctions **and** diagnostics rather than replacing several fields with one guessed alias.

## Disposition

preserve exact selector **and** endpoint requirements until their mapping **to** admitted schemas is established. then bind generic mechanics **to** that schema while retaining ATOM_SEARCH, ATOM_UPDATE, **and** REBIND_ATOM_RELATIONS semantic ownership. do **not** add Scope Unit dependency edges, infer relative names, collapse Claim targets into carrier ownership, widen mutation permission, **or** implement new query behavior during this repair.

## Inspected source Revisions

- `CA-R-1067@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1067-TOOLS-REQUIREMENT--accept-common-atom-target-selectors.md`; SHA-256 `88c087f12daf0d9c47d5cb97d243231b01489658379466a113e6630f0a0082f3`.
- `CA-R-1131@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1131-TOOLS-REQUIREMENT--patch-artifact-relations.md`; SHA-256 `5e1c49c3c61b1d1d64023c674aa3bd40e945f657d236b33659ef585c6531305a`.
- `CA-R-1135@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1135-TOOLS-REQUIREMENT--query-artifacts-by-filters.md`; SHA-256 `27e17b9774d9d32aa2704ca5ade8afa34db90aab6237dcba34894af75cc06cf9`.
- `CA-R-1246@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1246-CORE_META_MODEL-CORE-REQUIREMENT--keep-relation-vocabularies-graph-specific.md`; SHA-256 `63530dea52c225a6145843c252d01432d0928d27e5b1ae68504a0151e379cb56`.
- `CA-R-806@18`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata.md`; SHA-256 `90d4dfd9ecee45ec0d2e6c1f358a233beb624a47867942167cd9603000af325b`.
- `CA-C-111@2`: `.caprmedio_caprmedio/01_concern/CA-C-111-QUESTION--which-canonical-targets-do-the-legacy-subject-labels-identify.md`; SHA-256 `f276fee27794509dbda2293168ed43e7ef829f03c588f6ce929d95c5bcb39208`.
- `CA-C-117@1`: `.caprmedio_caprmedio/01_concern/CA-C-117-QUESTION--which-declarations-complete-the-authoritative-project-structure.md`; SHA-256 `18c58f8ab5fb4afaffe39137e0e0a54006d68bd45993b09d714e1cefea2a7846`.
- `CA-C-125@2`: `.caprmedio_caprmedio/01_concern/CA-C-125-QUESTION--which-legacy-scope-properties-should-be-retired-or-rebound.md`; SHA-256 `3b7f0d887bc023de9a938665ce0173b9b531fb0e2363e57c769c7a3b2140028a`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
