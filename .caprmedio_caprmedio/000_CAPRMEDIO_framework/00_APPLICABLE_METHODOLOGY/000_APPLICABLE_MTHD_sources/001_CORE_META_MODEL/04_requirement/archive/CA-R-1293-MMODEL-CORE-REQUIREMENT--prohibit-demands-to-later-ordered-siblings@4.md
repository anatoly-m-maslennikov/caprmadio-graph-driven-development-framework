---
atom_id: CA-R-1293
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    continuant:
      - Local Order
      - "Scope Unit/Type: Ordered"
version: 4
updated_at: 2026-09-04 01:04:00 +0400
relations: {}
---
# Prohibit Demands to Later Ordered Siblings

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
