---
atom_id: CA-D-298
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Directory Carrier/Name
  depends_on:
    continuant:
      - "Scope Unit/Type: Ordered"
      - "Scope Unit/Type: Unordered"
      - Scope Unit/Label
      - Local Order
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-298-CORE_META_MODEL-CORE-DELIVERY--serialize-local-order-only-for-ordered-scope-unit-directories.md
---
# Serialize Local Order Only for Ordered Scope Unit Directories

a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit.
