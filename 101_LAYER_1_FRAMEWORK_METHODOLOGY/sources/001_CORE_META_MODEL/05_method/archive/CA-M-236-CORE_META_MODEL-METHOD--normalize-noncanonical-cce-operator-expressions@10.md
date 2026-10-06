---
subjects:
  governs: "CCE Operator Expression Normalization"
  depends_on:
    - "CCE Operator Expression"
    - "CCE Operator Registry"
version: 10
updated_at: "2026-09-10 03:25:26 +0400"
relations: {}
---
# Normalize Noncanonical CCE Operator Expressions

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.
