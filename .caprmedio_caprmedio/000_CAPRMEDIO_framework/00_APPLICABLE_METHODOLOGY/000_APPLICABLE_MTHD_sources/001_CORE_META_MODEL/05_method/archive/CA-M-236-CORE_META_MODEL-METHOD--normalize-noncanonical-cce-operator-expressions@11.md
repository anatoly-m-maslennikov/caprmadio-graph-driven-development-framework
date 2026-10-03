---
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 11
updated_at: "2026-09-10 03:25:26 +0400"
relations: {}
atom_id: "CA-M-236"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Method"
---
# Normalize Noncanonical CCE Operator Expressions

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.
