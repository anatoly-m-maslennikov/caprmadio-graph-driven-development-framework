---
atom_id: CA-R-1454
cce_version: cce_1
cce_form: obligation
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
version: 2
updated_at: "2026-09-13 13:05:58 +0400"
relations:
  child_of:
    - CA-R-1335
    - CA-R-1319
    - CA-R-1437
---
# Derive governed Terms views from selected authority

for a requested source selection, a governed-only view of the Terms Graph **must** include **only** the Governed Terms admitted under CA-R-1319 **and** CA-M-114 from Definition Atoms **in** that selection **and** the Relations explicitly declared by source Atoms **in** that selection whose endpoints are included **and** whose Relation Kind is admitted for the Terms Graph; it **must** include **every** such Term **and** Relation. **every** displayed node **and** edge **must** retain traceability **to** its exact source Claim **and** Artifact Revision. this selection reuses the Terms Graph under CA-R-1335 **and** the source Relation authority under CA-R-1437 **without** introducing another graph kind **or** independent vocabulary authority.

the view **may** be derived from an upstream Terms Graph Projection **when** the upstream selection **and** source evidence support the requested view. its upstream Projection identity **and** Revision **must** remain traceable **to** the exact Definition Atoms **and** source Relation declarations required by this Claim. the upstream Projection **must not** acquire defining authority **or** establish complete source coverage from an incomplete selection. distinct graph **and** separately identified filtered-view Projection instances retain their own identities while reusing the Terms Graph Type **and** its Relation Kind authority; a governed-only filter alone does **not** admit another Type.
