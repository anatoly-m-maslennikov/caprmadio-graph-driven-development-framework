---
version: 4
updated_at: "2026-09-22 17:59:17 +0000"
relations:
  evaluation_for:
    - CA-M-294
subjects:
  governs: "language"
  depends_on:
    - "Author"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Governed Term"
    - "CCE Operator"
---
# Check simple wording without meaning loss

wording evaluated under CA-M-294 fails **if** **any** of the following holds:

- a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
- a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
- a simplification adds ambiguity **or** substitutes an unregistered synonym for a canonical Term, CCE Operator, **or** reference.
- a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim **or** Claim Scope.

necessary specialized wording **must not** fail merely because it is technical. shorter wording **must not** pass merely because it uses fewer words. uncertain meaning preservation remains unevaluated, **not** passed.
