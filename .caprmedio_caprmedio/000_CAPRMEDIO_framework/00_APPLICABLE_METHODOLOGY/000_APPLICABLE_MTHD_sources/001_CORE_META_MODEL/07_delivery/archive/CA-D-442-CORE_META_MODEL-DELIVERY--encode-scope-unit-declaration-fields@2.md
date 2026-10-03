---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Scope Unit/Name"
    - "Scope Unit/Type"
    - "Scope Unit/Label"
    - "Scope Unit/Local Order"
    - "Navigational Order Number"
    - "Framework Instance Settings"
    - "Carrier"
version: 2
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-D-441"
  relates_to:
    - "CA-R-1484"
    - "CA-R-1485"
    - "CA-R-976"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Encode Scope Unit declaration fields

**every** `[[scope_units]]` table **must** use the following field signatures **and** field order for readable serialization. omission is permitted **only** where stated; an empty string **or** copied default **must not** substitute for omission.

| Field | TOML value **and** responsibility |
|---|---|
| `scope_unit_name` | required nonempty canonical Scope Unit Name string |
| `parent` | required string: `PROJECT` for the owning root, **otherwise** a declared Scope Unit Name **in** the same Project |
| `scope_unit_type` | required string **in** (`Ordered`, `Unordered`) |
| `scope_unit_label` | required nonempty canonical Label string, independent of Type |
| `structural_level` | required integer equal **to** declared parent depth from Project level 0 |
| `local_order` | required integer **only** for Ordered units; absent for Unordered units |
| `navigational_order_number` | required nonnegative integer, independent of structural Local Order |
| `authority_path` | required nonempty repository-relative directory path string |
| `delivery_path` | required nonempty repository-relative Implementation Folder path string |
| `authority_mode` | optional explicit string **in** (`strict`, `casual`); absence inherits Framework Instance Settings |

both path fields use forward slashes **and** resolve from the repository root, **not** the TOML directory; a trailing slash does **not** establish another binding. absolute paths, parent traversal, escaping symlinks **and** paths resolving **to** another Project's control root are invalid. a native Carrier binding under admitted Delivery authority **may** differ from ordinary physical nesting. `node_id`, `structural_parent`, `child_composition`, `project_boundary_position`, `authority_materialized`, **and** `numeric_prefix` are **not** authored row fields.
