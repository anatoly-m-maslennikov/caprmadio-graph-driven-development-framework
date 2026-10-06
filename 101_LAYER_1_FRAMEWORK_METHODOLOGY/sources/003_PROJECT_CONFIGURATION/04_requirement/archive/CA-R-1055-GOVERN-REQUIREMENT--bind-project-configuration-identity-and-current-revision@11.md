---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Project Configuration/Revision Binding
version: 11
updated_at: 2026-08-30 19:30:26 +0400
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-661--register-project-configuration-atom-identity
    - CAPRMEDIO-GOV-REQU-771--admit-project-configuration-as-a-native-implementation-atom
---
# Bind Project Configuration identity and current revision

the Local Configuration **must** bind `CAPRMEDIO-I-001`, its current Revision, its SHA-256 Digest, **and** the canonical native Carrier locator `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/caprmedio_framework_settings.toml` in **=1** completed append-only Work Journal event under `.caprmedio_caprmedio/work_journal/`; absence, ambiguity, **or** mismatch leaves Project Configuration Atom currentness unknown.
