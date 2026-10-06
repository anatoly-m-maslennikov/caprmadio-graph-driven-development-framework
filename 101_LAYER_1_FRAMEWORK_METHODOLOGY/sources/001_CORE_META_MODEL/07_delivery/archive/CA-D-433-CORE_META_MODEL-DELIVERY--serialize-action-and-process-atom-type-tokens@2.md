---
atom_id: CA-D-433
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    - "Carrier"
version: 2
updated_at: 2026-09-15 05:51:38
relations: {}
---
# Serialize Action and Process Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type component as `ACTION` **if** its Type is Action **or** as `PROCESS` **if** its Type is Process, within the Atom filename grammar governed by CA-D-283 **and** CA-D-284.
