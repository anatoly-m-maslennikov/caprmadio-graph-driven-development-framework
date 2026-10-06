---
atom_id: CA-D-445
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Project Structure"
    - "Carrier"
    - "Implementation Folder"
version: 1
updated_at: "2026-09-15 00:13:02 +0000"
relations:
  relates_to:
    - "CA-R-862"
    - "CA-R-1485"
    - "CA-D-297"
    - "CA-D-299"
    - "CA-D-442"
---
# Admit explicit Scope Unit Carrier bindings

an explicit Scope Unit authority **or** Implementation Folder binding **in** Project Structure **may** select a native directory layout instead of the default Scope Unit directory convention. the binding **must** remain unambiguous, inside authorized path boundaries, distinct from another unit's exact authority binding, **and** explicit about its owning unit. a selected native layout **must not** change declared parentage, Structural Level, Type, Local Order, **or** Name merely because its path has different nesting **or** numeric tokens. ordinary physical containment remains observable **without** becoming a second declaration of structural parentage.
