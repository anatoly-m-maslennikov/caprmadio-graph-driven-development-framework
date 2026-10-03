---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Project"
    - "Operator"
priority: medium
version: 1
updated_at: "2026-09-22 17:04:17 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should the Local App runtime draft be reconciled?

how should the identified Draft Atom be reconciled **with** active authority **and** Project Principles **without** losing useful information **or** promoting it?

## Draft under review

- Carrier: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/07_delivery/drafts/CA-D--DELIVERY-FR_ENGN_APPS--provide-a-separated-local-app-runtime.md`.
- inspected SHA-256: `a88d36d5ded0a4694c9ca22b2724f929fbe72c0243ce1b0f87d834dd8f6c120b`.
- review point: 74 of 79; campaign `draft-review-8afeac79`.

## Prior review finding

> **Revise/split** — Keep App carrier/state placement; separate lifecycle, security and keyboard behavior, already checked by active QA.
>
> Basis: `CA-E-349`, `CA-E-350`, `CA-E-351`, `CA-E-352`, `CA-M-313`; I7,I8. Reviewer confidence: 99%.

## Active authority cited by the review

- `CA-E-349@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-349-APPS-QA_CASE--operate-the-primary-app-workflow-by-keyboard.md`; SHA-256 `1493f38ff2510eacd49b23139fde733fb5535366daa54c27ff4cccb12fe2db2e`.
- `CA-E-350@6`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-350-APPS-QA_CASE--reject-interface-bypass-of-governed-doers.md`; SHA-256 `db85aacac5b372168197bf2bac551912f11bb3ce5753a898fa671893eb5fc6c6`.
- `CA-E-351@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-351-APPS-QA_CASE--render-untrusted-project-content-only-as-data.md`; SHA-256 `a44f395e5ef67aad56284b49b56d87e41bdeea0cadb1e167b0b2dfc88e02c058`.
- `CA-E-352@5`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS/06_evaluation/CA-E-352-APPS-QA_CASE--restore-app-service-state-after-restart.md`; SHA-256 `8db521ebe28b76495d638a72658f4408c0de11cd50699e7532073e8ac1733c3d`.
- `CA-M-313@1`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-313-CORE_META_MODEL-METHOD--write-delivery-claims-with-the-delivery-cce-profile.md`; SHA-256 `2f7e6adc52588ea7b0be005b3fa0caf446fe814e64a6514ab8227bc8ee1d8fec`.

## Principles to apply

- [CA-M-002](.caprmedio_caprmedio/05_method/CA-M-002-PRINCIPLE-METHOD--dry-don-t-repeat-yourself.md).
- [CA-M-005](.caprmedio_caprmedio/05_method/CA-M-005-PRINCIPLE-METHOD--add-complexity-only-when-necessary.md).
- [CA-M-006](.caprmedio_caprmedio/05_method/CA-M-006-PRINCIPLE-METHOD--keep-the-whole-project-coherent.md).
- [CA-R-1490](.caprmedio_caprmedio/04_requirement/CA-R-1490-PRINCIPLE-REQUIREMENT--preserve-valuable-information.md).
- [CA-E-001](.caprmedio_caprmedio/06_evaluation/CA-E-001-PRINCIPLE-EVALUATION--make-governed-commitments-and-results-checkable.md).

## Resolution

not yet individually resolved. the quoted recommendation remains a proposal; its confidence is **not** a completed repair decision. review this point **in** the recorded sequence, using active Principles **and** current authority. ask the Operator **if** confidence remains below 99%; keep any repaired source **in** Draft.
