---
atom_id: CA-D-301
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - Carrier/Canonical Address/Segment
version: 1
updated_at: 2026-08-28 23:15:00 +0400
relations: {}
---
# Require Portable-Safe Carrier Addresses

every Project-owned Carrier address segment **must** use only portable automation-safe ASCII letters, digits, underscores, hyphens, and dots, **must not** contain whitespace, control characters, path separators, shell metacharacters, empty or reserved segments, or unsafe leading or trailing characters, and **must** remain sibling-unique under ASCII case folding.
