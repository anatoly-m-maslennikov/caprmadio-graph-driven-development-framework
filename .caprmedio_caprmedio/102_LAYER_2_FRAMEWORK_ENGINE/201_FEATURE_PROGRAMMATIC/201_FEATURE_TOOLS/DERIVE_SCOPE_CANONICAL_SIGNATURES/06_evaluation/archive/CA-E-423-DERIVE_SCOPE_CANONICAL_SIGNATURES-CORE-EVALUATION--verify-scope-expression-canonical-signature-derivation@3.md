---
atom_id: CA-E-423
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES/Canonical Scope Signature Derivation Validation"
  depends_on:
    - "Tool/DERIVE_SCOPE_CANONICAL_SIGNATURES"
    - "Scope Expression/Canonical Scope Signature"
version: 3
updated_at: 2026-09-02 01:12:00 +0400
relations:
  evaluation_for:
    - CA-M-257
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify Scope Expression Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-407 **or** changes one selected Source Atom.
