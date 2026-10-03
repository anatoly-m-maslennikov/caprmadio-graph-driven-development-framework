---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Current Scope/Governed Subject Set
  depends_on:
    continuant:
      - Subject
      - Atom/Current Scope/Owner
      - Atom/Claim Scope
      - Claim-Subject Relation/Kind: GOVERNS
version: 6
updated_at: 2026-09-02 00:35:23 +0400
relations:
  child_of:
    - CA-R-919
    - CA-R-1013
---
# Limit Subject-derived Scope Coordinates

an Atom's GOVERNS Subjects **must** determine **only** its Governed Subject Set **and** **must not** determine its Current Scope Owner **or** Claim Scope.
