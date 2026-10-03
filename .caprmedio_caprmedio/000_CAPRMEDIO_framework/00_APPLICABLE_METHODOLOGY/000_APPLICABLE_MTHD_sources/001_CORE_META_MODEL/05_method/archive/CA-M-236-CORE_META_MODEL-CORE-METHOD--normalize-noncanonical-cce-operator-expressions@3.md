---
atom_id: CA-M-236
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - CCE Operator Expression Normalization
  depends_on:
    continuant:
      - CCE Operator Expression
      - CCE Operator Registry
version: 3
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
---
# Normalize Noncanonical CCE Operator Expressions

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

1. `each` to **every**.
2. `equals` to **`=`**.
3. `does not equal` to **`!=`**.
4. `both <A> and <B>` to `(<A>` **and** `<B>)`.
5. `either <A> or <B>` to `(<A>` **or** `<B>)`.
6. `neither <A> nor <B>` to **not** `(<A>` **or** `<B>)`.
