---
subjects:
  governs: "Canonical Scope Signature Derivation Validation"
  depends_on:
    - "Scope Expression"
    - "Scope Expression/Canonical Scope Signature"
    - "Atom/Carrier"
version: 7
updated_at: "2026-09-10 05:21:58 +0400"
relations:
  evaluation_for:
    - CA-R-1361
    - CA-M-241
---
# Validate Canonical Scope Signature Boundary

the Evaluation **must** reject a Canonical Scope Signature derivation **if** it rewrites one source Carrier, treats one Signature as authority **or** Claim equivalence, accepts mixed **and** **or** groups, **without**, **where**, **all**, **any** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose, fails **to** flatten nested same-operator groups, retains duplicate exact Atom IDs, loses the distinction between **and** **and** **or**, **or** yields different Signatures from same-operator groups that differ **only** by operand order.
