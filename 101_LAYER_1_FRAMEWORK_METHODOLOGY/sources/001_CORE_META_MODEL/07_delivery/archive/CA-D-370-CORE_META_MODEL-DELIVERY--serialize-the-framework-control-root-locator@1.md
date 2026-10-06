---
atom_id: CA-D-370
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/framework control-root locator"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Project"
      - "Directory Carrier"
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Serialize the framework control-root locator

the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving to the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.
