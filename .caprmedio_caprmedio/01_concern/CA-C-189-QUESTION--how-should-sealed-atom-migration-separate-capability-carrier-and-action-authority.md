---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Atom"
    - "Carrier"
    - "Action"
    - "Journal/Record"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-17 19:50:40 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should sealed Atom migration separate capability, Carrier, and Action authority?

which exact R/D/O owners preserve the sealed migration **and** rebinding boundaries currently combined across R-1048/R-1049 **and** their child Methods **and** Deliveries?

## Evidence

- R-1048/R-1049 combine required capabilities with exact JSON request fields, filename/frontmatter authority, version/timestamp encoding, receipt values, effect sequencing, **and** durable intake acknowledgement.
- M-155/M-156 supply planning **and** effect behavior; pure planner isolation is a construction choice, while resolve/validate/apply/intake is operational behavior. D-412/D-413 also repeat delegation **and** success gates beside source/launcher placement.
- R-1105 explicitly retains the MCP-only mutation gate. the audit's description of that gate as stale does **not** prove it is superseded. C-179 preserves Initiative identity uncertainty; C-180 preserves optional Git reconciliation boundaries.
- R-1049 intentionally permits removing invalid historical/unregistered relation entries while restricting newly rewritten targets. a broader relation domain alone does **not** authorize this particular Tool **to** add new kinds of references.

## Principle check

DRY requires one owner per obligation, **not** deletion of unique mutation safeguards. coherence requires interfaces, permitted targets, operational gates, **and** receipts **to** agree. information preservation protects exact-match checks, collision checks, untouched content, atomicity, concurrency preconditions, frozen bulk sets, **and** truthful acknowledgement.

## Disposition

preserve the existing capabilities **and** authorization gates. establish a lossless clause map **before** replacing role identities **or** splitting Action responsibilities. reuse C-179/C-180 for their already recorded questions. do **not** widen mutation permission, invent an Initiative replacement, discard receipt fields, translate relation meanings, **or** call a direct file repair an admitted MCP mutation. no Tool implementation **or** execution is part of this content repair.

## Inspected source Revisions

- `CA-R-1048@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1048-TOOLS-CORE-REQUIREMENT--migrate-one-sealed-atom-identity.md`; SHA-256 `cd0cb04c5107fed827b477e07ea93485a5043a043d32340a2924061aa64dc4c2`.
- `CA-R-1049@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1049-TOOLS-CORE-REQUIREMENT--rebind-one-active-atom-relation-set.md`; SHA-256 `634cfd0a005952e1235cb3f1ac50cc80c1001cde506cd8a0f87a1326cfbe9ef4`.
- `CA-M-155@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/MIGRATE_ATOM_IDENTITY/05_method/CA-M-155-MIGRATE_ATOM_IDENTITY-CORE-IMPL_METHOD--plan-one-sealed-atom-identity-migration.md`; SHA-256 `328998faa90cc0ac893c08ab5ee99332155a2cec8fbc3bca000d84dd765e704d`.
- `CA-M-156@8`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REBIND_ATOM_RELATIONS/05_method/CA-M-156-REBIND_ATOM_RELATIONS-CORE-IMPL_METHOD--plan-one-sealed-atom-relation-rebinding.md`; SHA-256 `af474efa5c28bc40544dfc88b96fcb0eaa90016562d6c75d3c188101f84d4afa`.
- `CA-D-412@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/MIGRATE_ATOM_IDENTITY/07_delivery/CA-D-412-MIGRATE_ATOM_IDENTITY-RELEASE_DEFINITION--deliver-sealed-atom-identity-migration-doer.md`; SHA-256 `5941e87ac44f753b65755bc13b4db3634dd0b47a78af532706f6b7e7d793dab9`.
- `CA-D-413@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/REBIND_ATOM_RELATIONS/07_delivery/CA-D-413-REBIND_ATOM_RELATIONS-RELEASE_DEFINITION--deliver-sealed-atom-relation-rebinding-doer.md`; SHA-256 `7626badc23ce072345f1fd3eacffa315e2dc140d1586eb4934671b53ffd7cff5`.
- `CA-R-1105@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP/04_requirement/CA-R-1105-MCP-REQUIREMENT--admit-atom-mutations-through-initiative-bound-mcp-operations.md`; SHA-256 `a52c1ea52f7f37af12c419b1036ba5bda71f30e6933596782980d6f93e1b5665`.
- `CA-R-1344@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `300b0d772013aad37e26ec465f6b59279fe1f756d45643b5b91434d0d7020401`.
- `CA-R-1453@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1453-CORE_META_MODEL-CORE-REQUIREMENT--define-process.md`; SHA-256 `ef8aef1fb7a2193b3647e4de316069b2dfa2f0fd4009178421fd61d886356db4`.
- `CA-C-179@1`: `.caprmedio_caprmedio/01_concern/CA-C-179-QUESTION--what-is-the-canonical-initiative-boundary-for-programmatic-mutation.md`; SHA-256 `a94f17a3d10be8280cad5cc38491baac8b65491674c931891de0bb273b0e3fb9`.
- `CA-C-180@2`: `.caprmedio_caprmedio/01_concern/CA-C-180-QUESTION--which-programmatic-provenance-rules-belong-to-optional-git-integration.md`; SHA-256 `7c9456b66c627699f104bf59f9754e22ad25c93ce1fe858cb9adbb8421ca348c`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
