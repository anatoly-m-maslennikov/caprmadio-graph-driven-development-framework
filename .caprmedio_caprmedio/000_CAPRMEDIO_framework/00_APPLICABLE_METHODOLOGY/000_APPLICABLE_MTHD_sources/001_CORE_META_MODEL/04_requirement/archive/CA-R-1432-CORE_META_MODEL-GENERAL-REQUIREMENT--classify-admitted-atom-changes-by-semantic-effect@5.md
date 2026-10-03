---
cce_version: cce_1
cce_form: classification
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
version: 5
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Classify admitted Atom changes by semantic effect

**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, filename, path, **or** encoding changes **without** changing governed meaning **or** the Atom's Summary value | Keep the Atom ID | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while primary Claim, applicability, **and** acceptance meaning remain equivalent **and** the Summary value remains unchanged | Keep the Atom ID **and** create a new Revision | Demonstrate equivalence **and** assess lineage |
| `semantic_revision` | Meaning **or** applicability changes while the same primary Claim remains recognizable **and** the Summary value remains unchanged | Keep the Atom ID **and** create a new Revision | Declare the delta **and** complete lineage-impact review |
| `replacement` | the Summary value changes under CA-R-1464, the primary Claim changes identity, **or** an independently replaceable Claim is added **or** removed | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

**if** Scope narrowing **or** expansion preserves the primary Claim identity **and** Summary value, **then** it is a `semantic_revision`, **not** a carrier-only change. splitting **or** combining independently replaceable Claims is a `replacement`. the Summary-change replacement rule takes precedence even **when** the Claim remains unchanged; lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.
