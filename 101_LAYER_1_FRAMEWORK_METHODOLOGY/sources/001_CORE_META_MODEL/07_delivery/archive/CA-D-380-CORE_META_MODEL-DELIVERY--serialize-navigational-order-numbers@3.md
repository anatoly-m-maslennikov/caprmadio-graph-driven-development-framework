---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Navigational Order Number"
  depends_on:
    - "Carrier"
    - "Scope Unit"
    - "Project Structure"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Navigational Order Numbers

**every** Carrier rendering of a Navigational Order Number **must** use decimal digits. the default directory-name rendering of a non-Project Scope Unit **must** use **`>=2`** digits; a typed TOML integer stores the numeric value **without** leading-zero padding.
