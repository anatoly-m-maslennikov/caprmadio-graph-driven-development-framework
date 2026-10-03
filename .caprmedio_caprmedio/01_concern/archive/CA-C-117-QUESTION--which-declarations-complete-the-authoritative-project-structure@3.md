---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Project Structure"
  depends_on:
    - "Project Settings"
    - "Scope Unit"
    - "Implementation Folder"
    - "Atom/Content Role: Requirement/Type: Goal"
    - "Projection"
priority: medium
version: 3
updated_at: "2026-09-17 22:28:48 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which declarations complete the authoritative Project Structure?

which complete set of accepted Scope Unit declarations **and** exact authority/Implementation Folder bindings should become `.caprmedio_caprmedio/project_structure.toml`?

## Evidence

CA-R-1483, CA-R-1484, **and** CA-D-440 require **=1** authoritative declaration Carrier. that file is absent. Project Settings resolves the root identity **to** `caprmedio` but supplies no `scope_units` declaration set. current Goal Atoms identify intended unit relationships **and** CA-D-325 still holds concrete methodology-source bindings; neither a Goal nor an observed folder is itself the new structural declaration. older binding **and** name/order Atoms have **not** all been migrated away.

physical nesting alone cannot settle the complete logical tree: CORE_META_MODEL **and** PROJECT_CONFIGURATION use nested Framework Carriers while their Goals belong **to** METHODOLOGY_SOURCES under FRAMEWORK_METHODOLOGY. INSTALLED_EXTENSIONS has Goal authority, while CA-R-1228 permits an empty Extension contribution **without** requiring an empty collection Carrier. ordinary Engine units also retain legacy labels **and** address conventions. all selected values need one verified declaration **without** converting accidental materialization into authority.

## Principle check

CA-M-002 requires one structural source; CA-M-006 requires coherent logical ownership **and** bindings; CA-R-1490 preserves still-needed Goals **and** historical declarations. these reject both an independent duplicate table **and** a blind promotion of the old generated structure. current CA-R-1070, CA-M-149, **and** CA-E-164 already respect the declaration boundary; no Tool result can authorize new structural choices merely by observing folders.

## Disposition

defer unsupported declarations **and** binding choices. assemble a complete evidence-backed migration frontier **before** activating the TOML, reconcile conflicting legacy declarations, preserve Goal coverage separately, **and** retire redundant concrete binding authority **only** after the exact values are represented **and** checked. until then, Project-to-Methodology ownership moves **and** structural target certification remain incomplete; do **not** fill unknown values from the filesystem **or** an obsolete Projection by assumption.

## Current authority inspected

- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1483-CORE_META_MODEL-CORE-REQUIREMENT--define-authoritative-project-structure.md` at Version **2**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations.md` at Version **2**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-862-CORE_META_MODEL-CORE-REQUIREMENT--bind-scope-unit-places-without-requiring-local-delivery-atoms.md` at Version **13**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-440-CORE_META_MODEL-CORE-DELIVERY--store-one-authoritative-project-structure-toml.md` at Version **2**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-325-DELIVERY--place-applicable-methodology-sources.md` at Version **10**.
- `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/04_requirement/CA-R-1172-FRAMEWORK_METHODOLOGY-DEFINES_GOAL_FOR-METHODOLOGY_SOURCES--make-the-caprmedio-governing-model-recursively-self-applicable.md` at Version **10**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/04_requirement/CA-R-1174-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-CORE_META_MODEL--provide-the-minimal-self-applicable-canonical-methodology-model.md` at Version **10**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/04_requirement/CA-R-1175-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-INSTALLED_EXTENSIONS--preserve-installed-extension-revisions-as-candidate-inputs.md` at Version **10**.
- `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/04_requirement/CA-R-1176-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-PROJECT_CONFIGURATION--select-core-meta-model-and-project-configuration-for-compilation.md` at Version **12**.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1070-TOOLS-REQUIREMENT--derive-the-project-scope-unit-graph-and-sources-projection-from-configuration-authority.md` at Version **13**.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/05_method/CA-M-149-TOOLS-CORE-METHOD--generate-the-project-scope-unit-graph-from-configuration-authority.md` at Version **14**.
- `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-164-TOOLS-QA_CASE--rebuild-the-scope-unit-graph-and-sources-projection-from-configuration-authority.md` at Version **11**.

## Missing-folder integrity fixture

E-126 still defines a missing structural unit by deleting a folder required by Project Settings. R-1483/R-1484 instead distinguish accepted Project Structure declarations from materialization; an unmaterialized declaration remains declared. preserve **any** genuinely required-folder coverage, but identify its applicable materialization rule, Summary **and** diagnostic **before** replacement. do **not** declare **every** unmaterialized unit nonexistent **or** silently delete the test. the unknown-declaration cases E-076 **and** E-127 are corrected separately **and** do **not** settle missing materialization.

## Additional inspected source Revisions

- `CA-E-126@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-126-TOOLS-QA_CASE--reject-missing-structural-scope.md`; SHA-256 `9aa6cf7493f87f8a4c6cec61db1bb8d4b1fbc6b9b30b1da223fed5e8ca8e0852`.
- `CA-R-1483@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1483-CORE_META_MODEL-CORE-REQUIREMENT--define-authoritative-project-structure.md`; SHA-256 `a7906250415ecfabbdbbcfb6aa1041e63f8b4858147dc733c95696998bce5cb8`.
- `CA-R-1484@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations.md`; SHA-256 `e3ccdc37a334c699417322eb3dd409a6006f598773e6333fa92ebc2a951aed9c`.

## TARGET_SET declaration consumers

R-1153, M-219 **and** E-337 repeat the immediate TOOLS parent, legacy unordered_unit classification, level 4 **and** concrete authority/Implementation paths. R-1483/R-1484 make the accepted Project Structure declaration the sole authority for those facts. the source values **must** be reconciled with that accepted declaration, **not** copied into another independent registration **or** silently replaced by new guessed values.

preserve the Finder capability, exact identity/selector resolution, unique ordered membership, source frontier, digest **and** no-check/no-mutation boundary while settling the declaration migration. E-337's separate source-timing ambiguity is corrected: a changed captured frontier is stale, whereas a fresh valid request **may** use a new stable frontier. that correction does **not** certify its retained legacy structural fixture. do **not** infer a Tool Scope Unit from directory existence **or** mutate Project Structure during this review.

## Additional inspected source Revisions

- `CA-R-1153@16`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/04_requirement/CA-R-1153-TOOLS-REQUIREMENT--define-the-target-set-tool-unit.md`; SHA-256 `765c68e1f1194a24ad3c8d51d754bdbcaaeec3468d4931307afbb13f791e1a90`.
- `CA-M-219@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/05_method/CA-M-219-TOOLS-METHOD--resolve-one-target-set.md`; SHA-256 `4fc928993639f1123950156240409e9bd3b0a30a69b79a6c892e1ed240056a47`.
- `CA-E-337@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-337-TOOLS-QA_CASE--verify-resolve-one-target-set.md`; SHA-256 `4a0239d78fcd266551ab407402881988e6e5f2fefda63bb274124c405a707361`.
- `CA-R-1483@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1483-CORE_META_MODEL-CORE-REQUIREMENT--define-authoritative-project-structure.md`; SHA-256 `a7906250415ecfabbdbbcfb6aa1041e63f8b4858147dc733c95696998bce5cb8`.
- `CA-R-1484@2`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations.md`; SHA-256 `e3ccdc37a334c699417322eb3dd409a6006f598773e6333fa92ebc2a951aed9c`.
