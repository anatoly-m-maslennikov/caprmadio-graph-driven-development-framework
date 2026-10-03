---
atom_id: CA-D-393
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Type"
  depends_on:
    - "Atom/Content Role"
    - "Carrier"
version: 3
updated_at: "2026-09-10 20:55:13 +0400"
relations:
  child_of:
    - "CAPRMEDIO-META-REQU-100"
    - "CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type"
    - "CAPRMEDIO-META-REQU-742--permit-one-internal-default-type-per-content-role"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive default external Type names

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
