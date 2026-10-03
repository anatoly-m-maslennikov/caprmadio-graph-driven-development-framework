---
subjects:
  governs: "Structural Entity/Containment"
  depends_on:
    - "Containment Relation Pair"
    - "Directory Carrier/Nesting"
version: 10
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Prohibit Persisting Derived Containment

`CONTAINS` **and** `IS_CONTAINED_BY` relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
