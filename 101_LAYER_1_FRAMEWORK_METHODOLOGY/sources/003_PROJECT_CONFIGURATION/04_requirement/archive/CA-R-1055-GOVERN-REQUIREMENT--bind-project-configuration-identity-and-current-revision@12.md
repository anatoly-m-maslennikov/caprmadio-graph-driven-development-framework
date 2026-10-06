---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Project Configuration/Revision Binding
version: 12
updated_at: 2026-08-30 19:55:31 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-661--register-project-configuration-atom-identity
    - CAPRMEDIO-GOV-REQU-771--admit-project-configuration-as-a-native-implementation-atom
---
# Bind Project Configuration identity and current revision

the Local Configuration **must** bind `CAPRMEDIO-I-001` to the canonical native Carrier locator `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/caprmedio_framework_settings.toml` through `CAPRMEDIO-GOV-REQU-661` **and** bind the current Revision **and** SHA-256 Digest to that Carrier through the canonical completed governed commit Work Journal receipt under `.caprmedio_caprmedio/work_journal/`; absence, ambiguity, **or** mismatch leaves Project Configuration Atom currentness unknown.
