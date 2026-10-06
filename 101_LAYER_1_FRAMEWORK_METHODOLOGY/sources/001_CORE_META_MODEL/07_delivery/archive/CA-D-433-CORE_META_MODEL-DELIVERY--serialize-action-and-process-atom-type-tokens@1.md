---
atom_id: CA-D-433
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Ops/Type"
  depends_on:
    - "Carrier"
version: 1
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
---
# Serialize Action and Process Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type component as `ACTION` **if** its Type is Action **or** as `PROCESS` **if** its Type is Process, within the Atom filename grammar governed by CA-D-283 **and** CA-D-284.
