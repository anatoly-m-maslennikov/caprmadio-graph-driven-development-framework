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
      - Framework Instance Settings
      - Default Settings
version: 5
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - CA-D-359
  relates_to:
    - CA-M-279
    - CA-D-408
---
# Serialize Framework Settings Content in TOML

the Framework Instance Settings TOML Carrier **must** encode explicit Operator-selected instance choices through sections **and** fields specified by Standard-tier Atoms under its Core content **and** authority boundaries **and** applicable General settings specifications; it **must not** store Project initialization inputs **or** derived Project Structure as independently editable settings.
