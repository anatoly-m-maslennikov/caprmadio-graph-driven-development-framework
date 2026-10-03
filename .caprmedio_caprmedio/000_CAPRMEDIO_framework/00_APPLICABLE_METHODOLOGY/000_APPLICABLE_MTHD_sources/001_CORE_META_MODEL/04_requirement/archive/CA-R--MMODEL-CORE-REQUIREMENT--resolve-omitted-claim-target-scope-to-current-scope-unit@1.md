---
subjects:
  governs: "Atom/Claim/Target Scope"
  depends_on:
    - "Atom/Scope"
    - "Scope Unit"
    - "Atom/Carrier"
cce_version: cce_1
cce_form: resolution
version: 1
updated_at: "2026-09-15 23:56:42 +0400"
relations: {}
---
# Resolve Omitted Claim Target Scope to the Current Scope Unit

an Atom with **`=1`** current Scope Unit **and** no explicit Claim Target Scope representation **must** resolve its Claim Target Scope **to** that current Scope Unit; omission removes **only** duplicated Carrier representation **and** **must not** remove the semantic value.
