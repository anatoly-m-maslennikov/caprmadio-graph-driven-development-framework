---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Artifact/Carrier"
  depends_on:
    - "Atom/Subjects"
    - "Atom/Tier"
    - "Atom/Content Role"
    - "Atom/Type"
    - "Evaluation"
priority: medium
version: 1
updated_at: "2026-09-17 20:53:28 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which current Carrier contracts replace legacy validator cases?

which current fixtures, immutable Summaries **and** stable diagnostics replace the legacy filename-prefix, Subject **and** tier validator cases **without** losing distinct defect coverage?

## Evidence

- E-074 assumes an unregistered four-character Type prefix; E-075 calls Content Role placement Type placement. the current filename distinguishes the role letter from the Type segment. changing **only** their fixture text would leave misleading Summary **and** diagnostic identities.
- E-081 **and** E-082 exercise subject_scopes; E-083 assumes a structural-scope vocabulary registry. D-269 instead admits one scalar governs target **and** unique depends_on paths, resolved under R-1202. E-084 already tests one GOVERNS with **any** number of DEPENDS_ON targets; do **not** repeat its completed repair **or** confuse the axes.
- E-085 rejects a numeric YAML tier; D-267/D-285 prohibit duplicating an address-derived tier regardless of its value. E-087 assumes a role-specific tier restriction **without** selecting an admitted rule. neither case establishes the complete current diagnostic contract by itself.

## Principle check

DRY rejects duplicate coverage **and** invented registries. coherence requires Summary, current Carrier rule, fixture **and** diagnostic **to** describe the same defect. information preservation protects missing versus duplicate versus unresolved target cases **and** explicit role/tier eligibility coverage; it does **not** permit silently equating those failures.

## Disposition

preserve the listed legacy cases pending a lossless coverage **and** replacement-identity map. reuse existing current cases **where** equivalent, create replacement identities **where** Summaries **must** change, **and** select exact stable diagnostics from the admitted Carrier contract. do **not** reinterpret a missing GOVERNS target as an empty dependency set, reject multiple valid dependencies, invent a global vocabulary catalog, **or** retain invalid Type-prefix semantics merely **to** keep a test passing. E-076/E-086/E-091/E-092 receive separately justified source/location/default fixes; those do **not** settle this remaining family. no validator implementation **or** test is run here.

## Inspected source Revisions

- `CA-E-074@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-074-TOOLS-QA_CASE--reject-unknown-type-prefix.md`; SHA-256 `9d82e17c0994aee5095df6451de18af05a330815a69b8be7a5cf50a754876d77`.
- `CA-E-075@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-075-TOOLS-QA_CASE--reject-type-placement.md`; SHA-256 `9de5890a600ef6e36728e9276a4f53c8ec15d267fbb8c2c4b921250a0f7a2ccc`.
- `CA-E-081@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-081-TOOLS-QA_CASE--reject-empty-subject-scope.md`; SHA-256 `1cb290b39a21a106c44c6fe10a756d0761e4b653bfac4aebf51bd410accbf496`.
- `CA-E-082@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-082-TOOLS-QA_CASE--reject-duplicate-subject-scope.md`; SHA-256 `e91ecba4c1043fa5773200b1d5af7d4ef55dff60250f36de45413517913a1a8e`.
- `CA-E-083@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-083-TOOLS-QA_CASE--reject-unknown-subject-scope.md`; SHA-256 `586c961627c361914a95d50557b3b43dbdf2b9c0cc58dec1535bd19288f82278`.
- `CA-E-084@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-084-TOOLS-QA_CASE--reject-rmed-subject-cardinality.md`; SHA-256 `253135a20329e9178cbf25a128619b89788e234948b5688b30a57f567b44d56f`.
- `CA-E-085@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-085-TOOLS-QA_CASE--reject-numeric-tier.md`; SHA-256 `5c110c327e5c606c87b2c40f3f6ca704d6d911d040573c927c59716c2c50f16d`.
- `CA-E-087@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-087-TOOLS-QA_CASE--reject-role-ineligible-tier.md`; SHA-256 `ca8bf6c99eeee7df3528cb3b133ed0530b967acec7fbe4c7b6f2c3e4feb7244a`.
- `CA-D-267@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-267-CORE_META_MODEL-DELIVERY--derive-address-facts-without-duplicated-frontmatter.md`; SHA-256 `d186c63788a393e2d20076b2a6138da43516248a7d9862ccc214d0589b425d40`.
- `CA-D-269@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter.md`; SHA-256 `f3b43a72109dbdb710295e46c37c1c5d86b7c15ff982f980bae8a845f6756f0b`.
- `CA-D-285@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-285-CORE_META_MODEL-DELIVERY--serialize-local-tier-filename-tokens.md`; SHA-256 `0ed90df6dd9e2e1b3a3cbafdf0f255872b890c346c6b1068377ee062d97adf85`.
- `CA-R-1201@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1201-CORE_META_MODEL-CORE-REQUIREMENT--require-one-governed-subject-on-every-atom.md`; SHA-256 `2485221d389e3833ab085a3eb3ee37bdec36a8d4fd1642e875d82f67cc3ec3ba`.
- `CA-R-1202@9`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once.md`; SHA-256 `278d76a83c9cc6d5915aeaed78c9bfbb8b60e67a0fc4928bb171cc7ec08ed77e`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
