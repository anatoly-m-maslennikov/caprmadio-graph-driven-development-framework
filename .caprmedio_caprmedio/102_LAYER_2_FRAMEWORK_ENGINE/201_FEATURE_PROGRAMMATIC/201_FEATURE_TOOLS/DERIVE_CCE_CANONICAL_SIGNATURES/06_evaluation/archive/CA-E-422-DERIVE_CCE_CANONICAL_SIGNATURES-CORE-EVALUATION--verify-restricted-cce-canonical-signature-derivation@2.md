---
atom_id: CA-E-422
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/DERIVE_CCE_CANONICAL_SIGNATURES/Canonical Signature Derivation Validation"
  depends_on:
    - "Tool/DERIVE_CCE_CANONICAL_SIGNATURES"
    - "Atom/Claim/Canonical Signature"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  evaluation_for:
    - CA-M-256
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Verify Restricted CCE Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-405 **or** changes one selected Source Atom.
