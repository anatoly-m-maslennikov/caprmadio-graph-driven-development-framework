---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Operator"
    - "Artifact/Carrier"
    - "Atom/Identifier"
priority: medium
version: 1
updated_at: "2026-09-17 22:58:06 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which Atom operations cover external Project Goals?

which canonical Atom operation boundaries admit external Project Goals with their distinct identity **and** Carrier rules?

## Evidence

R-865 **and** O-032 restrict creation **to** configured Content Role locations. their identity checks distinguish identified Project-owned Atoms from unassigned Drafts. D-292 separately defines external Project Goal filenames **without** a Project prefix, Content Role letter **or** number. absence of a Project Atom ID therefore does **not** by itself mean Draft.

R-868 **and** O-029 likewise use Content Role ownership **and** role-local archive destinations. their recent replacements correctly preserve exact bytes **and** the archive version suffix, but that does **not** establish the permitted external Goal target **and** lifecycle location. this is a coverage boundary, **not** proof that **any** non-Atom file **may** bypass validation.

## Principle check

coherence requires external Goals **to** retain their own accepted identity **and** carrier rules. DRY **and** minimum necessary complexity favor reuse of admitted operation mechanics instead of a guessed parallel Tool. Operator authority **and** information preservation prohibit silently widening effect targets, assigning a Project ID **to** an external Goal, dropping safeguards **or** treating uncertain coverage as a passing test.

## Disposition

preserve the ordinary Atom capability **and** its completed Action replacements while resolving exact external Goal admission, placement **and** lifecycle ownership. determine whether existing canonical Tools cover this case through registered applicability **or** another existing boundary **before** changing them. do **not** create a new Tool, infer permission from an observed root file, relabel an external Goal as Draft, **or** remove identity/history/transaction checks. add explicit external-Goal conformance cases **only** **after** the complete target contract is established.

## Inspected source Revisions

- `CA-R-865@14`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_CREATE/04_requirement/CA-R-865-ATOM_CREATE-CORE-REQUIREMENT--create-caprmedio-markdown-atoms.md`; SHA-256 `7eb610e1374b4b42ba957b6aca12f80e2bb37afadd24b92fc4f4c8e101a43b7c`.
- `CA-O-032@4`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_CREATE/09_operations/CA-O-032-ATOM_CREATE-ACTION--create-sealed-caprmedio-atom-carriers.md`; SHA-256 `a0f87b115d4620114776f54e7b587d5f285f02329849e6b2a0c5ac8fd85d9d9b`.
- `CA-E-303@13`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_CREATE/06_evaluation/CA-E-303-ATOM_CREATE-QA_CASE--verify-create-sealed-caprmedio-atom-carriers.md`; SHA-256 `4b5108faa6794535a0f0d9e3d6747f0e153235556830e1643e3b85277111b584`.
- `CA-R-868@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_ARCHIVE/04_requirement/CA-R-868-ATOM_ARCHIVE-CORE-REQUIREMENT--archive-active-atoms.md`; SHA-256 `8ba1e208311ce5d44a291ff5c206ab8ec2cf87c09082623f7bab30ae3bf95292`.
- `CA-O-029@3`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_ARCHIVE/09_operations/CA-O-029-ATOM_ARCHIVE-ACTION--archive-selected-active-atoms.md`; SHA-256 `11678d524015ac709c632fdfde6a48528625b5888b49035db71dca30821a18a4`.
- `CA-E-306@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_ARCHIVE/06_evaluation/CA-E-306-ATOM_ARCHIVE-QA_CASE--verify-archive-selected-active-atoms.md`; SHA-256 `4cc6e096820c582f695a1dbf241189cac0bc6bb4ecfabc11d7cc19d0431cfbc6`.
- `CA-D-292@12`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL-DELIVERY--serialize-external-project-goal-filenames.md`; SHA-256 `0fcc2a4084bb217f02732d724dc97d21a67f3c1905f403809069a41493b83c2f`.
- `CA-D-450@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-450-CORE_META_MODEL-DELIVERY--number-project-owned-atoms-within-each-content-role.md`; SHA-256 `f86090c84d7117a8bf25b5d2fd8ccb1f2e7d3bfb63d931cb336659314ec42cc0`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
