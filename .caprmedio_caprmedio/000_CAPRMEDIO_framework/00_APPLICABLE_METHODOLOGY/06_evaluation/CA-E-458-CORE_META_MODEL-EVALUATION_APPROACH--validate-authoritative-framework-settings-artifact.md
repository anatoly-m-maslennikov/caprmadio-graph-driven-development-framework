---
subjects:
  governs: "Framework Instance Settings Validation"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Framework Instance Settings/Authoritative Carrier"
    - "Framework Instance Settings/Revision Binding"
version: 16
updated_at: "2026-10-01 21:31:46 +0400"
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
atom_id: "CA-E-458"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-458-CORE_META_MODEL-EVALUATION_APPROACH--validate-authoritative-framework-settings-artifact.md
  source_atom_id: CA-E-458
  source_atom_revision: 16
  source_sha256: b66034350426c662eb4f4de967ed29a5ee4c905f2383b530e6336b95c6b1cc4c
  original_relations_sha256: c43710a24ba9609df14ffa1948ef1b7800e193bfc80ab2f310b1715a02cb8616
---
# Summary

Validate Authoritative Framework Settings Artifact

## Scope

Framework Instance Settings.

## Claim

the Evaluation **must** reject Framework Instance Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- resolves outside the current Project's registered instance directory,
- uses another Project's Settings Carrier,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Project initialization inputs **or** independently editable Project Structure,
- violates its Core content boundary, applicable General settings specifications, **or** applicable Standard field specifications **after** parameter resolution governed by CA-M-279,
- **or** lacks an exact current Revision, SHA-256 Digest, **and** governed-change Work Journal receipt.

## Details
