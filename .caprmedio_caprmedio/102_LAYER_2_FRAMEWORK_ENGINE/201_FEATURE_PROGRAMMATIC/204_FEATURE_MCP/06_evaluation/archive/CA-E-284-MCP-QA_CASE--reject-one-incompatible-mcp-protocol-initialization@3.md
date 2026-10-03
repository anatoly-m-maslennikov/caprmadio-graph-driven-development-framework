---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - framework-engine-mcp
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-178
  derived_from:
    - CA-A-057
---
# Reject one incompatible MCP protocol initialization

## Claim checked

MCP initialization admits only a declared compatible protocol revision and capability set.

## Test case

Initialize with one unsupported required protocol capability.

## Acceptance criteria

Initialization fails with a machine-readable incompatibility diagnostic and no undefined compatibility mode.

## Failure disposition

Stop the session before registry use or Tool dispatch.
