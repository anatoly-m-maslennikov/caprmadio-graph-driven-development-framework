---
atom_id: CA-D-298
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Directory Carrier/Name
  depends_on:
    continuant:
      - "Scope Unit/Type: Ordered"
      - "Scope Unit/Type: Unordered"
      - Scope Unit/Label
      - Local Order
version: 6
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
---
# Serialize Local Order Only for Ordered Scope Unit Directories

a Scope Unit authority Directory Carrier Name **must** serialize Local Order immediately **after** Label **only** for an Ordered Scope Unit **and** **must not** serialize Local Order for an Unordered Scope Unit.
