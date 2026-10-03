---
atom_id: CA-M-111
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Scope"
    - "CCE"
    - "Atom/Summary"
cce_version: cce_1
cce_form: method
version: 17
updated_at: "2026-09-14 02:40:31 +0400"
relations: {}
---
# Author one CCE Claim and derived Summary

**to** author one CAPRMEDIO Atom Claim, the Author **must** perform **all** of:

1. write **`=1`** independently replaceable Claim **in** CAPRMEDIO Controlled English.
2. resolve **`=1`** atomic **or** composite Claim Scope; omit its duplicate representation for a Current-scope Atom **and** represent its different target explicitly for a Relational Atom.
3. derive **`=1`** concise Summary from the complete Claim **and** its resolved Claim Scope **when** creating the Atom. **when** revising an existing Atom, retain its Summary **and** check its source faithfulness under CA-R-1273; **if** that Summary needs changing, use a new Atom identity under CA-R-1464 instead of revising the existing identity.
4. derive **every** Translation from the complete Claim **and** its resolved Claim Scope rather than from the Summary.
