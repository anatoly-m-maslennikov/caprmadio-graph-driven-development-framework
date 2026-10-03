---
atom_id: CA-P-114
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Bootstrap Carrier Structure
    occurrent:
      - Bootstrap Structure Retirement
  depends_on:
    occurrent:
      - CA-P-113
version: 2
updated_at: 2026-09-03 14:57:33 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Retire Mapped Obsolete Bootstrap Structures

**when** CA-P-113 is Done, **then** the Assignee **must** retire the obsolete Bootstrap root and alternative delivery-directory shells after moving every retained Bootstrap Carrier to its exact reconciled successor.

## Scope

`((all current Carriers in .caprmedio) union (the legacy root delivery directories 001_FRAMEWORK_METHODOLOGY, 002_FRAMEWORK_ENGINE, 003_OPERATOR_DOCUMENTATION, 004_CORE_EXTENSIONS, 005_RELEASES, 010_COMMUNITY_EXTENSIONS, and 010_FIELD) union (the verified-empty _rename_probe directories) union (the corresponding CA-P-108 map rows and successor Carriers))`

## Definition of Done

the Task is **not done if** (CA-P-113 is not Done with passing evidence **or** any retained `.caprmedio` Carrier lacks one exact reconciled successor and matching digest **or** a Bootstrap-history Carrier is absent from `.caprmedio_bseed` **or** a legacy FPF report is absent from `fpf-reports` **or** a Project Analysis Carrier is absent from `.caprmedio_caprmedio/02_analysis` **or** any retired legacy root contains a governed Carrier **or** any removed or relocated Carrier lacks a pre-retirement digest and successor verification **or** any archive, Journal, Plan, FPF report, migration map, source manifest, rollback record, or execution evidence is lost or changed unexpectedly **or** `.caprmedio_install` or `.caprmedio_runtime` is deleted, moved, or treated as Bootstrap authority **or** an empty-directory removal is claimed without immediate emptiness verification **or** a macOS-blocked empty-directory residue lacks its exact recorded path and removal error **or** rollback cannot restore the pre-retirement Carrier paths from the evidence record).

## Details

the latest topology supersedes the CA-P-108 `OUT_OF_SCOPE_RETAIN_IN_PLACE` disposition for the remaining `.caprmedio` Bootstrap root. reconcile that disposition as follows before retirement:

- move `.caprmedio/-100_BSEED_SUPERLAYER_META_METHODOLOGY` byte-preservingly to `.caprmedio_bseed/-100_BSEED_SUPERLAYER_META_METHODOLOGY` as Bootstrap history;
- move `.caprmedio/fpf-reports` byte-preservingly to the existing root `fpf-reports` evidence directory;
- move the two current `.caprmedio/02_analysis` Carriers byte-preservingly to `.caprmedio_caprmedio/02_analysis`;
- retain `.caprmedio_install` and `.caprmedio_runtime` in place; and
- remove only source directories that contain no governed Carriers immediately before removal. record exact macOS-blocked empty directory paths as local residue rather than bypassing the protection.

the existing CA-P-108 map, source manifest, migration result, rollback record, and all earlier evidence remain immutable historical records. this Task supplies the exact current reconciliation and retirement evidence; it does not reinterpret old historical Claims as current authority.
