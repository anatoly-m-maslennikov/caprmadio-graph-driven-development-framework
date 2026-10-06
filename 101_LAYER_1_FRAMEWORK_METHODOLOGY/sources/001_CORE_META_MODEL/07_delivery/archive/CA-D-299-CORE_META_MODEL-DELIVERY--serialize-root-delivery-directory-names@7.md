---
atom_id: CA-D-299
cce_version: cce_1
cce_form: grammar
subjects:
  governs: "Directory Carrier/Name"
  depends_on:
    - "Scope Unit/Name"
    - "Scope Unit/Label"
    - "Structural Level"
    - "Navigational Order Number"
    - "Local Order"
version: 7
updated_at: "2026-09-15 00:13:02 +0000"
relations: {}
---
# Serialize Root Delivery Directory Names

**when** the default Scope Unit directory convention is used, **every** root Delivery Directory Carrier for a non-Project Scope Unit **must** serialize Structural Level, Navigational Order Number, **and** Scope Unit Name **and** **must not** serialize Label **or** Local Order. a declared native Carrier binding under CA-D-445 **must not** be reinterpreted through this default convention.
