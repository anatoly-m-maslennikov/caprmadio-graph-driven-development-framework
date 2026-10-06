---
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    - "Atom/Claim"
    - "Atom/Summary"
version: 14
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
---
# Derive Navigation Projections from the CCE Claim

**to** derive an Atom's navigation values, the Generator **must** read the complete Claim, including **any** applicability restrictions within it,, derive **`=1`** concise source-faithful Summary **when** creating the Atom, **and** derive **every** requested Projection directly from the Claim, including **any** applicability restrictions within it, rather than from the Summary. for an existing Atom identity, retain its Summary **and** check it against those sources; a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.
