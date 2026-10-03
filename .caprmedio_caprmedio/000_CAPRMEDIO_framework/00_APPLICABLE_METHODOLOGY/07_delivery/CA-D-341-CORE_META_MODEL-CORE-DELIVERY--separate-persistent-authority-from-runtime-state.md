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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-341-CORE_META_MODEL-CORE-DELIVERY--separate-persistent-authority-from-runtime-state.md
---
# Separate Persistent Authority from Runtime State

Framework-Owned **and** Project-Owned persistent Carriers **must** remain outside Runtime State so Runtime State cleanup cannot remove canonical authority **or** Journal history.
