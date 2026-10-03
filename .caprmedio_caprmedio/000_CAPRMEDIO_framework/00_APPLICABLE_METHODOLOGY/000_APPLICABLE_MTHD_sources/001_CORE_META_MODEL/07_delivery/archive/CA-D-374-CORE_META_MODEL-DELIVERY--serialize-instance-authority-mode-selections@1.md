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
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize instance Authority Mode selections

the Framework Instance Settings TOML Carrier **must** encode the Authority Mode default **and** optional explicit Project **or** Scope Unit overrides under `authority_modes`; current values **must not** be encoded as Project Settings selections.
