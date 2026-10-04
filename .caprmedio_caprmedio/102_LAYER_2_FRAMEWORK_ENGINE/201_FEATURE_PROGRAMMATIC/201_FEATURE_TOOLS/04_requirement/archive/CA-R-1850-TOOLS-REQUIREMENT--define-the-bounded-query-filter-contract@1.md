---
atom_id: CA-R-1850
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:00:00 +0400"
subjects:
  governs: QUERY_FILTER
  depends_on: [Tool, Query, Artifact, Journal]
relations: {}
---
# Summary

Define the bounded query-filter contract

## Scope

The shared basic filter contract for read-only query Tools. Each Tool retains
its own selector namespace, source domain, request/result representation,
coverage, and diagnostic carrier.

## Claim

Every Tool that uses QUERY_FILTER **must** accept only the closed literal
comparison grammar with exact typed equality, inequality, `NOT`, `IN`, and
parenthesized boolean composition defined below; it must reject arbitrary SQL,
code, evaluation, unknown syntax, and invalid typed literals.

## Details

`expression := or`; `or := and (OR and)*`; `and := unary (AND unary)*`;
`unary := NOT unary | primary`; and `primary := comparison | '(' expression
')'`. A `comparison` is `selector (= | !=) literal` or `selector IN '('
literal (',' literal)* ')'`. Parentheses override precedence; `NOT`, then
`AND`, then `OR` bind in that order. A caller Tool defines which selectors are
valid and how it reads their values, but must reject an unknown selector.

Comparison is literal and type-preserving: scalar types must match exactly, no
string/number/boolean coercion occurs, and every `IN` member has the selected
value's scalar type. An absent selector value makes its comparison false; an
explicit null remains a value of its own type. Invalid grammar, type mismatch,
unsupported collection/object value, or non-literal input is an invalid-filter
diagnostic, never an executable expression.
