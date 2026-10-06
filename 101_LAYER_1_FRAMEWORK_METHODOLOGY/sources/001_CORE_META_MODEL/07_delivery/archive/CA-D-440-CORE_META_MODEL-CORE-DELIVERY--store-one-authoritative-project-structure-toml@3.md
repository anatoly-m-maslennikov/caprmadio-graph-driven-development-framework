---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Project Settings"
    - "Carrier"
    - "Scope Unit"
version: 3
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-862"
---
# Store one authoritative Project Structure TOML

the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.
