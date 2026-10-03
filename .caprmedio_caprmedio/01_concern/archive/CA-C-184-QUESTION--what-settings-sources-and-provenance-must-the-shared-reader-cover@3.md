---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Project Settings"
    - "Default Settings"
    - "Project Structure"
    - "Artifact/Revision"
    - "Carrier"
priority: medium
version: 3
updated_at: "2026-09-17 21:23:15 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# What Settings sources and provenance must the shared Reader cover?

which parameter families must the shared Settings Reader cover, **and** how should their existing authority, precedence, currentness, **and** Carrier bindings be exposed **without** merging their owners?

## Evidence

M-284 incorrectly called Project Settings a Projection **and** selected `.caprmedio_caprmedio/caprmedio_project_settings.toml`. META-REQU-619 makes Project Settings authoritative; D-364 requires the project-named Carrier; D-365 binds Revision currentness through Journal evidence. that clear authority error is corrected. the observed filesystem still has the legacy filename, **not** the required project-named Carrier; this repair does **not** migrate it **or** certify currentness.

META-REQU-675 separates initialization inputs, Framework Instance behavior choices, **and** per-unit overrides. M-279 supplies parameter-level Framework/default resolution, preserving valid false/zero/empty selections **and** rejecting invalid explicit values. M-284's present Project Settings-only consumer boundary does **not** establish coverage of those other families. a shared parser alone does **not** resolve their different authority **or** precedence.

## Principle check

DRY requires shared mechanics **and** one owner per value, **not** one combined Settings authority. coherence requires consumers **to** follow current sources **and** precedence; information preservation protects explicit values, absence semantics, provenance, **and** no-reader-writes behavior.

## Disposition

preserve read-only immutable snapshots **and** dedicated mutation. map exact parameter families **to** existing source owners **and** applicable resolution rules **before** expanding the Reader contract. record the physical Carrier migration separately; do **not** read legacy filenames as an implicit fallback, invent defaults, modify Settings, rebuild Tools, **or** claim that the corrected Method proves runtime compliance.

## Inspected source Revisions

- `CA-M-284@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md`; SHA-256 `3865ada138452bc4c1baa6bae777a140872d48cbde9f85459f8f32179a998b94`.
- `CAPRMEDIO-META-REQU-619@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-619-CORE_META_MODEL-CORE-REQUIREMENT--define-project-settings.md`; SHA-256 `7855feedc15fabbd33ddb5c973606a40b45a2a1b3e1caafe0f87a89e1c4a2a11`.
- `CAPRMEDIO-META-REQU-675@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-675-CORE_META_MODEL-CORE-REQUIREMENT--partition-operator-settings-between-settings-artifacts.md`; SHA-256 `48173167bb3c39dae4a86263e449ac4d45333fe3ec1c02590e3fdb60ec79da08`.
- `CA-D-364@6`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-364-CORE_META_MODEL-DELIVERY--bind-project-settings-to-its-authoritative-toml-carrier.md`; SHA-256 `5d2d615155201df76cae3c7ae218dbb34e152e5a52eec9867bf9a6ebb0c3c270`.
- `CA-D-365@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-365-CORE_META_MODEL-DELIVERY--bind-project-settings-revisions-to-journal-receipts.md`; SHA-256 `e4072704bab06ff5ed4c067c3ef871017896666e2f1be126e34ab43edc164100`.
- `CA-M-279@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-279-CORE_META_MODEL-GENERAL-METHOD--resolve-missing-framework-parameters-from-default-settings.md`; SHA-256 `d71dcba2350bee811204735732ab3ac2c56369222e20010b13147ac3a89aab26`.
- `CA-R-1441@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1441-CORE_META_MODEL-CORE-REQUIREMENT--define-default-settings.md`; SHA-256 `01e2b43f029ebd58500fbea23bf466c32535763995f4a86ac7d4cbb4d53321aa`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.

## Legacy Settings Evaluation consumers

E-134 regenerates Project Settings from sources; E-135 **and** E-155 validate the source-address **and** source-digest metadata of that old Projection model. META-REQU-619 instead makes the Settings TOML authoritative. D-365 binds its current Revision **and** Digest through a completed Journal receipt; M-284 permits a derived read-only snapshot, **not** regeneration of the authority from Project Atoms.

preserve the reproducibility, exact-address **and** exact-digest checks **until** **every** is mapped **to** its actual current object: authoritative Settings Carrier, Journal receipt **or** derived Reader snapshot. those are **not** interchangeable sources. resolve the replacement Summary, identity **and** stable diagnostic for **every** case **before** changing it. do **not** invent new Settings provenance fields, rewrite Settings, **or** silently call a receipt-backed mismatch a legacy Projection failure. these tests are **not** evidence that the live Settings have been migrated **or** validated.

## Additional inspected source Revisions

- `CA-E-134@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-134-TOOLS-QA_CASE--reject-non-reproducible-settings.md`; SHA-256 `584193689e9b73ed17922e2c8e1aa5ec8d8469a5901b43db03cf28efd5a0eb2d`.
- `CA-E-135@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-135-TOOLS-QA_CASE--reject-settings-source-address.md`; SHA-256 `105fd6b449b197e8d6ac10f1e99cc3e949294136d58435352b07d82f9ec2d881`.
- `CA-E-155@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS/06_evaluation/CA-E-155-TOOLS-QA_CASE--reject-settings-source-digest.md`; SHA-256 `cc7938660640ebe9b3362afd1066c990c397cededc6a40bd5dc6eb3ce7a398bc`.
- `CA-D-365@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-365-CORE_META_MODEL-DELIVERY--bind-project-settings-revisions-to-journal-receipts.md`; SHA-256 `e4072704bab06ff5ed4c067c3ef871017896666e2f1be126e34ab43edc164100`.
- `CAPRMEDIO-META-REQU-619@17`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-619-CORE_META_MODEL-CORE-REQUIREMENT--define-project-settings.md`; SHA-256 `7855feedc15fabbd33ddb5c973606a40b45a2a1b3e1caafe0f87a89e1c4a2a11`.
- `CA-M-284@11`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary.md`; SHA-256 `690b9f8716d649e8d27a7e63ff0129455d6de14f9cf3fd30a7173cf25f9dc049`.
