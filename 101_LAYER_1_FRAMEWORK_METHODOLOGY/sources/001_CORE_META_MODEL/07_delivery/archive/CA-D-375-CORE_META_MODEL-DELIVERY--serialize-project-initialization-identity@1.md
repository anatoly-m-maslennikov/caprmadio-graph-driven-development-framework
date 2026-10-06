---
atom_id: CA-D-375
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Project Settings/Project identity/Carrier"
  depends_on:
    continuant:
      - "Project Settings"
      - "Project"
      - "Atom"
      - "Implementation"
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-366"
---
# Serialize Project initialization identity

the Project Settings TOML Carrier **must** encode the Project's initialization identity, including its exact lowercase name in `project.name`, **before** the first Project Atom **or** Implementation is created.
