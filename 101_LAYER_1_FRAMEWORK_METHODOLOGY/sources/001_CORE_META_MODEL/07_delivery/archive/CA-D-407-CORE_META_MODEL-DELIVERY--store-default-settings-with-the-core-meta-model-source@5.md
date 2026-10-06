---
subjects:
  governs: "Default Settings/Carrier"
  depends_on:
    - "Default Settings"
    - "File Carrier"
    - "Scope Unit"
    - "Methodology Source"
version: 5
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - "CA-R-1441"
---
# Store Default Settings with the Core Meta-Model source

the Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.
