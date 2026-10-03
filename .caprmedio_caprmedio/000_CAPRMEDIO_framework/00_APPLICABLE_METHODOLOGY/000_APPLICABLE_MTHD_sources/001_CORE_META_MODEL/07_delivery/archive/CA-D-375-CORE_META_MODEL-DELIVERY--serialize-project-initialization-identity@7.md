---
subjects:
  governs: "Project Settings/Project identity/Carrier"
  depends_on:
    - "Project Settings"
    - "Project"
    - "Project Name"
    - "Operator"
    - "Atom"
    - "Implementation"
version: 7
updated_at: "2026-09-11 15:22:56 +0400"
relations:
  child_of:
    - "CA-D-366"
---
# Serialize Project initialization identity

the Project Settings TOML Carrier **must** encode the Operator-selected Project Name as its exact lowercase value **in** `project.name`, **before** the first Project Atom **or** Implementation is created.
