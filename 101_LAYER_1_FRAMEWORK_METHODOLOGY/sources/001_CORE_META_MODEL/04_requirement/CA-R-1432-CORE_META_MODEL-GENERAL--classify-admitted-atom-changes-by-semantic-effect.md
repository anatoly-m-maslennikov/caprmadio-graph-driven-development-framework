---
subjects:
  governs: "Atom Change Classification"
  depends_on:
    - "Atom"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Carrier-Only Recoding"
    - "Lineage Impact Analysis"
    - "Tool"
version: 9
updated_at: "2026-10-02 22:59:46 +0400"
relations: {}
atom_id: "CA-R-1432"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Classify admitted Atom changes by semantic effect

## Scope

the classification of admitted Atom changes by semantic effect.

## Claim

**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, filename, path, encoding, **or** lossless Entity-name/reference renaming **without** changing governed meaning **or** the Atom's Summary value | Keep the Atom ID **and** Version | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while primary Claim, applicability, **and** acceptance meaning remain equivalent **and** the Summary value remains unchanged | Keep the Atom ID **and** Version | Demonstrate equivalence |
| `semantic_revision` | Meaning **or** applicability changes while the same primary Claim remains recognizable **and** the Summary value remains unchanged | Keep the Atom ID **and** create a new Revision | Declare the delta **and** complete lineage-impact review |
| `replacement` | the Summary value changes under CA-R-1464, the primary Claim changes identity, **or** an independently replaceable Claim is added **or** removed | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

**if** Scope narrowing **or** expansion preserves the primary Claim identity **and** Summary value, **then** it is a `semantic_revision`, **not** a carrier-only change. splitting **or** combining independently replaceable Claims is a `replacement`. the Summary-change replacement rule takes precedence even **when** the Claim remains unchanged; lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.

## Details
