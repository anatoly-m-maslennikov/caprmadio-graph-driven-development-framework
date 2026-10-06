---
subject_scopes:
  - language
relations:
  child_of:
    - CA-R-892
    - CA-R-893
    - CAPRMEDIO-META-REQU-126--govern-canonical-scoped-vocabulary
    - CAPRMEDIO-META-REQU-131--use-canonical-terms-for-governed-concepts
version: 2
updated_at: 2026-08-22 02:56:25
---
# Define CCE 1 interpretation rules

`cce_1` is the first CCE version identifier. In `cce_1`, uppercase function tokens have exactly the meanings defined here, and every other term or predicate phrase must resolve through the CCE vocabulary registry.

| Function | Admitted tokens | Interpretation |
|---|---|---|
| Reference and classification | `A`, `AN`, `THE`, `IS`, `IS NOT`, `MEANS`, `HAS` | `A` and `AN` introduce a kind member without asserting uniqueness; `THE` identifies exactly one resolvable participant; `IS` and `IS NOT` assert or deny classification or identity as selected by the statement form; `MEANS` establishes the governed definition; `HAS` invokes a registered possession or participation predicate. |
| Quantification | `EVERY`, `NO`, `AT LEAST ONE`, `AT MOST ONE`, `EXACTLY ONE` | The token binds the immediately following registered kind over the Claim's complete Applicability. `NO` asserts zero qualifying members. A bare plural or omitted required quantity has no interpretation. |
| Modality | `MUST`, `MUST NOT`, `MAY` | `MUST` establishes an obligation, `MUST NOT` establishes a prohibition, and `MAY` establishes permission only. None expresses likelihood, advice, preference, or prediction. |
| Logic | `AND`, `OR`, `EXACTLY ONE OF`, `ALL OF`, `ANY OF`, `IF`, `THEN` | `AND` and `ALL OF` require every member; `OR` and `ANY OF` are inclusive; `EXACTLY ONE OF` is exclusive; `IF ... THEN ...` scopes implication to its declared antecedent and consequent. |
| Scope | `FOR`, `WHEN`, `WHILE`, `WITHIN`, `WHETHER`, `TO`, `FROM`, `BY` | These tokens introduce the target, condition, persistent condition, Applicability boundary, decision question, outcome, source, or registered Method required by the selected statement form. |
| Role-form operation | `DECIDE`, `DERIVE`, `PERFORM`, `DELIVER`, `PASSES IF`, `FAILS IF`, `HOLD` | These tokens supply only the fixed operation of the registered Concern, derivation, Method, Delivery, Evaluation, or invariant form. Their statement-form slots determine all participants and conditions; the tokens do not establish a reusable content predicate outside that form. |

`AND` and `OR` must not occur at the same nesting level. Negation is admitted only through `MUST NOT`, `NO`, and `IS NOT`. `unless`, double negation, `not every`, `and/or`, pronouns, anaphora, ellipsis, bare plurals, comparative adjectives without a registered scale, passive clauses with an omitted participant, and unstated semantic defaults have no `cce_1` interpretation.

A condition follows the clause it constrains. `WHEN` precedes `WHILE`, and `WHILE` precedes `WITHIN` when more than one is present. Parenthetical wording does not establish logical grouping. A numbered `ALL OF` or `ANY OF` list supplies the only multi-item grouping in `cce_1`.

Absence of an asserted fact means unknown, not false. A predicate may use closed-world interpretation only when its registered signature names the exact exhaustive source and Evaluation that establish completeness. An unsupported token, unresolved reference, unknown term, undeclared predicate, kind-invalid participant, invalid cardinality, or ambiguous scope yields no CCE Claim.
