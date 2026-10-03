---
atom_id: CA-P-110
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Applicable Methodology
    occurrent:
      - Applicable Methodology Compilation
  depends_on:
    occurrent:
      - CA-P-109
version: 4
updated_at: 2026-08-26 17:42:48 +0400
autonomous_confidence_threshold: 98
relations: {}
---
# Compile the First Applicable Methodology

**when** CA-P-109 is Done, **then** the Assignee **must** compile the first final-carrier Applicable Methodology from the exact migrated authoritative source frontier.

## Scope

`((the migrated CORE_META_MODEL Carriers) union (the exact INSTALLED_EXTENSIONS selected and resolved by LOCAL_CONFIGURATION) union (the migrated LOCAL_CONFIGURATION Carriers) union (the CA-P-107 compiler authority and implementation) union (the predicted and generated Applicable Methodology Carriers))`

## Definition of Done

the Task is **not done if** (the first Applicable Methodology output is not compiled from CORE_META_MODEL plus exactly the Installed Extensions selected and resolved by LOCAL_CONFIGURATION **or** its ordered source frontier differs from the CA-P-108 prediction **or** its source and output digests do not match the migrated authoritative frontier **or** an installed but inactive, replaced, incompatible, or lower-priority Extension contributes **or** any source Carrier changes **or** 000_APPLICABLE_MTHD_sources changes **or** generated Applicable Methodology is treated as editable source or independent authority **or** the same source frontier produces different ordered output **or** deleting the generated output prevents complete regeneration).

## Details

execute the CA-P-107 compilation contract against the migrated source Layers and materialize only the predicted final generated Carriers. keep Core Meta-Model, installed Extension authority, and Local Configuration authoritative within their accepted source directories. keep the compiled Applicable Methodology mechanical, non-authoritative, and reproducible. defer every consumer rewrite and representative retrieval test to CA-P-113.
