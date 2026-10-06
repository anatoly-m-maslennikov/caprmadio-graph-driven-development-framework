---
subjects:
  governs: "Subject Expression/Delivery"
  depends_on:
    - "Atom/Carrier"
    - "Subject Expression"
    - "Subject Expression/Natural Rendering"
    - "Subject Path"
cce_version: cce_1
cce_form: delivery
version: 1
updated_at: "2026-09-16 00:13:53 +0400"
relations: {}
---
# Deliver Qualified Entity Names by Interaction Boundary

a Delivery of a qualified Entity name **must** use its canonical Subject Expression **in** every Atom **and may** use its Natural Rendering **in** an Operator prompt **or** LLM answer **only if** the interaction context resolves that rendering **to** **`=1`** canonical qualified Subject Expression.
