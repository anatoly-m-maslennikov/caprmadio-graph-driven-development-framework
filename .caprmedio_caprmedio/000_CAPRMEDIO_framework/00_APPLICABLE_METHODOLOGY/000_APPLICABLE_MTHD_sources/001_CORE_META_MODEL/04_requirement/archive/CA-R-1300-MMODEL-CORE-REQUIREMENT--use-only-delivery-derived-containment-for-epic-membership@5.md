---
atom_id: CA-R-1300
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - "Atom Collection/Type: Epic/Membership"
  depends_on:
    continuant:
      - Containment Relation Pair
      - Delivery
version: 5
updated_at: 2026-09-04 01:04:00 +0400
relations: {}
---
# Use Only Delivery-Derived Containment for Epic Membership

the Epic membership **must** use **only** `CONTAINS` **and** `IS_CONTAINED_BY` relation pairs derived by Delivery authority.
