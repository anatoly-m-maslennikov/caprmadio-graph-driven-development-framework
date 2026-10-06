---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Scope Expression/Canonical Scope Signature"
  depends_on:
    - "Scope Expression"
    - "Atom"
    - "Atom/Identifier"
    - "Artifact/Carrier"
    - "CCE Operator"
version: 8
updated_at: "2026-09-17 04:41:39 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Canonical Scope Signature

a Canonical Scope Signature **means** a derived non-authoritative comparison value for **=1** parenthesized Scope Expression occurrence satisfying **all** of the following boundaries.

## admitted expression

- a group contains **>=2** operands **and** uses **=1** Boolean Operator value from (**`and`**, **`or`**). its operands are joined **only** by repetitions of that Operator.
- an operand is an exact Atom ID **or** a nested parenthesized group with the same Boolean Operator as its containing group.
- **every** exact Atom ID resolves **to** **=1** active Atom Carrier inside the selected source frontier.

## canonical value

- the value preserves whether the root Boolean Operator is **`and`** **or** **`or`**.
- the value represents the flattened same-operator group as unique exact Atom IDs **in** canonical lexical order.
- groups that differ **only** by same-operator nesting, repeated exact Atom IDs, **or** operand order have the same value.

## exclusions

mixed Boolean Operators, **without**, **where**, **all**, **every** other CCE Operator, functions, Entity-kind selectors, descendant **or** dynamic selectors, unresolved identities, a changing source frontier, **and** unparseable prose are outside this signature domain.
