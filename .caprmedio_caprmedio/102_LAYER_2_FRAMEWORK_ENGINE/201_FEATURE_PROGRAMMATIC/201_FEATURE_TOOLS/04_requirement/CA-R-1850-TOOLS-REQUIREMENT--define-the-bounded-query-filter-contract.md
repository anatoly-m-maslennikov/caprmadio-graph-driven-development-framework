---
atom_id: CA-R-1850
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
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

The request is UTF-8 JSON. `expression := or`; `or := and (OR and)*`; `and := unary (AND unary)*`; `unary := NOT unary | primary`; and `primary := comparison | '(' expression ')'`. Tokens `NOT`, `AND`, `OR`, `IN`, `=`, `!=`, `(`, `)`, and `,` are ASCII tokens separated from JSON strings. A selector is one RFC 8259 JSON string token; a literal is one RFC 8259 JSON value token. A comparison is `selector (= | !=) literal` or `selector IN '(' literal (',' literal)* ')'`. Parentheses override precedence; NOT, then AND, then OR bind in that order. A caller Tool defines valid selectors and rejects unknown ones.

Artifact selectors are JSON strings `"fm:/<pointer>"` and `"section:/<level>:<heading>/..."`; pointer tokens and each complete heading segment apply RFC 6901 `~0`/`~1` escaping. JSON Pointer resolves nested object members and array indexes; the namespace prevents frontmatter/section collision.

Comparison is deep, literal, and type-preserving: null, boolean, number, string, array, and object are admitted RFC 8259 values; boolean and number are distinct; arrays compare in order and objects by member names and values. No coercion occurs. Every IN member is independently compared by this equality. Absent selector makes comparison false; explicit null remains a value. YAML temporals normalize to explicit strings; strings are never parsed as dates. Invalid JSON, grammar, selector, type, or non-literal is diagnostic.

Enforce values resolved first from explicit instance or request settings, otherwise Default Settings `[query]`: `max_request_bytes`, `max_grammar_depth`, `max_filter_tokens`, `max_in_members`, `max_selected_fields`, `max_page_size`, `max_snapshot_members`, `max_file_bytes`, `max_total_read_bytes`, `timeout_seconds`, and `max_findings`. They respectively bound whole request, parse depth, tokens, one IN list, selection, response page, enumeration, one file, total reads, operation time, and retained diagnostics. Values are positive integers; missing, nonpositive, or over-budget requests are rejected. These are enforceable configuration limits, not methodology constants.
