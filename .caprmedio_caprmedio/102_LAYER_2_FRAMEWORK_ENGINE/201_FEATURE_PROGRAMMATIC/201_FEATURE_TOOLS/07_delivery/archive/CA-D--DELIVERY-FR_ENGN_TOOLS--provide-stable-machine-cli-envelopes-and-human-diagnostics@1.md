---
subject_scopes:
  - cli
version: 1
updated_at: 2026-08-21 20:35:00
relations: {}
---
# Provide stable machine CLI envelopes and human diagnostics

Deliver every public Tool command with a schema-versioned machine-readable result envelope, stable exit semantics, and deterministic diagnostics. Keep identifiers, mode, success state, result data, and diagnostics structurally distinct.

Provide concise human-facing explanations without changing the canonical machine meaning. Adding a field must preserve the declared compatibility boundary or advance the schema version explicitly.

Candidate alignment: CA-D-001, CA-D-002, CA-M-002, CA-R-861.

## Sources

- [Python documentation: argparse](https://docs.python.org/3.14/library/argparse.html)
- [Python documentation: json](https://docs.python.org/3.14/library/json.html)
