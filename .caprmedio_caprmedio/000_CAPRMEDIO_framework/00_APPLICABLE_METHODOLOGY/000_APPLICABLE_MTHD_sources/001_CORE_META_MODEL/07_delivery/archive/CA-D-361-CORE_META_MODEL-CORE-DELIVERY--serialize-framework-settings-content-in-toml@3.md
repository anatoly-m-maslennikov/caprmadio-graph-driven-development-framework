---
atom_id: CA-D-361
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Authoritative Carrier/Content
  depends_on:
    continuant:
      - Tool
      - Extension
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - CA-D-359
---
# Serialize Framework Settings Content in TOML

the Framework Instance Settings TOML Carrier **must** encode Operator-editable instance choices through sections **and** fields specified by Standard-tier Atoms under its content boundary; it **must not** store Project initialization inputs **or** derived Project Structure as independently editable settings.
