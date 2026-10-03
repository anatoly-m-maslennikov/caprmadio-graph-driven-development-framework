---
atom_id: CA-D-408
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Default Settings/Carrier/Content"
  depends_on:
    - "Default Settings"
    - "Framework Instance Settings"
    - "Carrier"
version: 3
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - "CA-D-407"
  relates_to:
    - "CA-D-361"
    - "CA-D-368"
    - "CA-D-369"
    - "CA-D-374"
    - "CA-D-383"
    - "CA-D-387"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reuse framework parameter fields in Default Settings

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.
