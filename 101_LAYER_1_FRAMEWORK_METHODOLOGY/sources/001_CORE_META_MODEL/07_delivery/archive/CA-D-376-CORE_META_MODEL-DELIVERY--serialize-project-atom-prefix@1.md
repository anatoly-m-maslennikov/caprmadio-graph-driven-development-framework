---
atom_id: CA-D-376
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Project Settings/Atom Prefix/Carrier"
  depends_on:
    continuant:
      - "Project Settings"
      - "Atom"
      - "Operator"
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-366"
---
# Serialize the Project Atom prefix

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix in `artifacts.identity.project_prefix` **before** the first Project Atom is created.
