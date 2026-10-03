---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - plugin-architecture
    occurrent:
      - evaluation
version: 3
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-150
  derived_from:
    - CA-A-057
---
# Select one minimal Codex plugin shape

## Claim checked

One selected Codex plugin shape contains only capabilities necessary for its bounded workflow.

## Test case

Evaluate one proposed plugin shape containing an unnecessary UI or MCP capability.

## Acceptance criteria

The selection rejects that capability unless the workflow evidence demonstrates its necessity; provider-neutral behavior remains referenced rather than copied.

## Failure disposition

Return the shape for boundary reduction before packaging.
