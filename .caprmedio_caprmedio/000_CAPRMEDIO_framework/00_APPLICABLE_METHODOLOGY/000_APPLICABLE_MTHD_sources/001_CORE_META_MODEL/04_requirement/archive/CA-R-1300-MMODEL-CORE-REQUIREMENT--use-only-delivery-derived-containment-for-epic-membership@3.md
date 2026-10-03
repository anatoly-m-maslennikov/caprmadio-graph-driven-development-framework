---
atom_id: CA-R-1300
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - Epic/Membership
  depends_on:
    continuant:
      - CONTAINS
      - IS_CONTAINED_BY
      - Delivery
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Use Only Delivery-Derived Containment for Epic Membership

Epic membership **must** use **only** **contains** **and** IS_CONTAINED_BY relations derived by Delivery authority.
