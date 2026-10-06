---
atom_id: CA-D-264
cce_version: cce_1
cce_form: derivation
subjects:
  governs:
    continuant:
      - Relational Artifact/Direct Containment
  depends_on:
    continuant:
      - Containment Relation Pair
      - Directory Carrier/Nesting
version: 5
updated_at: 2026-09-03 00:06:31 +0400
relations: {}
---
# Derive Direct Containment from the Nearest Directory Carrier

an Artifact Revision whose canonical Carrier is nested below a Directory Carrier **must** derive one direct `CONTAINS` **and** `IS_CONTAINED_BY` relation pair with the Relational Artifact Revision carried by its nearest ancestor Directory Carrier.
