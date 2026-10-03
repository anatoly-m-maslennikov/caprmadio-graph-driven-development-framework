---
atom_id: CA-R-1246
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Relation Kind
  depends_on:
    continuant:
      - CAPRMEDIO Graph
      - Applicable Methodology
version: 6
updated_at: "2026-09-11 05:04:26 +0400"
relations: {}
---
# Keep relation vocabularies graph-specific

**every** Relation Kind **must** belong **to** **`=1`** kind of CAPRMEDIO Graph **and** be admitted **only** **in** instances of that graph kind. instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same Relation Kind authority.

the owning graph kind **and** canonical name **must** determine the Relation Kind's graph-qualified identity. matching names **or** compatible endpoints **must not** make Relation Kinds from different graph kinds interchangeable.
