---
atom_id: CA-D-347
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Scope Expression/Canonical Scope Signature/Projection
  depends_on:
    continuant:
      - Scope Expression/Canonical Scope Signature
      - Carrier
version: 1
updated_at: 2026-09-01 23:45:22 +0400
relations:
  child_of:
    - CA-D-266
---
# Deliver Canonical Scope Signatures as External Report Projections

every Canonical Scope Signature Projection **must** be delivered as one non-authoritative JSON report outside its selected source folder with the selected source frontier digest, each source Atom identity and revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.
