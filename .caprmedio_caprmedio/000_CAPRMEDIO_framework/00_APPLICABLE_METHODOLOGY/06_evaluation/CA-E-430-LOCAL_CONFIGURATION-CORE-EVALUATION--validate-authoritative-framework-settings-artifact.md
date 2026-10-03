---
atom_id: CA-E-430
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Framework Instance Settings Validation
  depends_on:
    continuant:
      - Framework Instance Settings
      - Framework Instance Settings/Authoritative Carrier
      - Framework Instance Settings/Revision Binding
version: 2
updated_at: 2026-09-04 04:05:44 +0400
relations:
  evaluation_for:
    - CA-R-1402
    - CA-R-1403
    - CA-R-1404
    - CA-D-358
    - CA-D-359
    - CA-D-360
    - CA-D-361
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/06_evaluation/CA-E-430-LOCAL_CONFIGURATION-CORE-EVALUATION--validate-authoritative-framework-settings-artifact.md
---
# Validate Authoritative Framework Settings Artifact

the Evaluation **must** reject caprmedio_framework_settings **if** it is treated as an Atom, has an Atom ID **or** Atom Content Role, has other than **`=1`** authoritative TOML Carrier, resolves from another Carrier, contains a Project setting, **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-commit Work Journal receipt.
