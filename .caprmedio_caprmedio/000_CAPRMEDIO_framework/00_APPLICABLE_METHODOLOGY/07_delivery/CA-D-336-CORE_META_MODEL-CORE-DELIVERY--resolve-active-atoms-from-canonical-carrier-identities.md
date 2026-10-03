---
atom_id: CA-D-336
cce_version: cce_1
cce_form: resolution
subjects:
  governs:
    occurrent:
      - Active Atom Carrier Discovery
  depends_on:
    continuant:
      - Atom/Identity
      - Carrier/Canonical Address
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-336-CORE_META_MODEL-CORE-DELIVERY--resolve-active-atoms-from-canonical-carrier-identities.md
---
# Resolve Active Atoms from Canonical Carrier Identities

Active Atom Carrier discovery **must** resolve requested Atom IDs from canonical identity segments **in** the selected Project-owned Carrier frontier, exclude **every** non-Active Status directory, **and** fail on zero **or** multiple active matches.
