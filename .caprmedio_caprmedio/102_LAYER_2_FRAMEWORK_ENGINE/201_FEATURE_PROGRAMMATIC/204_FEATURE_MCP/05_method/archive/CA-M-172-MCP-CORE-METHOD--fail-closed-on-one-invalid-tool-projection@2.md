---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - framework-engine-mcp
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  method_for:
    - CA-R-1110
  derived_from:
    - CA-A-057
---
# Fail closed on one invalid Tool projection

## Applicable when

Apply when registry generation detects an invalid selected Tool contract or projection.

## Procedure

1. Retain the complete candidate frontier and identify the first invalid source or projection field.
2. Emit explicit diagnostics for that defect without publishing a partial or misrepresented current registry.
3. Require a complete valid frontier before a later publication attempt.

## Outcome

MCP never presents a partial, silently skipped, or stale registry as current.

## Failure or stop

Stop publication until the invalid source or ambiguity is resolved.
