---
atom_id: CA-D-398
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Revision/Frontmatter"
  depends_on:
    continuant:
      - "Atom/Claim"
      - "Project Scope Unit Graph Projection"
      - "Project Settings"
      - "Framework Instance Settings"
version: 3
updated_at: "2026-09-11 23:47:49 +0400"
relations:
  child_of:
    - "CA-D-311"
    - "CAPRMEDIO-META-REQU-675"
---
# Encode configuration surfaces in owning Atoms

an owning Atom **may** carry its optional machine-readable contribution **to** the generated Project Scope Unit Graph under one top-level `project_scope_unit_graph` **or** `project_graph_state` YAML map **only** **when** it faithfully represents that Atom's own governed Claim. it **may** declare registered facts, allowed values, defaults, **or** structural contributions, but **must not** encode current Operator-selected Project identity, Atom prefix, Authority Mode values, **or** a `project_settings` contribution; Project initialization selections belong **only** **to** Project Settings, **and** Authority Mode selections belong **only** **to** Framework Instance Settings.
