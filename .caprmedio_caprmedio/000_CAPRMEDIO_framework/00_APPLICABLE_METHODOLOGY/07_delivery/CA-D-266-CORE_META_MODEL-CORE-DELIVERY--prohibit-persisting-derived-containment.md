---
atom_id: CA-D-266
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - Structural Entity/Containment
  depends_on:
    continuant:
      - Containment Relation Pair
      - Directory Carrier/Nesting
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-266-CORE_META_MODEL-CORE-DELIVERY--prohibit-persisting-derived-containment.md
---
# Prohibit Persisting Derived Containment

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
