---
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Project Structure"
    - "Authority Mode"
    - "Project"
    - "Scope Unit"
version: 5
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize instance Authority Mode selections

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.
