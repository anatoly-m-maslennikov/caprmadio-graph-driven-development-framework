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
version: 14
updated_at: "2026-10-02 20:25:13 +0400"
relations:
  child_of:
    - CA-R-295
    - CA-R-326
  method_for:
    - CA-R-806
    - CA-R-1246
    - CA-R-1437
    - CA-R-1472
atom_id: "CA-M-120"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-120-CORE_META_MODEL-CORE--compile-the-direct-relation-registry.md
  source_atom_id: CA-M-120
  source_atom_revision: 14
  source_sha256: 4f1a2004c885b1134ef57e309c37e1ab14c86bf008a3374fc93bbc20a2c104db
  original_relations_sha256: 0ee5848e38173afc3aa73f55b419962fa9b6f19cedd32210873fd1d71efaa5fa
---
# Summary

Compile the direct-relation registry

## Scope

direct-relation registry compilation.

## Claim

**to** compile the direct-relation registry, the Generator **must** perform **all** of:

1. derive the metadata required by CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata for **every** declared Relation Kind from its active governing Requirement authority. report missing **or** conflicting metadata **without** inventing a graph owner, meaning, endpoint class, **or** constraint.
2. group Relation Kinds by their owning kind of CAPRMEDIO Graph **and** resolve **every** lookup by graph kind **and** canonical name. reuse the same source authority across instances of the same graph kind governed by the same Applicable Methodology; do **not** merge registrations from different graph kinds because their names match.
3. derive inverse navigation from its declared owning direction **without** independently authoring an inverse Relation fact. distinguish **`=1`** authoritative declaration for an independently authored Relation fact from the governing derivation authority **and** input facts of a derived Relation under CA-R-1437-CORE_META_MODEL-CORE-REQUIREMENT--keep-one-source-for-each-relation-fact; do **not** invent a direct source declaration for a computed result.
4. retain source traceability for the compiled registry as a non-authoritative Projection. resolve cross-graph **and** authoritative-source endpoints against their admitted graph contexts under CA-R-806-CORE_META_MODEL-GENERAL-REQUIREMENT--register-complete-relation-kind-metadata **and** CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections. cross-graph references **or** views **must not** register a foreign Relation Kind as native **or** reclassify an external endpoint as a native node of the receiving graph.

## Details
