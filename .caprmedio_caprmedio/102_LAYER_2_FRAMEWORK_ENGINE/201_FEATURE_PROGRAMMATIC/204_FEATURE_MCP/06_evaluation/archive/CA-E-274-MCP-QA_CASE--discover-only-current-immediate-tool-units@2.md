---
cce_version: cce_1
cce_form: evaluation
subjects:
  declared:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-23 18:08:00 +0400
relations:
  evaluation_for:
    - CA-M-168
  derived_from:
    - CA-A-057
---
# Discover only current immediate Tool units

## Claim checked

MCP derives its source set from current immediate Tool units rather than helper folders.

## Test case

Add one enabled immediate Tool, one disabled immediate Tool, and one nested helper to a resolved test topology.

## Acceptance criteria

Discovery includes only the enabled immediate Tool and reports the other two dispositions explicitly.

## Failure disposition

Stop registry generation on an unresolved source identity.
