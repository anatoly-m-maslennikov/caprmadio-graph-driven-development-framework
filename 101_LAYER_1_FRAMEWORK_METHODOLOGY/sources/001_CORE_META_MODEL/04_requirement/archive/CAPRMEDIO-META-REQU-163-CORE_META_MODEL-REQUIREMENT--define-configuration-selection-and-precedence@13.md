---
atom_id: CAPRMEDIO-META-REQU-163
cce_version: cce_1
cce_form: definition
subjects:
  governs:
    continuant:
      - Configuration Selection and Precedence
  depends_on:
    continuant:
      - Framework Instance Settings
      - Extension
      - Tool
version: 13
updated_at: 2026-09-07 09:59:57 +0000
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-R-1052
---
# Define Configuration selection and precedence

the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.
