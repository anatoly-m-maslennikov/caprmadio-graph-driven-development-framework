---
subjects:
  governs: "Projection"
  depends_on:
    - "Carrier"
    - "Type"
    - "Atom/Claim"
version: 3
updated_at: "2026-09-13 15:47:24 +0400"
relations: {}
---
# Separate Projection derivation from Carrier materialization

the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.
