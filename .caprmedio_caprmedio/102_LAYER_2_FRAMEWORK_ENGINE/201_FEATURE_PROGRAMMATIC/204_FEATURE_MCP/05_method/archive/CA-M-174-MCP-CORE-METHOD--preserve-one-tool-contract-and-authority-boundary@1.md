---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - framework-engine-mcp
version: 1
updated_at: 2026-08-23 17:40:00 +0400
relations:
  method_for:
    - CA-R-1112
  derived_from:
    - CA-A-057
---
# Preserve one Tool contract and authority boundary

## Applicable when

Apply while MCP adapts one canonical Tool request or result to protocol transport.

## Procedure

1. Preserve accepted inputs, results, diagnostics, failures, target-set identity, and side-effect controls exactly.
2. Pass a CAPRMEDIO Markdown Atom Doer's sealed target set, expected revision or digest, Initiative action, and receipt through unchanged.
3. Keep Finder, Checker, and Doer boundaries intact; do not infer approval or turn a failed or partial result into success.

## Outcome

Transport changes representation only, never Tool authority or semantics.

## Failure or stop

Stop whenever protocol adaptation would broaden authority, alter cardinality, or obscure a Tool failure.
