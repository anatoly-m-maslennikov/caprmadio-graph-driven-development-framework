---
atom_id: CA-R-1360
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Atom/Claim/Canonical Signature"
  depends_on:
    - "Atom/Claim"
    - "CCE Operator"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - CA-R-918
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Restricted CCE Canonical Signature

a Canonical Signature **means** one derived non-authoritative comparison value for **`=1`** parenthesized restricted Boolean expression occurrence **in** one Atom Claim, **where** `group ::= (operand **and** operand [**and** operand ...]) | (operand **or** operand [**or** operand ...])`, `operand ::= atomic predicate | nested group with the same Boolean Operator`, `atomic predicate ::= subject path: value`, canonicalization flattens nested same-operator groups, removes duplicate atomic predicates, sorts the remaining atomic predicates, preserves the root Boolean Operator, **and** excludes mixed Boolean Operators, **every** other CCE Operator, unrecognized bold token, unbalanced parentheses, **and** unparseable prose.
