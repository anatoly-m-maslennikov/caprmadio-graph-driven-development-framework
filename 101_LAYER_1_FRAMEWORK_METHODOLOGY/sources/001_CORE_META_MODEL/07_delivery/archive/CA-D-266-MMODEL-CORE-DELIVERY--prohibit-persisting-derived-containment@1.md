---
atom_id: CA-D-266
cce_version: cce_1
cce_form: prohibition
subjects:
  governs:
    continuant:
      - Relational Artifact/Containment
  depends_on:
    continuant:
      - CONTAINS
      - IS_CONTAINED_BY
      - Directory Carrier/Nesting
version: 1
updated_at: 2026-08-28 23:15:00 +0400
relations: {}
---
# Prohibit Persisting Derived Containment

CONTAINS and IS_CONTAINED_BY relations derived from canonical Carrier nesting **must not** be persisted as independent relation declarations.
