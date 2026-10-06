---
atom_id: CA-D-375
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Project Settings/Project identity/Carrier"
  depends_on:
    - "Project Settings"
    - "Project"
    - "Project Name"
    - "Operator"
    - "Atom"
    - "Implementation"
version: 3
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-D-366"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Project initialization identity

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact lowercase value in `project.name`, **before** the first Project Atom **or** Implementation is created.
