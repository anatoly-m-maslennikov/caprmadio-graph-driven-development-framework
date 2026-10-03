---
atom_id: CA-D-301
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - Carrier/Canonical Address/Segment
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-301-CORE_META_MODEL-CORE-DELIVERY--require-portable-safe-carrier-addresses.md
---
# Require Portable-Safe Carrier Addresses

**every** Project-owned Carrier address segment **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters, **and** **must** remain sibling-unique under ASCII case folding.
