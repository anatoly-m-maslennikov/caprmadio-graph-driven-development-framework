---
subjects:
  governs: "Atom/Claim/Canonical Signature"
  depends_on:
    - "Atom/Claim"
    - "CCE Operator"
version: 7
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-R-918
---
# Define Restricted CCE Canonical Signature

a Canonical Signature **means** one derived non-authoritative comparison value for **`=1`** parenthesized restricted Boolean expression occurrence **in** one Atom Claim, **where** `group ::= (operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])`, `operand ::= atomic predicate | nested group with the same Boolean Operator`, `atomic predicate ::= subject path: value`, canonicalization flattens nested same-operator groups, removes duplicate atomic predicates, sorts the remaining atomic predicates, preserves the root Boolean Operator, **and** excludes mixed Boolean Operators, **every** other CCE Operator, unrecognized bold token, unbalanced parentheses, **and** unparseable prose.
