---
atom_id: CA-M-231
cce_version: cce_1
cce_form: method
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Claim/Scope"
    - "Atom/Summary"
version: 10
updated_at: "2026-09-14 02:40:31 +0400"
relations: {}
---
# Derive Navigation Projections from the CCE Claim

**to** derive an Atom's navigation values, the Generator **must** read the complete Claim **and** any Claim Scope, derive **`=1`** concise source-faithful Summary **when** creating the Atom, **and** derive **every** requested Projection directly from the Claim **and** any Claim Scope rather than from the Summary. for an existing Atom identity, retain its Summary **and** check it against those sources; a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.
