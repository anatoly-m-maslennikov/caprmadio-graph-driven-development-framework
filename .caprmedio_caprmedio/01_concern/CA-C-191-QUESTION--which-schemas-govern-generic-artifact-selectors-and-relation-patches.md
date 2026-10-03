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
version: 4
updated_at: "2026-09-17 22:44:37 +0000"
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

- `CA-R-1067@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1067-TOOLS-REQUIREMENT--accept-common-atom-target-selectors.md`; SHA-256 `88c087f12daf0d9c47d5cb97d243231b01489658379466a113e6630f0a0082f3`.
- `CA-R-1131@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1131-TOOLS-REQUIREMENT--patch-artifact-relations.md`; SHA-256 `5e1c49c3c61b1d1d64023c674aa3bd40e945f657d236b33659ef585c6531305a`.
- `CA-R-1135@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1135-TOOLS-REQUIREMENT--query-artifacts-by-filters.md`; SHA-256 `27e17b9774d9d32aa2704ca5ade8afa34db90aab6237dcba34894af75cc06cf9`.
- `CA-R-1246@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1246-CORE_META_MODEL-CORE-REQUIREMENT--keep-relation-vocabularies-graph-specific.md`; SHA-256 `63530dea52c225a6145843c252d01432d0928d27e5b1ae68504a0151e379cb56`.
- `CA-R-806@18`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata.md`; SHA-256 `90d4dfd9ecee45ec0d2e6c1f358a233beb624a47867942167cd9603000af325b`.
- `CA-C-111@2`: `.caprmedio_caprmedio/01_concern/CA-C-111-QUESTION--which-canonical-targets-do-the-legacy-subject-labels-identify.md`; SHA-256 `f276fee27794509dbda2293168ed43e7ef829f03c588f6ce929d95c5bcb39208`.
- `CA-C-117@1`: `.caprmedio_caprmedio/01_concern/CA-C-117-QUESTION--which-declarations-complete-the-authoritative-project-structure.md`; SHA-256 `18c58f8ab5fb4afaffe39137e0e0a54006d68bd45993b09d714e1cefea2a7846`.
- `CA-C-125@2`: `.caprmedio_caprmedio/01_concern/CA-C-125-QUESTION--which-legacy-scope-properties-should-be-retired-or-rebound.md`; SHA-256 `3b7f0d887bc023de9a938665ce0173b9b531fb0e2363e57c769c7a3b2140028a`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Metadata and construction consumers

M-207/M-208 describe generic frontmatter mechanics; their admitted Carrier population **and** per-kind schema **must** be explicit **before** claiming support for **every** Artifact. preserve caller-selected identity, source digest, explicit missing/error results, body-free returned metadata, authorized field-**only** patches, stale-precondition checks **and** rejection of Relation patches. a full-source digest can be computed by streaming; it does **not** contradict a body-free metadata result.

M-209 now follows R-1132's schema-driven construction rather than imposing Atom-**only** Content Role **and** title/body fields on **every** non-Atom Artifact. retain structural ownership, exact derived destination, collision rejection, preview, complete materialization verification **and** canonical Atom Tool responsibility. the correction does **not** establish a new generic schema, silently widen supported formats, **or** authorize native Tool changes.

## Additional inspected source Revisions

- `CA-M-207@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-207-TOOLS-METHOD--read-generic-artifact-metadata.md`; SHA-256 `6c00d1138110666a2a68e1c2490ce25abde33e0c7e2cb98e7ade58c2ccd59224`.
- `CA-M-208@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-208-TOOLS-METHOD--patch-generic-artifact-metadata.md`; SHA-256 `ebd4226199030ca789a23300ff9dab541da8d3f96a8e30a3ced22f5cc6920726`.
- `CA-M-209@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-209-TOOLS-METHOD--create-one-generic-artifact-carrier.md`; SHA-256 `9864e9b43452b1317e20dd61dc94e9f71ed558d92f7d673b8f0427326a5abddc`.
- `CA-R-1129@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1129-TOOLS-REQUIREMENT--read-artifact-metadata.md`; SHA-256 `eb6272b93ec3e074c1323bd34b602a9c4c45c5aaea7649a7faddc5543c26cc15`.
- `CA-R-1130@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1130-TOOLS-REQUIREMENT--patch-artifact-metadata.md`; SHA-256 `7fb7a1dfd375e0d64d61c82ee207eb8ea9bffb35ed50ae77dec6cc4d4b520b33`.
- `CA-R-1132@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1132-TOOLS-REQUIREMENT--create-an-artifact-carrier.md`; SHA-256 `0d543aa1ab03f259ba0a9853559d38f7e283cb1269ccbd9082380fe4c2613801`.
- `CA-R-1282@7`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1282-CORE_META_MODEL-CORE-REQUIREMENT--define-content-role-as-an-atom-property.md`; SHA-256 `555838efe33f1ee23c0f81b01afa034f8e81d1a5bc215ab1650b453f9dac4282`.

## Already extracted Action consumers

O-038 **and** O-039 already replace M-243 **and** M-244, but retain the legacy generic selector dimensions **and** endpoint descriptor schema. correct role identity alone does **not** resolve graph-qualified Relation ownership, per-kind applicability **or** distinct owner/target/Subject filters. retain complete body-free query results, stable ordering, exact errors, full relation-**only** preview, stale-precondition checks **and** unchanged body/unrelated metadata. do **not** widen target eligibility **or** replace several filters with one guessed alias.

## Additional inspected source Revisions

- `CA-O-038@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/09_operations/CA-O-038-TOOLS-ACTION--query-generic-artifacts-by-filters.md`; SHA-256 `3aaad3d31af62cb37b02b11864377abf49cdd853d68ca918c1735ce76e90fa1a`.
- `CA-O-039@1`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/09_operations/CA-O-039-TOOLS-ACTION--patch-generic-artifact-relations.md`; SHA-256 `983ff129f7e05a66815a6991c05cfac4d54b780ee26946dc7ddb1ad24e94faf5`.
- `CA-R-1131@14`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1131-TOOLS-REQUIREMENT--patch-artifact-relations.md`; SHA-256 `ca4852ea82117ed866cc860ca92a544d677567eef30391276bb5cb7e4c1997ba`.
- `CA-R-1135@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1135-TOOLS-REQUIREMENT--query-artifacts-by-filters.md`; SHA-256 `27e17b9774d9d32aa2704ca5ade8afa34db90aab6237dcba34894af75cc06cf9`.

## Evaluation consumers

E-409 **and** E-410 evaluate the already extracted O-038 **and** O-039 Actions. their fixtures still rely on the unresolved selector dimensions **and** endpoint schema above. formatting, body-access sentinels **and** rollback coverage do **not** establish the missing admitted field mapping. retain body-free query membership **and** ordering, explicit unsupported-filter rejection, exact relation-only effects, unchanged body **and** unrelated metadata, **and** real post-effect restoration evidence.

do **not** certify those legacy filters **or** endpoint descriptors merely because the corresponding Action **and** Evaluation agree. resolve the source schema first, **then** align the consumers **without** changing canonical Atom Tool ownership.

## Additional inspected source Revisions

- `CA-E-409@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-409-TOOLS-QA_CASE--verify-query-generic-artifacts-by-filters.md`; SHA-256 `147bdd81c9ac5b1ec8c67a71dadc452ce85e96b650ce9ab4109d40fe01ee473a`.
- `CA-E-410@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-410-TOOLS-QA_CASE--verify-patch-generic-artifact-relations.md`; SHA-256 `337700397a75136edbebbce9dbdedee9fffc67bdc315d0ab3af82444b616b1e0`.
- `CA-O-038@2`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/09_operations/CA-O-038-TOOLS-ACTION--query-generic-artifacts-by-filters.md`; SHA-256 `0b0918504fb6b78148266d5f265fd925e3dbe1ac9166ee41b56167e672660218`.
- `CA-O-039@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/09_operations/CA-O-039-TOOLS-ACTION--patch-generic-artifact-relations.md`; SHA-256 `344874f7e90b1814a1d684e711de73fa837bbed7e0f039678e646fc759a23440`.
