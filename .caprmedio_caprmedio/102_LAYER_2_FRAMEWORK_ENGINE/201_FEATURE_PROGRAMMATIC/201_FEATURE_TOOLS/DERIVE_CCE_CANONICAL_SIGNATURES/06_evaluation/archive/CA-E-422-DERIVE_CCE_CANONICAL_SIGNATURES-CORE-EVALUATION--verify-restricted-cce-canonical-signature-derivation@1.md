---
atom_id: CA-E-422
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Tool/DERIVE_CCE_CANONICAL_SIGNATURES/Canonical Signature Derivation Validation
  depends_on:
    continuant:
      - Tool/DERIVE_CCE_CANONICAL_SIGNATURES
      - Atom/Claim/Canonical Signature
version: 1
updated_at: 2026-09-02 01:12:00 +0400
relations:
  evaluation_for:
    - CA-M-256
---
# Verify Restricted CCE Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-405 **or** changes one selected Source Atom.
