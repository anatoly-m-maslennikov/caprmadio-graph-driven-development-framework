---
atom_id: CA-D-374
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Authority Modes/Carrier"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Project Settings"
      - "Authority Mode"
      - "Project"
      - "Scope Unit"
version: 2
updated_at: "2026-09-11 19:51:42 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize instance Authority Mode selections

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** the registered target-specific field under `authority_modes` for a Project **or** Scope Unit override, **not** a Project Settings field.
