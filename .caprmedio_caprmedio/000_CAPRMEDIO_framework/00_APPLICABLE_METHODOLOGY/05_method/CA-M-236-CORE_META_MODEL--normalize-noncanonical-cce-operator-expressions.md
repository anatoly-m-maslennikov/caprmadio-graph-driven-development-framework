---
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 12
updated_at: "2026-10-02 20:25:13 +0400"
relations: {}
atom_id: "CA-M-236"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-236-CORE_META_MODEL--normalize-noncanonical-cce-operator-expressions.md
  source_atom_id: CA-M-236
  source_atom_revision: 12
  source_sha256: 11adc0ba64795bc0b33892dfed8ce46c24c93a3fcc364ba1179a2a84aaa096b9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Normalize Noncanonical CCE Operator Expressions

## Scope

noncanonical CCE Operator Expressions.

## Claim

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.

## Details
