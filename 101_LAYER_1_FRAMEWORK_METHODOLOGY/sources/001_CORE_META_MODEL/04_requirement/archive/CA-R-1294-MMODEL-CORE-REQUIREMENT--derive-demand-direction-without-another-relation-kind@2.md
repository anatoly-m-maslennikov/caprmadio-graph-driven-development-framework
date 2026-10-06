---
atom_id: CA-R-1294
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - Demand/Direction
  depends_on:
    continuant:
      - Atom/Current Scope
      - Atom/Claim Scope
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
---
# Derive Demand Direction without Another Relation Kind

a Demand Atom **must not** introduce a graph relation Kind for its direction because its Consumer Current Scope **and** Producer Claim Scope references determine that direction.
