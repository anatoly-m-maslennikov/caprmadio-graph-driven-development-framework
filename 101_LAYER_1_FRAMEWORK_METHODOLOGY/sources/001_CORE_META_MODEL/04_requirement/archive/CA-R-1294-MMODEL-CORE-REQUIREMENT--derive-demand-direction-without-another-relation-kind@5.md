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
      - Atom/Current Scope/Owner
      - Atom/Claim Scope/Scope Unit Set
version: 5
updated_at: 2026-09-02 00:35:23 +0400
relations: {}
---
# Derive Demand Direction without Another Relation Kind

a Demand Atom **must not** introduce a graph relation Kind for its direction because its Consumer Current Scope Owner Scope Unit **and** Producer Claim Scope Scope Unit references determine that direction.
