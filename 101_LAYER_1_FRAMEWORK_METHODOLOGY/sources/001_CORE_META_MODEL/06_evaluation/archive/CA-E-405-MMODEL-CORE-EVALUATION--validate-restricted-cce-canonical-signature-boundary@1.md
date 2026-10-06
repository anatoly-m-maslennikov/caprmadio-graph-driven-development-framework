---
atom_id: CA-E-405
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Canonical Signature Derivation Validation
  depends_on:
    continuant:
      - Atom/Claim
      - Atom/Claim/Canonical Signature
      - CCE Operator
version: 1
updated_at: 2026-09-01 23:31:49 +0400
relations:
  evaluation_for:
    - CA-R-1360
    - CA-M-240
---
# Validate Restricted CCE Canonical Signature Boundary

the Evaluation **must** reject a Canonical Signature derivation **if** it rewrites one source Claim, treats one Canonical Signature as authority, accepts mixed **and** **or** groups, rewrites negation, implication, **where**, **without**, temporal condition, quantifier, extension-defined CCE Operator, **or** unparseable prose, fails **to** flatten nested same-operator groups, retains duplicate atomic predicates, **or** yields different Canonical Signatures from Boolean groups that differ **only** by operand order.
