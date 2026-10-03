---
atom_id: CA-E-431
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Project Settings Validation
  depends_on:
    continuant:
      - Project Settings
      - Project Settings/Authoritative Carrier
      - Project Settings/Revision Binding
version: 1
updated_at: 2026-09-04 04:05:44 +0400
relations:
  evaluation_for:
    - CAPRMEDIO-META-REQU-619
    - CA-R-1400
    - CA-R-1401
    - CA-D-362
    - CA-D-363
    - CA-D-364
    - CA-D-365
    - CA-D-366
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/06_evaluation/CA-E-431-LOCAL_CONFIGURATION-CORE-EVALUATION--validate-authoritative-project-settings-artifact.md
---
# Validate Authoritative Project Settings Artifact

the Evaluation **must** reject Project Settings **if** the Artifact is treated as an Atom **or** Projection, has an Atom ID **or** Atom Content Role, violates the project-specific filename grammar, has other than **`=1`** authoritative TOML Carrier, contains a Framework Instance setting, **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-commit Work Journal receipt.
