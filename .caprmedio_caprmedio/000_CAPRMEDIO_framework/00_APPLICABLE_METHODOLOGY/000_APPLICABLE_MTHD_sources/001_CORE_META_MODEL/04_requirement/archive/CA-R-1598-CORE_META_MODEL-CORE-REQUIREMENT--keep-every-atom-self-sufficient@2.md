---
subjects:
  governs: "Atom"
  depends_on:
    - "Atom/Property"
    - "Atom/Claim"
    - "Atom/Revision"
    - "Atom/Carrier"
    - "Relation"
    - "Single Source of Truth"
version: 2
updated_at: "2026-09-22 23:02:20 +0000"
relations: {"relates_to": ["CA-R-117", "CA-R-118", "CA-R-1470"]}
---
# Summary

Keep every Atom self-sufficient

## Claim

**every** Atom Revision **must** carry its applicable Properties within its own Markdown Carrier so that its own declared content can be read **without** reconstructing it from a filename **or** directory placement.

- the applicable model determines which Properties are required, optional, **or** inapplicable; self-sufficiency does **not** invent missing Properties **or** permit an invalid value.
- a Relation **to** another Atom remains declared **only** on its registered owning endpoint; the other endpoint **and** inverse views are resolved from that declaration, **not** independently copied.
- self-sufficiency does **not** require copying the referenced Atom, governing model, **or** inherited Settings authority into this Atom.
