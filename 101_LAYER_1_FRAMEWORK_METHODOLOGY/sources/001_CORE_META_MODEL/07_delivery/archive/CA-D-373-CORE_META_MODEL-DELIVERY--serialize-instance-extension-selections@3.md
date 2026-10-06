---
atom_id: CA-D-373
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Framework Instance Settings/Extension selections"
  depends_on:
    - "Framework Instance Settings"
    - "Extension"
version: 3
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize instance Extension selections

the Framework Instance Settings TOML Carrier **must** encode enabled **or** disabled Extensions with selected revisions **when** applicable **and** retained per-Extension settings; retained settings **must not** activate a disabled Extension.
