---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Framework Instance Settings Validation"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Framework Instance Settings/Authoritative Carrier"
    - "Framework Instance Settings/Revision Binding"
version: 12
updated_at: "2026-09-14 06:21:07 +0400"
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
    - CA-R-1441
    - CA-M-279
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate Authoritative Framework Settings Artifact

the Evaluation **must** reject Framework Instance Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- resolves outside the current Project's registered instance directory,
- uses another Project's Settings Carrier,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Project initialization inputs **or** independently editable Project Structure,
- violates its Core content boundary, applicable General settings specifications, **or** applicable Standard field specifications **after** parameter resolution governed by CA-M-279,
- **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-change Work Journal receipt.
