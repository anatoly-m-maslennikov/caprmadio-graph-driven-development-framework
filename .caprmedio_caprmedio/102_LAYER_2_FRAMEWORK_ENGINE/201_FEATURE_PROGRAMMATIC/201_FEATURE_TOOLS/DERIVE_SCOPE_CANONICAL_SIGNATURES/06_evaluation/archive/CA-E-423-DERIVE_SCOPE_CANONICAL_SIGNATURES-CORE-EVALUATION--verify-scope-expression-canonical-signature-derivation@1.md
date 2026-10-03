---
atom_id: CA-E-423
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES/Canonical Scope Signature Derivation Validation
  depends_on:
    continuant:
      - Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES
      - Scope Expression/Canonical Scope Signature
version: 1
updated_at: 2026-09-02 01:12:00 +0400
relations:
  evaluation_for:
    - CA-M-257
---
# Verify Scope Expression Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-407 **or** changes one selected Source Atom.
