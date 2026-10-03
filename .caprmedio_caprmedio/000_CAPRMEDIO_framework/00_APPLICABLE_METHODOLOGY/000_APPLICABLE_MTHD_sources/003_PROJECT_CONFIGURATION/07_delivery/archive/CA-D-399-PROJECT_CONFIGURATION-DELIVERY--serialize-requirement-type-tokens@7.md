---
subjects:
  governs: "Atom/Content Role: Requirement/Type"
  depends_on:
    - "Carrier"
version: 7
updated_at: "2026-09-17 15:05:38 +0000"
relations: {}
---
# Serialize Requirement Type Tokens

a Requirement Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Constraint: `CONSTRAINT`.
- Boundary: `BOUNDARY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
