---
subjects:
  governs: "Relation Kind/registry compilation"
  depends_on:
    - "Relation Kind"
    - "Relation Kind/Metadata"
    - "CAPRMEDIO Graph"
    - "Applicable Methodology"
    - "Relation/authority"
    - "Atom/Content Role: Requirement"
    - "Projection"
    - "Generator"
    - "Relation"
    - "Single Source of Truth"
version: 12
updated_at: "2026-09-15 01:47:49 +0400"
relations:
  child_of:
    - CA-R-295
    - CA-R-326
  method_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
    - CA-R-1472
---
# Compile the direct-relation registry

**to** compile the direct-relation registry, the Generator **must** perform **all** of:

1. derive the metadata required by CA-R-806 for **every** declared Relation Kind from its active governing Requirement authority. report missing **or** conflicting metadata **without** inventing a graph owner, meaning, endpoint class, **or** constraint.
2. group Relation Kinds by their owning kind of CAPRMEDIO Graph **and** resolve **every** lookup by graph kind **and** canonical name. reuse the same source authority across instances of the same graph kind governed by the same Applicable Methodology; do **not** merge registrations from different graph kinds because their names match.
3. derive inverse navigation from its declared owning direction **without** independently authoring an inverse Relation fact. distinguish **`=1`** authoritative declaration for an independently authored Relation fact from the governing derivation authority **and** input facts of a derived Relation under CA-R-1437; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the compiled registry as a non-authoritative Projection. resolve cross-graph **and** authoritative-source endpoints against their admitted graph contexts under CA-R-806 **and** CA-R-1472. cross-graph references **or** views **must not** register a foreign Relation Kind as native **or** reclassify an external endpoint as a native node of the receiving graph.
