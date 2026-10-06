---
atom_id: CA-R-1014
cce_version: cce_1
cce_form: requirement
subjects:
  governs:
    continuant:
      - Atom/Claim/Governed Subject Set
  depends_on:
    continuant:
      - Subject
      - Atom/Scope
      - Atom/Claim/Scope
      - "Claim-Subject Relation/Kind: GOVERNS"
version: 9
updated_at: 2026-09-04 14:07:21 +0400
relations:
  child_of:
    - CA-R-919
    - CA-R-1013
---
# Keep Subjects Independent from Scope Coordinates

an Atom's GOVERNS Subjects **must** determine **only** its Claim's Governed Subject Set **and** **must not** determine its Atom Scope **or** Claim Scope.
