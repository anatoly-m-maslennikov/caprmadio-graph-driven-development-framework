---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 2
updated_at: 2026-08-30 16:44:07 +0400
relations:
  evaluation_for:
    - CA-M-220
---
# Verify executable Tool folder registration

## Claim checked

CA-M-220 registers every admitted immediate executable Tool folder as exactly one active Tool Scope Unit while excluding infrastructure folders.

## Test case

Provide a fixture containing the five canonical executable folders `GENERATE_PROJECT_GRAPH_STATE`, `CLOSE_ATOM`, `MIGRATE_ATOM_IDENTITY`, `REBIND_ATOM_RELATIONS`, and `REPLACE_ATOM`, plus a cache folder, a migration collection, a shared library, one explicitly disabled Tool, and one duplicate Tool identity. Resolve registration and MCP discovery twice over the same unchanged frontier.

## Acceptance criteria

Each enabled canonical executable folder yields exactly one registered immediate Tool unit and one MCP-eligible identity; the disabled Tool remains registered but is not MCP-eligible; infrastructure folders yield none; the duplicate identity fails explicitly; and repeated resolution produces the same ordered Tool frontier.

## Failure disposition

Reject the registration or MCP frontier, preserve every pre-existing carrier and Projection, and report the exact invalid folder or identity without publishing a partial current result.
