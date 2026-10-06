---
atom_id: CA-D-377
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    continuant:
      - "Framework Instance Settings"
      - "Atom"
      - "Artifact/Revision"
version: 1
updated_at: "2026-09-09 23:04:14 +0400"
relations:
  child_of:
    - "CA-D-361"
---
# Exclude Atom metadata from Framework Instance Settings

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.
