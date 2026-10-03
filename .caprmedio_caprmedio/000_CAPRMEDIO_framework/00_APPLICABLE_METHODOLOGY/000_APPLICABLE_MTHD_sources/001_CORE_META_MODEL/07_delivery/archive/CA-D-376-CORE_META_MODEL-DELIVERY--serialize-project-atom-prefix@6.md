---
subjects:
  governs: "Project Settings/Atom Prefix/Carrier"
  depends_on:
    - "Project Settings"
    - "Atom"
    - "Operator"
version: 6
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-366"
---
# Serialize the Project Atom prefix

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix **in** `artifacts.identity.project_prefix` **before** the first Project Atom is created.
