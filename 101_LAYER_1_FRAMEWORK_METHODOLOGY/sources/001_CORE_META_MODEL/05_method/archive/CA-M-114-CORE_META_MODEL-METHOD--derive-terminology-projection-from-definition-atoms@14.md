---
atom_id: CA-M-114
subjects:
  governs: "Terminology Projection Derivation"
  depends_on:
    - "Projection/Type: Catalog"
    - "Generator"
    - "Definition Atom"
    - "Governed Term"
    - "Project"
    - "Atom/Claim"
    - "Subject"
    - "Subject Path"
    - "Entity"
    - "Term"
cce_version: cce_1
cce_form: method
version: 14
updated_at: "2026-09-13 14:15:09 +0400"
relations: {}
---
# Derive Terminology Projection from Definition Atoms

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. obtain the name from the terminal Term **in** the GOVERNS Subject Path that references the defined Subject. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone is insufficient. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.
