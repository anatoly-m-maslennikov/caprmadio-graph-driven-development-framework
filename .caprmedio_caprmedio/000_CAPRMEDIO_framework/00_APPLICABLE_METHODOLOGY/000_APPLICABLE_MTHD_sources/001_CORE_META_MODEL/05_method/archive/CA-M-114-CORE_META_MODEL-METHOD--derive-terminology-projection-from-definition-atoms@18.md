---
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
    - "Action"
    - "Workflow"
version: 18
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
---
# Derive Terminology Projection from Definition Atoms

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. read the Term named by the defining Claim **and** verify that the Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279. extract Term references from **every** named component of a Subject Path, **not** **only** its terminal component; obtain **every** referenced Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** supply defining authority. an unresolved named component is a Term-reference gap **to** report, **not** permission **to** invent a definition **or** silently treat that component as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.
