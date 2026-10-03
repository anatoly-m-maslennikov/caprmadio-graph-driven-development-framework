---
atom_id: CA-D-376
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Project Settings/Atom Prefix/Carrier"
  depends_on:
    - "Project Settings"
    - "Atom"
    - "Operator"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-D-366"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize the Project Atom prefix

the Project Settings TOML Carrier **must** encode the Operator-selected Atom prefix in `artifacts.identity.project_prefix` **before** the first Project Atom is created.
