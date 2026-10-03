---
subjects:
  governs: "Projection/Type: Terms Graph"
  depends_on:
    - "Governed Term"
    - "Term"
    - "Definition Atom"
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Relation"
    - "Relation Kind"
    - "Projection"
version: 5
updated_at: "2026-09-15 01:47:49 +0400"
relations:
  child_of:
    - CA-R-1335
    - CA-R-1319
    - CA-R-1437
---
# Derive governed Terms views from selected authority

for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319 **and** CA-M-114 from Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Kind is admitted for the Terms Graph; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335 **and** the source Relation authority under CA-R-1437 **without** introducing another graph kind **or** independent vocabulary authority.

the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** its Relation Kind authority; a governed-only filter alone does **not** admit another Type.

these node **and** internal-Relation selection rules do **not** require importing the endpoints of separately admitted external references as native graph members. **if** the view includes cross-graph **or** source references under CA-R-1472, it **must** keep them distinguishable from its native node **and** internal-Relation selection **and** preserve their admitted endpoint classes, graph-qualified Relation authority, **and** source traceability. such references **must not** silently enlarge the selected native graph **or** bypass an explicit source-declaration requirement for its internal Relations.
