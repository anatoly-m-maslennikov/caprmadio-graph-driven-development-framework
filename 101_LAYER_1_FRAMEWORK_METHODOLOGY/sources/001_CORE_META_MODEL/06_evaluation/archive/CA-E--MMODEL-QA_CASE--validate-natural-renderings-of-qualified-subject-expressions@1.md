---
subjects:
  governs: "Subject Expression/Natural Rendering"
  depends_on:
    - "Subject Expression"
    - "Subject Path"
    - "IS_BORNE_BY"
    - "IS_ALLOWED_VALUE_OF"
cce_version: cce_1
cce_form: evaluation
version: 1
updated_at: "2026-09-16 00:13:53 +0400"
relations:
  evaluation_for:
    - CA-R-1204
    - CA-R-1245
    - CA-M-228
---
# Validate Natural Renderings of Qualified Subject Expressions

## Claim checked

a Natural Rendering preserves the canonical target **and** registered qualification semantics of **`=1`** qualified Subject Expression.

## Test case

render each qualified Subject Expression **in** an Operator prompt **and** LLM answer:

- `Claim/Target Scope` as `Claim Target Scope`;
- `Content Role/Requirement` as `Content Role Requirement`;
- `Atom/Type` as `Atom Type`;
- `Scope Unit/Own Atoms` as `Scope Unit Own Atoms`; **and**
- `Requirement/Type: Goal` as `Requirement Type Goal`.

resolve each pair against the same complete vocabulary **and** context. author an Atom once with the canonical qualified expression **and** once with its Natural Rendering. **then** reorder one component, omit one component, use `/` where `:` is required, use `:` where `/` is required, admit two qualified expressions that share the same Natural Rendering **in** the selected context, **or** interpret `/` as a filesystem path, set operation, **or** hierarchy edge.

## Acceptance criteria

each valid interaction pair resolves **to** the same canonical target with the same IS_BORNE_BY **and** IS_ALLOWED_VALUE_OF relations. the Atom using the canonical qualified expression passes; the Atom using its Natural Rendering fails. every changed, ambiguous, misqualified, **or** misinterpreted expression fails with the exact unresolved component **or** relation identified.

## Failure disposition

record a Concern naming the qualified Subject Expression, Natural Rendering, context, **and** failed resolution.
