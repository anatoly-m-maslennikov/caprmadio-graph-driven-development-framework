---
subjects:
  governs: "Relation/authority"
  depends_on:
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Projection"
    - "Single Source of Truth"
    - "Atom/Claim"
    - "Structural Entity"
    - "Journal"
version: 4
updated_at: "2026-09-15 01:47:49 +0400"
relations: {}
---
# Keep one source for each relation fact

**every** independently authored Relation fact **must** have **`=1`** authoritative source declaration under Single Source of Truth. its representation **in** multiple CAPRMEDIO Graph views remains a reference **or** derived Projection of that declaration **without** creating another independently maintained source.

a Relation derived under admitted derivation authority **must** remain traceable **to** that authority **and** its authoritative input facts, including through upstream Projections. it does **not** require a fabricated direct source declaration for the derived result. this distinction **must not** weaken a Relation Kind's requirement for an explicit source fact **or** permit unsupported inference.
