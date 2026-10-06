---
atom_id: CA-R-1294
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    continuant:
      - Atom/Current Scope
      - Atom/Claim Scope
version: 4
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Derive Demand Direction without Another Relation Kind

a Demand Atom **must not** introduce a graph relation Kind for its direction because its Consumer Current Scope **and** Producer Claim Scope references determine that direction.
