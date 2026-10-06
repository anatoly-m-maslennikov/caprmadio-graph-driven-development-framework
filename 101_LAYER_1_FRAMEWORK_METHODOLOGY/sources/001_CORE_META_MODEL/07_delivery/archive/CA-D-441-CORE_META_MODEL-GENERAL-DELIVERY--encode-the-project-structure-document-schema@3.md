---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Scope Unit"
    - "Carrier"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-D-440"
---
# Encode the Project Structure document schema

the Project Structure TOML document **must** contain the integer `schema_version = 1` **and** one `scope_units` array of tables, with **`>=0`** rows for declared non-Project Scope Units. an empty array **must** use `scope_units = []`; nonempty arrays use `[[scope_units]]`. the root Project is implicit from Project Settings **and** **must not** have a duplicate row. unknown top-level keys, unknown row keys, duplicate TOML keys, **and** unsupported schema versions **must** be rejected rather than ignored. document comments **may** explain authority **and** retained readability fields, **without** introducing additional authoritative fields.
