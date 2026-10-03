---
atom_id: CA-D-341
cce_version: cce_1
cce_form: separation
subjects:
  governs:
    continuant:
      - Carrier/Storage Boundary
  depends_on:
    continuant:
      - Framework-Owned Carrier
      - Project-Owned Carrier
      - Runtime State Carrier
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Separate Persistent Authority from Runtime State

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.
