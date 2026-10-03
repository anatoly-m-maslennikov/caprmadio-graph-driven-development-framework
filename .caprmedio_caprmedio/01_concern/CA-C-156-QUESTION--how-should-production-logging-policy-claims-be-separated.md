---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Logging Policy"
  depends_on:
    - "Journal"
    - "Artifact/Carrier"
    - "Atom/Content Role"
    - "Framework Instance Settings"
    - "Actor"
    - "Action"
priority: medium
version: 2
updated_at: "2026-09-17 18:36:51 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# How should production logging policy Claims be separated?

which independently governed R, M, E, D, **and** O Claims preserve the production Logging Policy **without** making it another Project Journal?

## Evidence

GOV-REQU-315 combines required event coverage, four severity meanings, actionable failures, aggregation, default-disabled DEBUG with bounded expiry, secret **and** sensitive-data handling, retention **and** sink behavior, monitoring, **and** the distinction from CAPRMEDIO Journals. D-396 already owns structured record fields. the Rationale still calls logs Operations records, while current O authority defines reusable behavior rather than emitted facts. D-320 separately protects non-reconstructible runtime history **without** making it governing authority.

## Principle check

CA-M-002 requires reuse of field, secret **and** Journal authority; CA-M-006 requires coherent Content Roles **and** data boundaries; CA-R-1490 protects valuable production evidence. the single Project Journal rule does **not** imply that a governed application's production log platform must be replaced by that Journal.

## Disposition

preserve all listed obligations until their unique owners, configuration values **and** actual execution responsibilities are mapped. do **not** drop sanitization, expiry, loss signals or failure handling during a role split; do **not** create a second canonical Project event log **or** classify emitted production facts as O definition Atoms. no logger, sink, retention value **or** native Tool is changed here.

## Inspected source Revisions

- `CAPRMEDIO-GOV-REQU-315` Version 13: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-315--require-production-logging-policies.md`; SHA-256 `1d657c7d6611bf2e08b5bc29320a7543464dd8adbae677b2794b51f2941ea420`.
- `CA-D-396` Version 5: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-396-PROJECT_CONFIGURATION-DELIVERY--serialize-structured-production-log-records.md`; SHA-256 `1799899a01c2127d9bb98df4ba64228f693ae3bdc17e95d2fb37e8603c42fb4a`.
- `CA-D-320` Version 9: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-320-DELIVERY--place-framework-engine-runtime-carriers.md`; SHA-256 `304b509e9175ed8014c9a61b9c51197e4f3c34711d3d29fd87c8e180c1cc8c48`.

## PROGRAMMATIC Method consumer

CA-M-163 additionally specifies timestamp, level, component, operation, outcome, **and** canonical action **or** event identity **when** available. CA-D-396 owns a broader applicable-field structure, but does **not** express the operation field **and** exact canonical-identity condition identically. removing M-163's field list as a duplicate would therefore risk losing a distinct obligation. preserve those fields **until** the exact Programmatic Delivery coverage is mapped; no new schema **or** Carrier is chosen by this Concern.

M-163 now separates reusable Operations behavior, Journal execution evidence, **and** production-log diagnostics under R-1344. this resolves the old O-record wording, **not** the remaining field/Method boundary.

## Additional inspected source Revisions

- `CA-M-163@10`: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-163-PROGRAMMATIC-CORE-METHOD--emit-structured-operational-diagnostics.md`; SHA-256 `2dc9bf4996ccb460d9e28b7da6f3e7c3c930d8a904009111b84c81f0917f5105`.
- `CA-D-396@5`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-396-PROJECT_CONFIGURATION-DELIVERY--serialize-structured-production-log-records.md`; SHA-256 `1799899a01c2127d9bb98df4ba64228f693ae3bdc17e95d2fb37e8603c42fb4a`.
- `CA-R-1344@10`: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1344-CORE_META_MODEL-CORE-REQUIREMENT--define-operations-content-role.md`; SHA-256 `300b0d772013aad37e26ec465f6b59279fe1f756d45643b5b91434d0d7020401`.
