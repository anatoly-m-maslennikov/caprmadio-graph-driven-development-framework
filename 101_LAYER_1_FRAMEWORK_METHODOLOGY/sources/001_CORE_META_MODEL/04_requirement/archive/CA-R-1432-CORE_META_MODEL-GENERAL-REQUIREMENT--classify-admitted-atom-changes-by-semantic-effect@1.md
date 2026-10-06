---
atom_id: CA-R-1432
cce_version: cce_1
cce_form: classification
subjects:
  governs:
    occurrent:
      - Atom Change Classification
  depends_on:
    continuant:
      - Atom
      - Atom/Claim
      - Atom/Claim/Scope
      - Artifact/Revision
      - Carrier-Only Recoding
      - Lineage Impact Analysis
      - Tool
version: 1
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
---
# Classify admitted Atom changes by semantic effect

**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, Summary, filename, path, **or** encoding changes **without** changing governed meaning | Keep the Atom ID | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while primary Claim, applicability, **and** acceptance meaning remain equivalent | Keep the Atom ID **and** create a new Revision | Demonstrate equivalence **and** assess lineage |
| `semantic_revision` | Meaning **or** applicability changes while the same primary Claim remains recognizable | Keep the Atom ID **and** create a new Revision | Declare the delta **and** complete lineage-impact review |
| `replacement` | The primary Claim changes identity, **or** an independently replaceable Claim is added **or** removed | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

Scope narrowing **or** expansion is a `semantic_revision`, **not** a carrier-only change. splitting **or** combining independently replaceable Claims is a `replacement`. the semantic change class is independent of the Git change set; persistence remains governed by CA-D-334 **and** CA-D-335.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.
