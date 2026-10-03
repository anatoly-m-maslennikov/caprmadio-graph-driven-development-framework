---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Action"
    - "Process"
priority: medium
version: 1
updated_at: "2026-09-17 19:03:32 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should Python workflow selections separate conventions, Carriers, and Actions?

which Claims from the shared Python workflow family remain reusable Implementation choices, **and** which require separate Carrier **or** operational authority?

## Evidence

- M-221 selects uv but also defines install/change/run/exception behavior, exact command forms, installed-runtime independence, **and** temporary placement. its old Operations-evidence wording is corrected separately; this does **not** settle the remaining partition.
- M-280 selects idioms by declared benefit while preserving explicit string/concurrency choices **and** compatibility exceptions.
- M-281 selects CPython 3.14.* but also governs technical-configuration centralization, runtime Settings separation, **and** shared Reader use. D-250 already owns the technical configuration Carrier.
- M-282/M-283 select Ruff/Mypy **and** also contain run/admission/exception or suppression conditions.
- M-286 selects bounded Pydantic validation; validate-once **and** strictness conventions are **not** automatically Process definitions.

## Principle check

DRY requires reusing selection **and** Carrier owners; coherence requires exact constraints **and** consumers **to** remain aligned. minimum complexity rejects an Action created merely **to** change a role label. information preservation protects approved technologies, pinning/locking, exception approval, suppression explanation, strictness, runtime independence, **and** confinement.

## Disposition

preserve accepted technology choices **and** constraints. map independent conventions, field/path encodings, **and** execution contributions losslessly **before** splitting **or** replacing identities. do **not** upgrade packages, alter commands, choose new settings, install a runtime, weaken admission gates, **or** turn every algorithm into an O Process. exact values in the existing Method remain unchanged pending their owner map.

## Inspected source Revisions

- `CA-M-221@12`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-221-PROGRAMMATIC-CORE-METHOD--use-uv-as-the-default-python-workflow-frontend.md`; SHA-256 `dd6b4f7e682970c16cd3ab2f66b366675636c08dcbd9a9cfa842694f8624006c`.
- `CA-M-280@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-280-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit.md`; SHA-256 `8a91cae1ca34461a5723a65288f4c2ac835af4b737eed2a0c1f725f420b2a30d`.
- `CA-M-281@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-281-PROGRAMMATIC-CORE-METHOD--declare-one-python-and-software-configuration-boundary.md`; SHA-256 `4056499a8e3f62f4b27ead7259d5f4cade74c3686896913311bf95a3d7dcf98a`.
- `CA-M-282@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-282-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity.md`; SHA-256 `92f3c3dabef677e770020c06b38c543f9f88f8aaa2368b4a7790fca29d0f0142`.
- `CA-M-283@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-283-PROGRAMMATIC-CORE-METHOD--use-mypy-for-static-python-type-checking.md`; SHA-256 `2dee325c367c8f63f61b115be3bd7b4761a272ae5802294653383fdb465bcaa6`.
- `CA-M-286@7`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-286-PROGRAMMATIC-CORE-METHOD--validate-untrusted-structured-data-with-pydantic.md`; SHA-256 `b50a6ba1fbfba17e746f57b34b424f8beefb9382a07bb06bd2f3cd630d602d30`.
- `CA-D-250@9`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/07_delivery/CA-D-250-PROGRAMMATIC-CORE-DELIVERY--provide-programmatic-software-carriers.md`; SHA-256 `0631b4211c0973f6f622e3a3b7ca956f17c67e2d442d3149958ff0f7c7d32520`.
- `CA-R-1340@8`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1340-CORE_META_MODEL-CORE-REQUIREMENT--define-method-content-role.md`; SHA-256 `f00d924a7f6f44ec8bd34548030ef5eb8f6f47e95a4437914a323aec6465fc8f`.
- `CA-R-1344@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `300b0d772013aad37e26ec465f6b59279fe1f756d45643b5b91434d0d7020401`.
- `CA-R-1452@4`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1452-CORE_META_MODEL-CORE-REQUIREMENT--define-action.md`; SHA-256 `f6bf25fa0e9868bb29311aebc9dde8a7f42fa3b7ab8bd9a7359f3546de931ea1`.
- `CA-M-002@15`: `.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md`; SHA-256 `943be84418b6f865e85d172845892c58187917d22dad56bb6103c5ded7cc6834`.
- `CA-M-005@8`: `.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md`; SHA-256 `cd4f3ec4fa61d979997600fbcdb2e96865da694ba1f49fcd391232b72664fd1b`.
- `CA-M-006@8`: `.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md`; SHA-256 `f34990465205ac3e655d83b1e3b5dcd66c8c93d2e5287cedbcb9dd38a432bd1f`.
- `CA-R-1490@1`: `.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md`; SHA-256 `af65fc105597d5966efaa59d663d452dfa7d0376ad9ebe7bb2b521077ccafb65`.
