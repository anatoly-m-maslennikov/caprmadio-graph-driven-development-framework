---
subjects:
  governs: "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    - "Framework Instance Settings"
    - "Atom"
    - "Artifact/Revision"
version: 5
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Exclude Atom metadata from Framework Instance Settings

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
