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
version: 1
updated_at: "2026-09-10 20:54:14 +0400"
relations: {}
---
# Serialize Interaction Reporting Mode

the Framework Instance Settings TOML Carrier **must** serialize its interaction reporting setting as `reporting_mode` **in** the `[interaction]` section, using the allowed value **and** default governed by CAPRMEDIO-GOV-REQU-294.
