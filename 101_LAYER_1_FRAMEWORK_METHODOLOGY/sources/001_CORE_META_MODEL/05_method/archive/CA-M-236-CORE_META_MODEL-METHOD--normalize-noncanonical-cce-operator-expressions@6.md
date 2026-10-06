---
atom_id: CA-M-236
cce_version: cce_1
cce_form: method
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 6
updated_at: "2026-09-10 03:25:26 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Normalize Noncanonical CCE Operator Expressions

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

1. `each` to **every**.
2. `equals` to **`=`**.
3. `does not equal` to **`!=`**.
4. `both <A> and <B>` to `(<A>` **and** `<B>)`.
5. `either <A> or <B>` to `(<A>` **or** `<B>)`.
6. `neither <A> nor <B>` to **not** `(<A>` **or** `<B>)`.
