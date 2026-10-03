---
subjects:
  governs: "Atom/Content Role: Delivery/Type"
  depends_on:
    - "Carrier"
version: 7
updated_at: "2026-09-17 15:05:42 +0000"
relations: {}
---
# Serialize Delivery Type Tokens

a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Release Definition: `RELEASE_DEFINITION`.
- Environment Definition: `ENVIRONMENT_DEFINITION`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
