---
atom_id: CA-R-1437
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Relation/authority
  depends_on:
    continuant:
      - Relation
      - CAPRMEDIO Graph
      - Projection
version: 1
updated_at: "2026-09-11 05:04:26 +0400"
relations: {}
---
# Keep one source for each relation fact

a Relation fact **must** have **`=1`** authoritative source declaration. its representation **in** multiple CAPRMEDIO Graph views **must** remain a reference **or** derived Projection of that declaration **and** **must not** create another independently maintained source of authority.
