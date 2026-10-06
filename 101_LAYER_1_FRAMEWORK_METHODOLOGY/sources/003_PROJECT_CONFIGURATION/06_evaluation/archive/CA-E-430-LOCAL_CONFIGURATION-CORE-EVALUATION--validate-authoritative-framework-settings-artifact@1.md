---
atom_id: CA-E-430
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Project Configuration Validation
  depends_on:
    continuant:
      - Project Configuration
      - Project Configuration/Authoritative Carrier
      - Project Configuration/Revision Binding
version: 1
updated_at: 2026-09-04 03:52:00 +0400
relations:
  evaluation_for:
    - CA-R-1400
    - CA-R-1401
    - CA-D-358
    - CA-D-359
    - CA-D-360
    - CA-D-361
---
# Validate Authoritative Framework Settings Artifact

the Evaluation **must** reject caprmedio_framework_settings **if** it is treated as an Atom, has an Atom ID **or** Atom Content Role, has other than **`=1`** authoritative TOML Carrier, resolves from another Carrier, **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-commit Work Journal receipt.
