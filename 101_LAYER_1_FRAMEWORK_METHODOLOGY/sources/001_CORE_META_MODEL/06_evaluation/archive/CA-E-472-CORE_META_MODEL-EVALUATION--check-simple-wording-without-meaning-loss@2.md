---
version: 2
updated_at: "2026-09-15 23:08:05 +0400"
relations:
  evaluation_for:
    - CA-M-294
subjects:
  governs: "language"
  depends_on:
    - "Author"
    - "Atom/Claim"
    - "Atom/Claim/Scope"
    - "Atom/Summary"
    - "Governed Term"
    - "CCE Operator"
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Check simple wording without meaning loss

wording evaluated under CA-M-294 fails **if** **any** of the following holds:

- a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
- a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
- a simplification adds ambiguity **or** substitutes an unregistered synonym for a canonical Term, CCE Operator, **or** reference.
- a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim **or** Claim Scope.

necessary specialized wording **must not** fail merely because it is technical. shorter wording **must not** pass merely because it uses fewer words. uncertain meaning preservation remains unevaluated, **not** passed.
