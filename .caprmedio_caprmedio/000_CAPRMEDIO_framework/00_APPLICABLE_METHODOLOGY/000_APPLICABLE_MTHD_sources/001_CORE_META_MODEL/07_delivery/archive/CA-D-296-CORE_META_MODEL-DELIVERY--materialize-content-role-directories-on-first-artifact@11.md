---
subjects:
  governs: "Artifact/Carrier Placement"
  depends_on:
    - "Atom/Content Role"
    - "Scope Unit"
    - "Artifact"
    - "Directory Carrier"
version: 11
updated_at: "2026-09-17 12:25:48 +0000"
relations: {}
---
# Materialize Content Role Directories on First Artifact

a Scope Unit's administrative Content Role directory **must** be materialized for canonical Artifact placement **only** **when** the first current Artifact requires that placement.

an absent Content Role directory **must** represent empty role placement, **not** an absent Scope Unit. this administrative directory does **not** itself carry a Structural Entity **or** become a Directory Carrier under CA-D-451. this materialization condition does **not** require deletion of an existing empty directory.
