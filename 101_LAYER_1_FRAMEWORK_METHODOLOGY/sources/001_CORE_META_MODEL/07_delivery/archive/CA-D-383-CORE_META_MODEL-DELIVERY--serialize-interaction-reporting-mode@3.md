---
atom_id: CA-D-383
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Authoritative Carrier/Content"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Operator"
      - "Framework Instance Settings/interaction/reporting mode"
version: 3
updated_at: "2026-09-11 18:18:55 +0400"
relations:
  child_of:
    - CA-D-361
  relates_to:
    - CAPRMEDIO-GOV-REQU-294
    - CAPRMEDIO-META-REQU-675
---
# Serialize Interaction Reporting Mode

the Framework Instance Settings TOML Carrier **must** serialize its Operator-selected instance reporting default as `reporting_mode` **in** the `[interaction]` section, using an allowed value governed by CAPRMEDIO-GOV-REQU-294.
