---
atom_id: CA-D-572
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-05 16:25:00 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Additive selected-route source admission"
  depends_on: [Tool, Workflow, Action, Manifest, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1876, CA-R-1877, CA-R-1878, CA-R-1879, CA-M-331, CA-M-332]
---
# Summary

Serialize additive Release route source admission

## Scope

The one Release Version source-admission record which a successor canonical selected-workflow manifest needs before admitting `release_version`.

## Claim

A successor of `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` **must** admit `release_version` only through the one closed `release_source_admissions` serialization below. It carries CA-P-1622@4 at `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/done/02-CA-P-1622-TASK--review-release-version-source-and-admission.md`, SHA-256 `7cd6a839a190add10108bdd5e58700aeae7a89316aa721b2b5340bda865a2739`, the exact current O164–O179 pins, and the full accepted Release RMED frontier including CA-D-573@2 and CA-D-574@1.

## Details

`release_source_admissions` is an optional top-level array in the loaded canonical `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` manifest file. It is never a member of D527's request `definition_manifest`, which remains exactly the existing two fields `manifest_ref` and `manifest_digest`. The current fifteen-route manifest omits this array. A successor which contains `release_version` **must** contain it with cardinality exactly one; a manifest without that route **must not** carry a Release admission. No unknown member of that admission array or its record is accepted. Its one record has exactly `route`, `acceptance_frontier`, `workflow`, `ordered_steps`, `ordered_actions`, `rmed_frontier`, `mutation_capable`, and `native_action_calls`; `route` is exactly `release_version`.

Every `acceptance_frontier`, `workflow`, `step`, `action`, and `rmed_frontier` member is the existing canonical manifest pin object with exactly `atom_id`, positive integer `version`, safe Project-relative `source_path`, and lowercase 64-hex `digest`. `acceptance_frontier` is exactly CA-P-1622@4 above. `workflow` is exactly:

| Atom | Version | Source path | SHA-256 |
| --- | --- | --- | --- |
| CA-O-164 | 3 | `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-164-PROJECT_CONFIGURATION-WORKFLOW--release-a-selected-framework-version.md` | `3f0fa17f96e96a14888ccc131943bb5e743b05447a2f67f8a238541e6541df0d` |

`ordered_steps` has exactly the following ten entries, in this order. Each entry has exactly `step` and `action` pin objects; it is neither a set nor an inferred graph. `ordered_actions` has exactly ten pin objects and is the same ordered action occurrence sequence, including repeated Action pins: CA-O-165, CA-O-165, CA-O-166, CA-O-166, CA-O-168, CA-O-167, CA-O-168, CA-O-168, CA-O-169, CA-O-169.

| Order | Step pin | Action pin |
| --- | --- | --- |
| 1 | CA-O-170@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-170-PROJECT_CONFIGURATION-STEP--freeze-the-executing-and-candidate-release-versions.md` `621cd9c836bdf1398594723e456f1155f9f8725c780d88b47fbc92b92f1c14e5` | CA-O-165@2 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-165-PROJECT_CONFIGURATION-ACTION--freeze-and-validate-the-release-boundary.md` `64afd80c7f93eca5a4047647f52b1471b016426fefbcf14de0eba5dfd8fec909` |
| 2 | CA-O-171@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-171-PROJECT_CONFIGURATION-STEP--validate-the-selected-release-delivery-bindings.md` `9fb2188769963363af44489043771214f889afd849f1c8eb4f8a0cdac2a5c6fd` | CA-O-165@2 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-165-PROJECT_CONFIGURATION-ACTION--freeze-and-validate-the-release-boundary.md` `64afd80c7f93eca5a4047647f52b1471b016426fefbcf14de0eba5dfd8fec909` |
| 3 | CA-O-172@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-172-PROJECT_CONFIGURATION-STEP--deliver-the-complete-candidate-methodology-sources.md` `2dc8c989b95ad1c64e1533491a1fb6195fc663fb764d4d5a52115e6c3c4f12a9` | CA-O-166@3 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-166-PROJECT_CONFIGURATION-ACTION--deliver-and-compile-candidate-methodology.md` `553a2dac5f8413242f119f02a88ff0e1915902ffb7a6d3326c9a1e831aa6ee91` |
| 4 | CA-O-173@3 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-173-PROJECT_CONFIGURATION-STEP--compile-the-candidate-applicable-methodology.md` `f5209614e245abcd3f1b38ab60c2b23f3f92f3b6f7682af8b9302f028cf255b8` | CA-O-166@3 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-166-PROJECT_CONFIGURATION-ACTION--deliver-and-compile-candidate-methodology.md` `553a2dac5f8413242f119f02a88ff0e1915902ffb7a6d3326c9a1e831aa6ee91` |
| 5 | CA-O-174@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-174-PROJECT_CONFIGURATION-STEP--run-the-complete-candidate-release-test-suite.md` `81b97982ffb40623f2aee6fc2d337eea33c978866f7d2e63e802cf03b9f7a6f4` | CA-O-168@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-168-PROJECT_CONFIGURATION-ACTION--verify-candidate-release-package-and-image.md` `ec4c7b0c42924f33b816b3f9a00f00d80b05119087283e1dc8c2674087256704` |
| 6 | CA-O-175@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-175-PROJECT_CONFIGURATION-STEP--stage-the-candidate-framework-package-and-ca-skill.md` `ba058eaf5a125a8053e1df87e54078c835da2551583edfb5837f9453b1625c87` | CA-O-167@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-167-PROJECT_CONFIGURATION-ACTION--install-candidate-runtime-package-and-skill.md` `1c016231b149b3096f1e66452707dddf59d4e8befab8c155406ab42144d4b142` |
| 7 | CA-O-176@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-176-PROJECT_CONFIGURATION-STEP--build-the-candidate-release-image.md` `e1b6a9bfa1603d926e54fd16b3dd3379b9a3bc2667e9e7095a608b69c6b0ae1c` | CA-O-168@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-168-PROJECT_CONFIGURATION-ACTION--verify-candidate-release-package-and-image.md` `ec4c7b0c42924f33b816b3f9a00f00d80b05119087283e1dc8c2674087256704` |
| 8 | CA-O-177@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-177-PROJECT_CONFIGURATION-STEP--prove-the-actual-candidate-package-and-image.md` `a26a2740b4324ee40b3d55f2cc6c90eb917c0b05785fed69df087f3a9f3c24a4` | CA-O-168@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-168-PROJECT_CONFIGURATION-ACTION--verify-candidate-release-package-and-image.md` `ec4c7b0c42924f33b816b3f9a00f00d80b05119087283e1dc8c2674087256704` |
| 9 | CA-O-178@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-178-PROJECT_CONFIGURATION-STEP--promote-the-candidate-runtime-and-project-local-ca-skill.md` `90deb140df692959689388e3785860fa5fc450ea63f1b9a6645215580e0b658d` | CA-O-169@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-169-PROJECT_CONFIGURATION-ACTION--promote-candidate-and-retire-exact-prior-image.md` `a3e492fee45833a17f78bb99a61c3c59c1ca1185f2b357b6f41c7cb2d8ad969f` |
| 10 | CA-O-179@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-179-PROJECT_CONFIGURATION-STEP--retire-the-exact-prior-image-after-promotion.md` `7472a8e806ed0859a611c733bc130fcddc11a2dab9d033492732a9253cbb8107` | CA-O-169@1 `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-169-PROJECT_CONFIGURATION-ACTION--promote-candidate-and-retire-exact-prior-image.md` `a3e492fee45833a17f78bb99a61c3c59c1ca1185f2b357b6f41c7cb2d8ad969f` |

## Route serialization metadata

```json
{"mutation_capable": true,"native_action_calls": []}
```

This one unique delivery-level object is part of the one Release admission record. `mutation_capable: true` declares a potentially effectful route; it grants neither permission nor automatic execution. `native_action_calls: []` declares that the record adds no direct native Action calls outside the Action pins bound by `ordered_steps` and `ordered_actions`. The record serializes no catch-all transition, outcome, or execution policy: CA-O-164@3 and the generic executor retain the existing catch-all stop behavior. This metadata therefore neither creates a second Workflow graph nor omits that behavior.

`rmed_frontier` has exactly the following source pins, each once, in ascending Atom ID order within content role. It is source evidence only: it never contains D572, a canonical-manifest digest, a caller approval, a Run result, or any self/final/expected output digest that would make a self-hash or cross-hash cycle.

| Atom | Version | Source path | SHA-256 |
| --- | --- | --- | --- |
| CA-R-1876 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1876-TOOLS-REQUIREMENT--seal-release-version-request-and-candidate-boundary.md` | `f1240a46da3456d44fc3f7691fde0b050a67ed146b1b0bca2b8bfc697195d820` |
| CA-R-1877 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1877-TOOLS-REQUIREMENT--require-complete-framework-release-manifest.md` | `6779176be413d3c0f69f85b890941ce4ee0c1b313bcec2edacbeb005e452dad5` |
| CA-R-1878 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1878-TOOLS-REQUIREMENT--preserve-authoritative-sources-and-derived-release-boundaries.md` | `cd452283befce49a220323a5d93413fe71ceb46ced75be4ef25f5eced5de6366` |
| CA-R-1879 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1879-TOOLS-REQUIREMENT--freeze-executing-release-and-pin-candidate-currentness.md` | `cc5c6a4da157ad1b41c3487fb358d11aed9ad54163a5a17d1266b22dc19d8c93` |
| CA-R-1880 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/04_requirement/CA-R-1880-TOOLS-REQUIREMENT--preserve-prior-release-and-truthful-failure-recording.md` | `205eff8b642596cabc4ca645226a904a2da67ba9673b35a2dfcb820f62092816` |
| CA-M-331 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-331-TOOLS-METHOD--construct-sealed-release-version-candidate-manifest.md` | `f21d14db580cdab298247d40e0ea11bb226e3ff92109c691c9543b86d71fe54d` |
| CA-M-332 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-332-TOOLS-METHOD--derive-complete-release-delivery-plan.md` | `d4e7d56e164dda4b0203ec163d661dbbb3ba0cff479840ada2e6a751eb512a82` |
| CA-M-333 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/05_method/CA-M-333-TOOLS-METHOD--derive-release-gate-and-retirement-decision.md` | `bae178535465a791c34220e4469ecb7465974207b5a541ded90ca7ac2c5fb62c` |
| CA-E-571 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-571-TOOLS-QA_CASE--verify-sealed-release-input-and-manifest-boundaries.md` | `a7b1ba81dba2fe1727f39eae83e143b33db5a54b5db1c32efcc52b201068a9cb` |
| CA-E-572 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-572-TOOLS-QA_CASE--verify-complete-framework-package-and-full-suite-gate.md` | `0add9d0b18c8695dc49f01bae84ece6bf07c0639af3e305fb8fc3aa652d705bf` |
| CA-E-573 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-573-TOOLS-QA_CASE--verify-installed-runtime-skill-and-candidate-image-evidence.md` | `f1036775a73e99f14fed4416b017cf938555382ba73d39b0f7ff255d1137c357` |
| CA-E-574 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/06_evaluation/CA-E-574-TOOLS-QA_CASE--verify-release-failure-rollback-and-safe-image-retirement.md` | `584e910e69dd3c8ef3c44ad9d694adaca3e533c1fd6407acbbb02ba171e2bb82` |
| CA-D-560 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-560-TOOLS-DELIVERY--bind-release-version-tool-request-and-result-boundary.md` | `df88a519c1676f621e0fbfca66b9ebc63a84a6f0732625f5e652df161df08c10` |
| CA-D-561 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-561-TOOLS-DELIVERY--bind-release-source-compilation-and-package-carriers.md` | `a2198ba1a3d038100ad8f5ef6fd774a50fa2249906a4340656e9871880d56e7d` |
| CA-D-562 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-562-TOOLS-DELIVERY--bind-full-framework-runtime-installation-boundary.md` | `d6509c48567ec4627616597950d892fb6fba5f287f86dbff2e828b1578f5190b` |
| CA-D-563 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-563-TOOLS-DELIVERY--bind-project-local-ca-skill-without-hooks.md` | `f73a38dd7b634d654a7044f20c96240a0d1f850c4a71e4eef18f98d074cdbb3d` |
| CA-D-564 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-564-TOOLS-DELIVERY--bind-candidate-image-and-safe-retirement-evidence.md` | `ca6d734334c258fc0e1493b4161cc184762649be6b6ba33fdbc2958ec79ce2b4` |
| CA-D-566 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-566-TOOLS-DELIVERY--encode-sealed-candidate-snapshot-manifest.md` | `825ae839bb6a151b7f4a45fbb01ae6fb2491d0f8bf68204ca2a21f2f34657a7d` |
| CA-D-567 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-567-TOOLS-DELIVERY--bind-validated-compiler-and-package-handoff.md` | `1b99cb85186a1899d72eb07cc3c6ef6589613dd4c732e6dc387d7b76524329b8` |
| CA-D-571 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-571-TOOLS-DELIVERY--encode-deterministic-release-child-manifest.md` | `24dc030c0a95dc21c72a4b054c1eae088a004550bed0efd75265c2ad95fc753c` |
| CA-D-573 | 2 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-573-TOOLS-DELIVERY--serialize-approved-release-rollback-retention.md` | `5db7045ec34fbd9aea129d63262f6fce1ac5a6bff2b147af90a9fad6e560adad` |
| CA-D-574 | 1 | `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/07_delivery/CA-D-574-TOOLS-DELIVERY--serialize-typed-release-recovery-checkpoints.md` | `d1162607c515afe184ba2488d6030acc93b522331b3a819c520792db39e28012` |

The record is additive source-admission serialization only. It preserves the original thirteen CA-A-1142@2 registry entries and both unchanged query-source admissions (CA-P-1618@1 and CA-P-1535@2) in the same canonical manifest. It is not a second registry, Workflow graph, executor, permission grant, generic effect schema, caller-supplied approval, or dispatch result. Its typed metadata neither changes CA-O-164@3's catch-all stop behavior nor confers permission or automatic execution. A route-bound current Operator authorization and D527 preview/currentness rechecks remain required for `execute`; no admission record itself creates a Run, queue intent, Journal Event, compiler result, package effect, or release completion. Absent, duplicate, malformed, stale, digest-mismatched, out-of-order, incomplete, or self/cross-hash-cyclic Release evidence rejects before shared support.
