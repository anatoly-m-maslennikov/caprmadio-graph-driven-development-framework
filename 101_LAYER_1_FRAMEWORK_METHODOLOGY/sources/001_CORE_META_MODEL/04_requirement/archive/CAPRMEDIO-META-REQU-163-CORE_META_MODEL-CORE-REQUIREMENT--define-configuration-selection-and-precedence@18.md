---
subjects:
  governs: "Configuration Selection and Precedence"
  depends_on:
    - "Framework Instance Settings"
    - "Extension"
    - "Tool"
version: 18
updated_at: "2026-09-10 04:26:29 +0400"
relations: {}
---
# Define Configuration selection and precedence

the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.
