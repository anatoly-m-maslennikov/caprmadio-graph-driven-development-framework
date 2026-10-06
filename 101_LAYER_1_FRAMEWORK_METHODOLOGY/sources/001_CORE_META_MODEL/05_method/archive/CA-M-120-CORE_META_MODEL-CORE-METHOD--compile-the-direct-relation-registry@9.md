---
atom_id: CA-M-120
subjects:
  governs:
    occurrent:
      - Relation Kind/registry compilation
  depends_on:
    continuant:
      - Relation Kind
      - Relation Kind/Metadata
      - CAPRMEDIO Graph
      - Applicable Methodology
      - Relation/authority
      - "Atom/Content Role: Requirement"
      - Projection
      - Generator
      - Relation
cce_version: cce_1
cce_form: method
version: 9
updated_at: "2026-09-11 05:04:26 +0400"
relations:
  child_of:
    - CA-R-295
    - CA-R-326
  method_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
---
# Compile the direct-relation registry

**to** compile the direct-relation registry, the Generator **must** perform **all** of:

1. derive the metadata required by CA-R-806 for **every** declared Relation Kind from its active governing Requirement authority. report missing **or** conflicting metadata **without** inventing a graph owner, meaning, endpoint class, **or** constraint.
2. group Relation Kinds by their owning kind of CAPRMEDIO Graph **and** resolve **every** lookup by graph kind **and** canonical name. reuse the same source authority across instances of the same graph kind governed by the same Applicable Methodology; do **not** merge registrations from different graph kinds because their names match.
3. derive inverse navigation from its declared owning direction **without** independently authoring an inverse Relation fact. preserve **`=1`** authoritative source declaration for **every** Relation fact represented **in** references **or** derived graph views.
4. retain source traceability for the compiled registry as a non-authoritative Projection. cross-graph references **or** views **must not** register a foreign Relation Kind as a native Relation Kind of the receiving graph.
