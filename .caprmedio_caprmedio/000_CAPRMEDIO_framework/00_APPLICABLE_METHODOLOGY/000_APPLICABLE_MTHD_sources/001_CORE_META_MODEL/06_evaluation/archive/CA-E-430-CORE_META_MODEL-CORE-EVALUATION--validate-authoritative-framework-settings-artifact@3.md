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
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  evaluation_for:
    - CA-R-1402
    - CA-R-1430
    - CA-R-1429
    - CA-D-317
    - CA-D-358
    - CA-D-359
    - CA-D-360
    - CA-D-361
---
# Validate Authoritative Framework Settings Artifact

the Evaluation **must** reject Framework Instance Settings **if** it is treated as an Atom **or** Projection, has an Atom ID **or** Atom Content Role, resolves outside the current Project's registered instance directory, uses another Project's Settings Carrier, has other than **`=1`** authoritative TOML Carrier, contains Project initialization inputs **or** independently editable Project Structure, violates its Core content boundary **or** applicable Standard field specifications, **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-commit Work Journal receipt.
